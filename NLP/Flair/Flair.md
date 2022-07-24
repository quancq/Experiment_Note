Flair
=======================

#1. Giới thiệu
* Thư viện NLP dùng framework Pytorch
* Cung cấp chức năng: sử dụng model có sẵn (hỗ trợ 1 số ngôn ngữ), sử dụng hoặc train 1 số embedding (Flair, Bert, Elmo), train model các task: ner, pos, classification, chunking

#2. Tutorial Document
## 2.1. Kiểu dữ liệu
* Có 2 đối tượng chính là Sentence (chứa text của 1 câu, cụ thể là list các Token) và Token
* Class Label dùng để mô hình hóa tag
* Mỗi token có thể gắn các tag (pos, ner). Có 2 hàm ``token.add_tag('ner', 'PER')``, ``token.get_tag('ner')`` để thao tác với token và tag. Mỗi tag có thuộc tính ``tag.value`` (text của tag, vd PER) và ``tag.score`` là độ tin cậy dự đoán (nếu tự add thì score = 1.0)
* Mỗi sentence có thể gắn 1/nhiều label (nhãn cho bài toán classification)
	* Thêm label: ``sentence.add_label('topic', 'sports')``
	* Truy cập label: ``sentence.labels``

* Sử dụng Flair cho việc tagging (ner, pos,...)
	* Load sequence tagger (1 class trong Flair), cần truyền model path, hoặc tên pretrained model
	* Đóng gói text vào đối tượng Sentence
	* Gọi hàm predict, có thể truyền 1 list Sentence. Duyệt token trong sentence để lấy ra tag value và score.

* Flair hỗ trợ sử dụng pretrained embedding và train embedding trên dữ liệu riêng
	* Sử dụng pretrained model: Glove, Word2vec, Fasttext, Transformer (Bert,...),... (Flair dùng gensim để load Word2vec, Fasttext, dùng transformer huggingface để load transformer model)
	* Tự train trên dữ liệu riêng: Flair, PooledFlair

* Document embedding: Flair hỗ trợ 4 kiểu document embedding (2 cáu đầu cần sử dụng word embedding)
	* Pooling: min, max, mean. Có thể transform nonlinear các word embedding trước khi vào pooling của doc embedding
	* RNN: dùng kiểu embedding này thì cần finetune trên downstream task. Khi train Flair model (classification, seq tagging) thì sẽ train luôn cả mạng RNN này.
	* Transformer
	* SentenceTransformer: model được pretrained hướng đến việc sinh ra biểu diễn câu
	
* Train Flair embedding