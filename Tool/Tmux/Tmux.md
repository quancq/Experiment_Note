Tmux
===========================

# 1. Session
* Tạo session mới tên là ``temp``: ``tmux new -s temp``
* Thoát session (vẫn giữ session tại server): ``Ctrl+b d``
* Vào lại session ``temp`` đã tạo: ``tmux a -t temp``
* Xóa session ``temp``: ``tmux kill-session -t temp``
* Đổi tên session từ temp -> temp1: ``tmux rename-session -t temp temp1``
* Xem các session đã tạo: ``tmux ls``

# 2. Window
* Tạo window mới: ``Ctrl+b c``
* Đổi tên window: ``Ctrl+b ,``
* Xem danh sách window: `Ctrl+b w``
* Chuyển đến window
	* Trước: ``Ctrl+b p``
	* Sau: ``Ctrl+b n``
	* Số 1: ``Ctrl+b 1``
* Xóa window: ``Ctrl+b &``

# 3. Panes
* Split panes
	* Theo chiều dọc: ``Ctrl+b %``
	* Theo chiều ngang: ``Ctrl+b "``
* Hiển thị số thứ tự của các panes: ``Ctrl+b q``
* Chuyển đến panes:
	* Tiếp theo (theo thứ tự tăng dần của số thứ tự pane): ``Ctrl+b o``
	* Số 1: ``Ctrl+b q 1``

* Hoán đổi vị trí 2 panes:
	* Pane hiện tại và pane phía trước: ``Ctrl+b {``
	* Pane hiện tại và pane phía sau: ``Ctrl+b }``
* Thay đổi kiểu layout của các panes: ``Ctrl+b space``
* Phóng to, thu nhỏ pane hiện tại toàn màn hình: ``Ctrl+b z``
* Thay đổi kích thước pane: ``Ctrl+b Ctrl+arrow``
* Xóa pane: ``Ctrl+b x``

# 4. Other