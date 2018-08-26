Matplotlib
=======================

## Giới thiệu
* Library quan trọng trong data visualization python stack
* Cross-platform, nhiều tính năng
* Các lib mới dễ dùng, hiện đại (Seaborn, Bokeh,...) đều được build trên Matplotlib => Để có thể custom các bức hình theo ý muốn thì cần nắm được cú pháp, tính năng của matplotlib

## General Matplotlib Tips
* Import matplotlib theo *chuẩn*
	* ``import matplotlib as mpl``
	* ``import matplotlib.pyplot as plt``
* Setting styles
	* ``plt.style.use('classic')``
* Cách display plot: phụ thuộc vào *context* chạy đoạn code python
	* Plotting from a script
		* Gọi hàm **``plt.show()``**, hàm này thực hiện tìm kiếm các active figure và mở cửa sổ để hiển thị fig
 		* Chỉ *nên gọi hàm này 1 lần ở cuối script*. Khi gọi nhiều lần có thể gặp kết quả khó đoán trước
   	* Plotting from an IPython shell
    	* ``%matplotlib`` để bật chế độ làm việc với Mpl
    	* Không cần gọi hàm plt.show()
    	* Gọi hàm plot là hiển thị luôn figure
    	* Các lệnh sau đó có thể cập nhật được figure trước, nhưng sau khi thay đổi thì phải gọi hàm ``plt.draw()`` để update tường minh  
	* Plotting from an IPython notebook
    	* Cách plot gần giống với IPython
    	* Có 2 tùy chọn
	    	* ``%matplotlib notebook`` tạo ra interactive plot
	    	* ``%matplotlib inline`` tạo ra static image chứa plot
* Save figures to file
	* ``fig.savefig('my_figure.png')``
	* File format được suy ra từ extension của file name. Để tìm danh sách các kiểu file mà hệ thống hỗ trợ thì dùng: ``fig.canvas.get_supported_filetypes()``
* Maplotlib có 2 interface để sử dụng
	* Matlab-style interface
		* Interface này quen thuộc với Matlab user
		* Interface này là *stateful*: nghĩa là theo dõi current figure và axes để khi gọi plt.plot(...) thì sẽ plot trên fig và ax đó. Chính vì thế khi cần plot thêm vào fig đã tạo lúc trước thì cần code phức tạp mới plot được
	* s


=====================
# Các hàm hay sử dụng

* ``fig.savefig('fname.jpg')``
* ``fig = plt.figure(num=None, figsize=None, dpi=None,...)``: 
	* Tạo figure mới với ++id nếu num is None 
	* Tạo figure mới với id = num nếu tham số num được truyền vào và figure với id đó không tồn tại
	* Trả về figure với id = num nếu figure với id đó tồn tại
* ``plt.subplot()``
* ``plt.subplots()``