from langchain_core.tools import tool

# MOCK DATA
FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1450000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1350000, "class": "economy"},
    ],
    # Bạn có thể thêm data từ ảnh vào đây...
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250000, "area": "Hải Châu", "rating": 4.6},
    ],
    "Phú Quốc": [
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200000, "area": "Dương Đông", "rating": 4.5},
    ]
}

@tool
def search_flights(origin: str, destination: str) -> str:
    """Tìm kiếm các chuyến bay giữa hai thành phố."""
    flights = FLIGHTS_DB.get((origin, destination))
    if not flights:
        # Thử tra ngược chiều
        flights = FLIGHTS_DB.get((destination, origin))
        if not flights:
            return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."
    
    res = f"Danh sách chuyến bay từ {origin} đến {destination}:\n"
    for f in flights:
        res += f"- {f['airline']} ({f['departure']}-{f['arrival']}): {f['price']:,}đ [{f['class']}]\n"
    return res

@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa."""
    hotels = HOTELS_DB.get(city, [])
    filtered = [h for h in hotels if h['price_per_night'] <= max_price_per_night]
    filtered.sort(key=lambda x: x['rating'], reverse=True)
    
    if not filtered:
        return f"Không tìm thấy khách sạn tại {city} với giá dưới {max_price_per_night:,}đ. Hãy thử tăng ngân sách."
    
    res = f"Khách sạn phù hợp tại {city} (sắp xếp theo đánh giá):\n"
    for h in filtered:
        res += f"- {h['name']} ({h['stars']} sao): {h['price_per_night']:,}đ/đêm - Khu vực: {h['area']} (Rating: {h['rating']})\n"
    return res

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """Tính toán ngân sách còn lại. Expenses format: 'tên:số_tiền,tên:số_tiền'"""
    try:
        items = {}
        for item in expenses.split(','):
            name, price = item.split(':')
            items[name.strip()] = int(price.strip())
        
        total_spent = sum(items.values())
        remaining = total_budget - total_spent
        
        res = "--- Bảng chi phí ---\n"
        for k, v in items.items():
            res += f"- {k.replace('_', ' ').capitalize()}: {v:,}đ\n"
        res += f"---\nTổng chi: {total_spent:,}đ\n"
        res += f"Ngân sách: {total_budget:,}đ\n"
        res += f"Còn lại: {remaining:,}đ\n"
        
        if remaining < 0:
            res += f"⚠️ Cảnh báo: Bạn đang vượt ngân sách {abs(remaining):,}đ!"
        return res
    except:
        return "Lỗi định dạng expenses. Vui lòng dùng định dạng 'tên:số_tiền,tên:số_tiền'."