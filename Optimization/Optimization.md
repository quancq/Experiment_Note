Gradient Descent
=========================

# Mục lục

# 1. Tổng quan
* Dùng để tìm nghiệm để tối ưu hóa 1 hàm số
* Kịch bản: cần tối thiểu hóa hàm J(theta) với theta là tham số của model, ta sẽ cập nhật theta theo hướng **ngược** với hướng đạo hàm của hàm J theo theta.

# 2. Các biến thể của Gradient descent (GD variants)
* Có 3 biến thể của GD, được xác định dựa theo *lượng* dữ liệu dùng để tính gradient của hàm mục tiêu
* Tùy vào lượng dữ liệu dùng nhiều hay ít, ta sẽ có trade-off
	* Dùng nhiều dữ liệu trong 1 lần update: tham số được update chính xác hơn, nhưng tốn thời gian thực hiện update
	* Dùng ít dữ liệu trong 1 lần update: tham số được update kém chính xác hơn, nhưng giảm được thời gian thực hiện update (trong TH này, hàm mục tiêu sẽ tăng - giảm đột ngột, biến động hơn)
* Ẩn dụ: Khi cần hỏi 1 nhóm người (dữ liệu) về hướng đường cần tìm (hỏi hướng đạo hàm) để đến đích (tối ưu hóa obj fnc)
	* Nếu mỗi lần đến 1 vùng, ta phải hỏi đủ 1 nhóm người thì ta thường tìm được hướng đi tốt hơn, nhưng tốn thời gian hỏi
	* Nếu mỗi lần đến 1 vùng, ta chỉ hỏi 1 vài người thì độ chính xác của kết quả thường biến động nhiều (lúc tốt, lúc xấu), nhưng giảm được thời gian hỏi đường

## 2.1.

# Tài liệu tham khảo
* [An overview of gradient descent optimization algorithms](http://ruder.io/optimizing-gradient-descent/)