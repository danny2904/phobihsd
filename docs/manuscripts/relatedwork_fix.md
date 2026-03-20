Dưới đây là **góp ý chi tiết cho phần Related Work**, tập trung vào hai khía cạnh chính:

1. **Cấu trúc và logic trình bày theo chuẩn bài báo NLP**
2. **Cách trích dẫn tài liệu theo chuẩn IEEE dạng ngoặc vuông [ ]**

Phân tích dựa trên nội dung phần Related Work trong bản thảo .

---

# 1. Cấu trúc Related Work còn quá ngắn và chưa phân nhóm rõ ràng

Phần Related Work hiện tại của bản thảo có cấu trúc tương đối đơn giản và chỉ gồm một vài đoạn ngắn. Nội dung chủ yếu đề cập đến:

* ViHSD dataset
* một số mô hình transformer
* PhoBERT

Tuy nhiên, trong các bài báo NLP conference hoặc journal, phần Related Work thường được **chia thành các nhóm nghiên cứu rõ ràng**.

Cấu trúc thường gặp gồm:

1. Hate speech detection in NLP
2. Vietnamese hate speech datasets and models
3. Class imbalance handling in NLP

Phần Related Work của bản thảo hiện tại chưa tách rõ các nhóm này, khiến mạch trình bày chưa thật sự rõ ràng.

### Đề xuất

Có thể tổ chức lại thành ba tiểu phần như sau:

* Hate speech detection research
* Vietnamese hate speech detection
* Imbalanced learning in NLP

Cách phân nhóm này giúp reviewer dễ nhận ra rằng bài báo đã **đặt nghiên cứu của mình trong bối cảnh học thuật rộng hơn**.

---

# 2. Thiếu các nghiên cứu tổng quan về hate speech detection

Phần Related Work hiện tại chủ yếu trích dẫn các nghiên cứu gần đây, nhưng lại thiếu các **survey paper quan trọng trong lĩnh vực hate speech detection**.

Trong nhiều bài báo NLP, phần mở đầu của Related Work thường nhắc đến các survey để:

* giới thiệu toàn cảnh lĩnh vực
* định vị bài nghiên cứu trong bối cảnh chung.

Ví dụ có thể bổ sung một đoạn như sau:

Hate speech detection has been widely studied in natural language processing, with early approaches relying on lexical features and traditional machine learning classifiers. More recent studies employ deep learning and transformer based models to capture contextual representations of offensive language [1], [2].

Ở đây:

* [1] có thể là survey về hate speech detection
* [2] có thể là survey về toxicity detection.

Việc bổ sung các survey này giúp phần Related Work **có nền tảng học thuật rõ ràng hơn**.

---

# 3. Phần nghiên cứu về tiếng Việt còn hơi ngắn

Đoạn Related Work hiện tại viết:

ViHSD established an important benchmark for Vietnamese hate speech detection with three labels: Clean, Offensive, and Hate [1]. Subsequent work improved results through augmentation and stronger language models, including BERTology variants and specialized Vietnamese social-media pretraining such as ViSoBERT [2], [3].

Đây là một đoạn hợp lý, nhưng vẫn có hai hạn chế.

### Thứ nhất: chưa giải thích đóng góp của từng nghiên cứu

Citation chỉ được liệt kê dưới dạng [1], [2], [3] nhưng chưa mô tả rõ vai trò của từng nghiên cứu.

Trong các bài báo NLP, reviewer thường muốn thấy:

* dataset paper
* augmentation paper
* language model paper

được giải thích ngắn gọn.

### Đề xuất chỉnh sửa

Vietnamese hate speech detection has attracted increasing research attention in recent years. The ViHSD dataset introduced a large scale benchmark for Vietnamese hate speech classification with three labels: Clean, Offensive, and Hate [3]. Subsequent studies explored data augmentation strategies and improved transformer based models to enhance classification performance on this dataset [4]. In addition, pretrained Vietnamese language models such as PhoBERT and ViSoBERT have been shown to provide strong contextual representations for social media text processing [5], [6].

Đoạn này:

* giải thích vai trò của từng nghiên cứu
* giữ citation theo chuẩn IEEE.

---

# 4. Thiếu nhóm nghiên cứu về class imbalance

Phần Related Work có đề cập đến mất cân bằng dữ liệu nhưng chưa tách thành một nhóm nghiên cứu riêng.

Trong khi đó, **class imbalance là một trong những trọng tâm của bài báo**.

Nếu không có phần tổng quan về imbalanced learning, reviewer có thể cho rằng phần Related Work **chưa bao phủ đầy đủ lĩnh vực nghiên cứu**.

### Đề xuất bổ sung đoạn sau

Handling imbalanced datasets has been widely studied in machine learning and natural language processing. Traditional approaches include data level techniques such as oversampling and undersampling, as well as algorithm level strategies designed to reduce bias toward majority classes [7], [8]. In hate speech detection tasks, class imbalance often leads to poor recognition of minority categories such as explicit hate expressions.

Đoạn này giúp liên kết rõ hơn giữa:

* nghiên cứu trước
* phương pháp được đề xuất trong bài báo.

---

# 5. Thiếu phần chuyển tiếp sang nghiên cứu hiện tại

Một lỗi phổ biến trong Related Work là **không kết nối rõ ràng giữa nghiên cứu trước và nghiên cứu hiện tại**.

Phần Related Work của bản thảo hiện tại kết thúc khá đột ngột.

Nên bổ sung một câu kết nối như sau:

Although transformer based models have achieved promising results for hate speech detection, the impact of hybrid architectures and imbalance handling strategies remains insufficiently explored for Vietnamese social media data. This motivates the proposed PhoBiHSD architecture investigated in this study.

Câu này giúp:

* nhấn mạnh **research gap**
* dẫn sang phần methodology.

---

# 6. Số lượng citation trong Related Work

Hiện tại phần Related Work của bản thảo sử dụng khoảng **7–10 citation**.

Đối với một bài báo NLP conference, số lượng này **tương đối chấp nhận được**, nhưng có thể cải thiện thêm.

Một Related Work tiêu chuẩn thường có:

* khoảng **10–15 citation**

Tuy nhiên nếu bài báo ngắn thì khoảng **8–10 citation** vẫn được xem là hợp lý.

---

# 7. Đánh giá tổng thể phần Related Work

| Tiêu chí                      | Đánh giá      |
| ----------------------------- | ------------- |
| Coverage of research field    | trung bình    |
| Structure clarity             | cần cải thiện |
| Citation explanation          | còn thiếu     |
| Connection to proposed method | yếu           |

### Mức hiện tại

≈ **6.5 / 10**

### Sau khi chỉnh sửa

≈ **8.5 / 10**

---