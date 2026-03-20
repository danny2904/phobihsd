Dưới đây là **phiên bản viết lại phần góp ý cho Discussion**, theo đúng phong cách của bài mẫu. Phần Discussion **không dùng citation**, tập trung vào:

* giải thích kết quả
* phân tích xu hướng
* phân tích lỗi
* liên hệ với mục tiêu nghiên cứu

Cách viết này tương tự cấu trúc của phần *Results and Discussion* trong bài mẫu  (phần 4.5–4.7).

---

# Góp ý phần Discussion (viết lại theo phong cách bài mẫu)

Phần Discussion của bản thảo đã trình bày kết quả thực nghiệm và so sánh giữa các mô hình khác nhau, tuy nhiên cách diễn giải kết quả vẫn còn tương đối ngắn và thiên về mô tả số liệu. Để phù hợp với cách trình bày của các bài báo trong lĩnh vực NLP, phần Discussion nên tập trung nhiều hơn vào **giải thích xu hướng kết quả, phân tích nguyên nhân và đánh giá tác động của phương pháp đề xuất**.

---

## 1. Phần mở đầu Discussion nên nêu rõ mục tiêu phân tích

Hiện tại phần Discussion bắt đầu trực tiếp bằng việc so sánh kết quả giữa các mô hình. Cách viết này khiến phần phân tích hơi đột ngột.

Trong nhiều bài báo NLP, phần Discussion thường bắt đầu bằng một câu định hướng, ví dụ nêu rõ mục tiêu của phần phân tích kết quả.

Có thể bổ sung một câu mở đầu như sau:

This section analyzes the experimental results to evaluate the effectiveness of the proposed PhoBiHSD architecture and to examine the impact of different imbalance handling strategies on Vietnamese hate speech classification.

Câu này giúp người đọc hiểu rằng phần tiếp theo sẽ tập trung vào **đánh giá mô hình và phân tích kết quả thực nghiệm**.

---

## 2. Phân tích kết quả so sánh mô hình cần sâu hơn

Phần hiện tại đã chỉ ra rằng PhoBiHSD đạt Macro-F1 cao hơn so với một số baseline. Tuy nhiên phần Discussion mới chỉ nêu sự khác biệt về số liệu mà chưa giải thích rõ **nguyên nhân của sự cải thiện**.

Trong các bài báo NLP, khi một mô hình đạt kết quả tốt hơn, phần Discussion thường phân tích các yếu tố sau:

* khả năng biểu diễn ngữ cảnh của transformer
* khả năng học quan hệ tuần tự của BiLSTM
* tác động của imbalance handling.

Có thể mở rộng phần phân tích theo hướng:

The improved Macro-F1 score suggests that combining contextual representations from PhoBERT with the sequential modeling capability of BiLSTM helps capture subtle contextual cues in Vietnamese hate speech. The hybrid architecture allows the model to leverage both deep contextual embeddings and sequential dependencies across tokens, which is particularly useful for identifying implicit or context-dependent offensive expressions.

Cách viết này giúp **giải thích rõ hơn vì sao mô hình đạt kết quả tốt hơn**.

---

## 3. Phân tích kết quả imbalance nên chi tiết hơn

Bài báo có một bảng riêng để so sánh các phương pháp xử lý mất cân bằng dữ liệu. Đây là điểm mạnh của nghiên cứu, nhưng phần Discussion mới chỉ nêu rằng ROS đạt kết quả tốt nhất.

Phần phân tích nên giải thích vì sao các phương pháp undersampling kém hiệu quả hơn.

Có thể mở rộng như sau:

The comparison of imbalance handling strategies shows that random oversampling produces the best overall performance in this experimental setting. This result suggests that preserving minority class samples is important for hate speech classification. In contrast, aggressive undersampling methods remove a large portion of majority class data, which may eliminate useful contextual patterns and reduce the model’s ability to generalize.

Cách viết này giúp người đọc hiểu rõ **nguyên nhân của sự khác biệt giữa các phương pháp**.

---

## 4. Phân tích lỗi phân loại nên được mở rộng

Phần Discussion có đề cập đến việc nhiều lỗi xảy ra giữa hai lớp Hate và Offensive. Đây là một nhận xét quan trọng nhưng hiện vẫn còn khá ngắn.

Trong các bài NLP, phần Discussion thường phân tích sâu hơn các trường hợp lỗi, đặc biệt là khi các lớp có ranh giới ngữ nghĩa gần nhau.

Có thể mở rộng phần này theo hướng:

A closer inspection of the prediction errors reveals that many misclassifications occur between the Hate and Offensive categories. This observation indicates that the semantic boundary between these classes is often ambiguous and highly dependent on contextual interpretation. Some comments may contain indirect insults or sarcasm that are difficult to distinguish from explicit hate expressions.

Phân tích này giúp làm rõ **thách thức của bài toán**.

---

## 5. Nên bổ sung nhận xét về độ khó của dữ liệu

Trong bài toán hate speech detection, dữ liệu thường chứa nhiều biểu thức ngôn ngữ không chuẩn như:

* viết tắt
* emoji
* tiếng lóng.

Phần Discussion có thể nhấn mạnh rằng các yếu tố này ảnh hưởng đến độ chính xác của mô hình.

Ví dụ:

The difficulty of the task is further increased by the informal nature of Vietnamese social media language, which frequently includes slang expressions, abbreviations, and implicit offensive meanings. Such linguistic variations make automatic classification more challenging and contribute to the observed misclassification cases.

---

## 6. Cần bổ sung phần đánh giá hạn chế của phương pháp

Một điểm còn thiếu trong phần Discussion là **đánh giá các hạn chế của mô hình**.

Trong các bài báo khoa học, việc thừa nhận hạn chế giúp tăng tính thuyết phục và minh bạch của nghiên cứu.

Có thể bổ sung đoạn sau:

Despite the improvements observed in the experiments, the proposed model may still struggle with implicit hate expressions and sarcasm, which require deeper contextual understanding. In addition, the performance of the model is evaluated on a single dataset, which may limit its generalizability to other social media domains.

---

## 7. Cần liên kết Discussion với hướng nghiên cứu tiếp theo

Phần cuối của Discussion nên tạo cầu nối sang phần Conclusion.

Có thể thêm một câu như sau:

These observations highlight the need for further research on more advanced contextual modeling strategies and more robust imbalance handling techniques for Vietnamese hate speech detection.

---

# Đánh giá tổng thể phần Discussion

| Tiêu chí                         | Đánh giá    |
| -------------------------------- | ----------- |
| Giải thích kết quả               | khá         |
| Phân tích nguyên nhân            | cần mở rộng |
| Phân tích lỗi                    | còn ngắn    |
| Đánh giá hạn chế                 | chưa rõ     |
| Liên kết với mục tiêu nghiên cứu | trung bình  |

### Mức hiện tại

Khoảng **6.5 / 10**

### Sau khi chỉnh sửa

Khoảng **8.5 / 10**

---
