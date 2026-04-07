# TEST RESULTS - LAB 4

### Test Case 1
**User:** xin chào tôi muốn đi du lịch nhưng chưa biết đi đâu.
TravelBuddy đang suy nghĩ...  
**TravelBuddy:** Chào bạn! Rất vui khi bạn muốn đi du lịch. Để giúp bạn tìm điểm đến thú vị, bạn có thể cho mình biết một số thông tin không? Ví dụ như:

1. Bạn thích khám phá thiên nhiên hay văn hóa?
2. Ngân sách dự kiến cho chuyến đi của bạn là bao nhiêu?
3. Bạn có thời gian đi vào khoảng thời gian nào không?

Từ đó mình có thể gợi ý cho bạn một số điểm đến hấp dẫn!

---

### Test Case 2
**User:** tìm giúp tôi chuyến bay từ hà nội đi đà nẵng  
TravelBuddy đang suy nghĩ...  
`Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Đà Nẵng'})`
**TravelBuddy:** Dưới đây là danh sách chuyến bay từ Hà Nội đến Đà Nẵng:

1. ***Vietnam Airlines***: 06:00 - 07:20, giá 1,450,000đ (economy).
2. ***VietJet Air***: 08:30 - 09:50, giá 890,000đ (economy).

Bạn có cần thêm thông tin gì không hay muốn đặt vé?

---

### Test Case 3
**User:** tôi ở Hà nội, tôi muốn đi phú quốc 2 đêm, budget 5 tr, tư vấn giúp. 
TravelBuddy đang suy nghĩ...  
TravelBuddy đang suy nghĩ...  
`Gọi tool: search_flights({'origin': 'Hà Nội', 'destination': 'Phú Quốc'})`
`Gọi tool: search_hotels({'city': 'Phú Quốc', 'max_price_per_night': 2500000})`
**TravelBuddy:** Chuyến đi Phú Quốc của bạn sẽ rất thú vị! Đây là một số thông tin bạn cần biết:

**Chuyến bay:**
- Vietnam Airlines (07:00-09:15): 2,100,000đ [economy]
- VietJet Air (10:00-12:15): 1,350,000đ [economy]

**Khách sạn:**
- **9Station Hostel (2 sao):** 200,000đ/đêm - Khu vực: Dương Đông (Rating: 4.5)
- **Lahana Resort (3 sao):** 800,000đ/đêm - Khu vực: Dương Đông (Rating: 4.0)

**Tính toán tổng chi phí:**
- Chọn 2 đêm ở 9Station Hostel: 200,000đ * 2 = 400,000đ
- Chọn chuyến bay VietJet Air: 1,350,000đ

**Tổng chi phí ước tính:**
- Tổng chi phí: 1,350,000đ (vé máy bay) + 400,000đ (khách sạn) = 1,750,000đ

**Ngân sách còn lại sau khi chi phí tổng là 5 triệu:**
- 5,000,000đ - 1,750,000đ = 3,250,000đ

**Gợi ý thêm:**
Với số tiền còn lại, bạn có thể chi cho các hoạt động vui chơi, ăn uống tại Phú Quốc. Bạn có thể tham quan Dinh Cậu, Bãi Sao, hay thử các món hải sản tươi ngon ở các quán ven biển.

Nếu bạn muốn đặt vé máy bay hoặc khách sạn, hãy cho mình biết nhé!

---

### Test Case 4
**User:** tôi muốn đặt khách sạn.  
TravelBuddy đang suy nghĩ...  
**TravelBuddy:** Để giúp bạn đặt khách sạn, mình cần biết một số thông tin hơn. Bạn đang muốn đặt khách sạn ở đâu và có ngân sách cụ thể nào không?

---

### Test Case 5
**User:** giải giúp tôi bài tập python về link list.  
TravelBuddy đang suy nghĩ...  
Trả lời trực tiếp.  
**TravelBuddy**: Xin lỗi, nhưng mình chỉ hỗ trợ về du lịch và các thông tin liên quan đến việc đặt phòng, đặt vé máy bay. Nếu bạn có câu hỏi nào về chuyến đi của mình, đừng ngần ngại hỏi mình nhé!
