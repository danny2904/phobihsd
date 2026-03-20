Dưới đây là **góp ý chi tiết cho phần 3. Methodology**, tập trung vào:

1. **Logic trình bày phương pháp**
2. **Mức độ đầy đủ của mô tả mô hình**
3. **Cách trích dẫn tài liệu theo chuẩn IEEE [ ]**
4. **Các điểm reviewer NLP thường yêu cầu trong Method section**

Phân tích dựa trên nội dung phần Methodology của bản thảo .

---

# 1. Cấu trúc phần Methodology còn quá ngắn

Phần Methodology hiện tại chỉ gồm **một đoạn mô tả tổng quát kiến trúc**:

PhoBiHSD uses a three-stage architecture. First, input comments are normalized and tokenized with PhoBERT tokenizer. Second, PhoBERT encodes each sequence into contextual embeddings. Third, a bidirectional LSTM layer captures additional left-right sequence dependencies before a final classification head predicts one of the three labels. 

Vấn đề của cách viết này là:

* chỉ mô tả pipeline ở mức **ý tưởng**
* chưa mô tả **chi tiết kỹ thuật**

Trong các bài NLP conference, phần Methodology thường được chia thành **3–4 tiểu mục**.

### Đề xuất cấu trúc

Có thể tổ chức lại phần Methodology như sau:

3. Methodology

3.1 Text preprocessing

3.2 PhoBERT encoder

3.3 BiLSTM classification layer

3.4 Imbalance handling strategy

Cách chia này giúp reviewer dễ đọc và dễ đánh giá phương pháp.

---

# 2. Phần mô tả PhoBERT chưa có citation

Đoạn hiện tại viết:

PhoBERT encodes each sequence into contextual embeddings.

Đây là một mô hình pretrained nổi tiếng trong NLP tiếng Việt nên **bắt buộc phải trích dẫn bài báo gốc**.

Trong reference list của bài báo đã có:

Nguyen & Nguyen 2020 PhoBERT.

Do đó câu này nên được sửa thành:

PhoBERT, a pretrained Vietnamese language model based on the RoBERTa architecture, is used to encode each input sequence into contextual embeddings [5].

Việc thêm citation giúp:

* ghi nhận đúng công trình gốc
* tuân thủ chuẩn trích dẫn IEEE.

---

# 3. Thiếu mô tả chi tiết về kiến trúc mô hình

Methodology hiện tại chưa trả lời các câu hỏi quan trọng mà reviewer thường đặt ra:

* embedding dimension của PhoBERT là bao nhiêu
* hidden size của BiLSTM
* có sử dụng dropout hay không
* output layer là gì.

Trong các bài NLP, phần này thường được mô tả rõ.

### Đề xuất bổ sung đoạn mô tả

The contextual representations produced by PhoBERT are passed to a bidirectional LSTM layer, which captures sequential dependencies from both forward and backward directions. The final hidden states are then fed into a fully connected classification layer followed by a softmax function to predict the probability distribution over the three classes.

Ngoài ra nên bổ sung các thông số như:

* hidden size
* dropout rate.

---

# 4. Chưa giải thích rõ vai trò của BiLSTM

Trong phần Methodology hiện tại, BiLSTM chỉ được mô tả ngắn gọn:

a bidirectional LSTM layer captures additional left-right sequence dependencies.

Reviewer có thể đặt câu hỏi:

Why is BiLSTM necessary when PhoBERT already captures contextual information?

Do đó cần giải thích rõ motivation.

### Đề xuất chỉnh sửa

A bidirectional LSTM layer is introduced on top of the PhoBERT embeddings to further model sequential dependencies and refine contextual interactions across tokens.

Câu này giải thích:

* PhoBERT tạo contextual embedding
* BiLSTM giúp học thêm pattern tuần tự.

---

# 5. Phần preprocessing mô tả chưa đầy đủ

Methodology có nhắc đến preprocessing:

The preprocessing pipeline standardizes schema fields, removes invalid entries, maps labels to numerical IDs, and applies truncation/padding. 

Đây là một đoạn hợp lý, nhưng vẫn thiếu một số thông tin:

* tokenization strategy
* maximum sequence length
* handling emojis hoặc slang.

Trong các bài NLP, preprocessing thường cần mô tả rõ để đảm bảo **reproducibility**.

### Đề xuất bổ sung

Before model training, the input comments are normalized and tokenized using the PhoBERT tokenizer. All sequences are truncated or padded to a fixed maximum length to ensure consistent input representation.

---

# 6. Phần imbalance handling chưa đủ rõ

Bài báo nhấn mạnh vào **class imbalance**, nhưng phần Methodology chưa giải thích rõ cách thực hiện.

Đoạn hiện tại viết:

Resampling is applied only to the training split to avoid leakage. 

Đây là một điểm đúng nhưng chưa đủ.

Reviewer thường muốn biết:

* oversampling thực hiện như thế nào
* sampling ratio là bao nhiêu.

### Đề xuất bổ sung

To address class imbalance, random oversampling is applied to the training set to increase the number of minority class samples. The resampling process is restricted to the training split to avoid data leakage during evaluation.

---

# 7. Thiếu sơ đồ kiến trúc mô hình

Trong nhiều bài NLP, phần Methodology thường có **một figure mô tả pipeline**.

Phần Methodology hiện tại chỉ có mô tả bằng văn bản.

Nếu bổ sung một hình như sau sẽ giúp bài báo rõ ràng hơn:

Input text
→ PhoBERT encoder
→ BiLSTM layer
→ Dense classifier
→ Softmax output.

Figure này giúp reviewer hiểu nhanh kiến trúc.

---

# 8. Thiếu phân tích độ phức tạp hoặc thiết kế kiến trúc

Một số reviewer có thể hỏi:

Why use a hybrid architecture instead of a pure transformer classifier?

Do đó Methodology nên có một câu giải thích thiết kế.

Ví dụ:

The hybrid architecture aims to combine the contextual encoding ability of transformer models with the sequential modeling capability of recurrent networks.

---

# 9. Đánh giá tổng thể phần Methodology

| Tiêu chí                | Đánh giá      |
| ----------------------- | ------------- |
| Clarity of architecture | trung bình    |
| Technical detail        | còn thiếu     |
| Citation usage          | cần bổ sung   |
| Reproducibility         | cần cải thiện |

### Mức hiện tại

≈ **6.5 / 10**

### Sau khi chỉnh sửa

≈ **8.5 / 10**

---

# 10. Các câu hỏi reviewer có thể đặt ra

Nếu nộp conference NLP, reviewer có thể hỏi:

1

Why combine PhoBERT with BiLSTM instead of directly using the transformer classifier?

2

What is the architecture configuration of the BiLSTM layer?

3

How does the resampling ratio affect model performance?

---