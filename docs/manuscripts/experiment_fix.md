Dưới đây là **góp ý chi tiết cho phần 4. Experimental Setup**, tập trung vào ba khía cạnh chính thường được reviewer NLP đánh giá:

1. **độ đầy đủ của thiết lập thí nghiệm**
2. **tính tái lập (reproducibility)**
3. **cách trích dẫn và trình bày theo chuẩn IEEE [ ]**

Phân tích dựa trên nội dung phần Experiment trong bản thảo .

---

# 1. Cấu trúc phần Experiment còn đơn giản

Phần 4 của bản thảo hiện gồm hai nội dung chính:

* Dataset description
* Environment and training setup

Cách trình bày này đúng hướng, nhưng trong các bài NLP conference, phần Experiment thường được chia thành **nhiều tiểu mục rõ ràng hơn**.

Một cấu trúc phổ biến là:

4. Experiments

4.1 Dataset

4.2 Evaluation metrics

4.3 Baseline models

4.4 Implementation details

Hiện tại bài báo **thiếu hai tiểu mục quan trọng**:

* evaluation metrics
* baseline description

---

# 2. Phần Dataset viết hợp lý nhưng cần thêm citation

Đoạn hiện tại viết:

We use ViHSD with 33,400 Vietnamese social-media comments labeled as Clean, Offensive, and Hate. Annotation quality in the original release reports Cohen's kappa around 0.52. 

Đây là thông tin đúng về dataset, tuy nhiên khi mô tả dataset cần **trích dẫn paper gốc của dataset** theo chuẩn IEEE.

Có thể viết lại:

The experiments are conducted on the ViHSD dataset, which contains 33,400 Vietnamese social media comments annotated into three categories: Clean, Offensive, and Hate [1]. The dataset reports an inter annotator agreement of approximately Cohen's kappa = 0.52, reflecting the inherent difficulty of hate speech annotation.

Việc trích dẫn dataset giúp:

* đảm bảo attribution
* tăng độ tin cậy học thuật.

---

# 3. Phần phân bố dữ liệu nên giải thích rõ hơn

Bài báo đã đưa **Table 1 và Table 2** mô tả phân bố dữ liệu.

Điểm này là một ưu điểm vì reviewer thường muốn thấy:

* class distribution
* train dev test split.

Tuy nhiên phần văn bản nên nhấn mạnh rõ hơn **mức độ mất cân bằng dữ liệu**.

Ví dụ có thể bổ sung một câu:

The dataset exhibits a strong class imbalance, with the Clean class accounting for approximately 72% of the total samples, while the Offensive and Hate categories appear significantly less frequently.

Câu này giúp liên kết tốt hơn với **mục tiêu nghiên cứu về imbalance**.

---

# 4. Phần Evaluation Metrics đang thiếu

Trong phần Experiment hiện tại, bài báo **không có tiểu mục riêng cho evaluation metrics**.

Trong khi đó phần Results lại báo cáo các chỉ số:

* Accuracy
* Macro F1
* Precision
* Recall.

Reviewer thường yêu cầu giải thích **vì sao chọn metric đó**.

Có thể thêm một tiểu mục như sau:

4.2 Evaluation Metrics

Following previous hate speech detection studies, we evaluate the classification performance using Accuracy, Precision, Recall, and Macro F1 score. Macro F1 is particularly important for imbalanced datasets because it assigns equal weight to each class regardless of its frequency.

Phần này giúp:

* giải thích metric
* liên hệ với imbalance.

---

# 5. Thiếu mô tả baseline models

Trong phần Results, bài báo so sánh với nhiều mô hình:

* TextCNN
* GRU
* mBERT
* XLM-R
* GPT 4o

Tuy nhiên trong phần Experiment **không có tiểu mục mô tả các baseline này**.

Đây là một thiếu sót lớn vì reviewer thường muốn biết:

* baseline lấy từ đâu
* có được train lại hay không.

Có thể thêm tiểu mục:

4.3 Baseline Models

We compare the proposed model with several representative baselines used in Vietnamese hate speech detection studies, including traditional neural models such as TextCNN and GRU, as well as transformer based models such as mBERT and XLM R.

---

# 6. Phần Implementation details cần đầy đủ hơn

Đoạn hiện tại viết:

Experiments were run on Ubuntu 22.04 with an NVIDIA RTX 4060 Ti GPU using PyTorch and HuggingFace Transformers. 

Đây là thông tin tốt, nhưng reviewer NLP thường muốn biết thêm:

* learning rate
* optimizer
* batch size
* training epochs.

Một số thông tin đã xuất hiện nhưng nên trình bày rõ hơn.

Ví dụ:

The models are implemented using PyTorch and the HuggingFace Transformers library. Training is performed using the Adam optimizer with a learning rate of 2e-5, a batch size of 16, and four training epochs.

Việc mô tả chi tiết giúp **đảm bảo reproducibility**.

---

# 7. Maximum sequence length đang hơi mâu thuẫn

Phần Experiment viết:

maximum sequence length 100 in baseline table and 256 in PhoBiHSD pipeline script. 

Điều này có thể gây thắc mắc cho reviewer vì:

* baseline và model chính dùng **khác sequence length**.

Nếu không giải thích rõ, reviewer có thể đặt câu hỏi về **fair comparison**.

Nên bổ sung một câu giải thích:

For fair comparison, all transformer based models are trained under the same maximum sequence length unless otherwise specified.

---

# 8. Thiếu thông tin về random seed

Trong nhiều bài NLP, phần Experiment cần nói rõ:

* random seed
* number of runs.

Hiện tại bài báo chưa đề cập đến điều này.

Có thể bổ sung:

All experiments are conducted using a fixed random seed to ensure reproducibility.

---

# 9. Thiếu link code hoặc repository

Trong các bài NLP hiện nay, reviewer thường đánh giá cao **reproducibility**.

Nếu có code repository nên đề cập trong phần Experiment.

Ví dụ:

The implementation code and experiment scripts will be released publicly to facilitate reproducibility.

---

# 10. Đánh giá tổng thể phần Experiment

| Tiêu chí             | Đánh giá      |
| -------------------- | ------------- |
| Dataset description  | tốt           |
| Experimental design  | trung bình    |
| Baseline description | thiếu         |
| Evaluation metrics   | thiếu         |
| Reproducibility      | cần cải thiện |

### Mức hiện tại

≈ **6.5 / 10**

### Sau chỉnh sửa

≈ **8.5 / 10**

---

# 11. Các câu hỏi reviewer có thể đặt ra

Một số câu hỏi reviewer NLP thường đặt cho phần Experiment:

1

Why is Macro F1 chosen as the main evaluation metric?

2

Are all baselines trained under the same experimental conditions?

3

How sensitive is the model to different resampling strategies?

---