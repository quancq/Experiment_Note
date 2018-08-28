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
 		
			```python
				plt.figure() # create a plot figure
				# create the first of two panels and set current axis
				plt.subplot(2, 1, 1) # (rows, columns, panel number)
				plt.plot(x, np.sin(x))
				# create the second panel and set current axis
				plt.subplot(2, 1, 2)
				plt.plot(x, np.cos(x));
			```
					
	* Object oriented interface
		* Giúp giải quyết tình huống phức tạp
		* Khi cần plot trên fig, ax nào thì chỉ cần gọi hàm plot từ đối tượng đó (với matlab interface thì ta phải chuyển fig đó sang active rồi gọi plt.plot())
			```python
				# First create a grid of plots
				# ax will be an array of two Axes objects
				fig, ax = plt.subplots(2)
				# Call plot() method on the appropriate object
				ax[0].plot(x, np.sin(x))
				ax[1].plot(x, np.cos(x));
			```

* Simple Line Plots
	* Gọi hàm ``plt.plot(x,y)``
	* Tùy chỉnh color, linestyle, legend, label, title, xlim,...
* Simple Scatter Plots
	* Dùng hàm ``plt.plot(x,y,fmt='o')``
* Scatter plots với plt.scatter
	* Phương thức này mạnh hơn plt.plot. Sự khác biệt là nó cho phép mỗi điểm dữ liệu có các thuộc tính (size, face color,...) khác nhau
	* Với data gồm hàng nghìn points thì plt.plot hiệu quả hơn hẳn so với plt.scatter. Lý do là vì plt.scatter phải làm thêm 1 số việc để có thể render size/ color cho mỗi điểm dữ liệu. Còn trong plt.plot thì hình ảnh của toàn bộ data chỉ phải tính toán 1 lần, sau đó clone cho các point khác
* Visualize error
	* ``plt.errorbar()``
	* ``plt.fill_between()``
* Contour Plots
	* Vẽ các đường đồng mức để visualize data 3 chiều trên mặt phẳng 2 chiều
	* Các hàm hỗ trợ:
		* ``plt.contour()``
		* ``plt.contourf()``
		* ``plt.imshow()``: biểu diễn mảng 2 chiều thành image
* Histogram Plots
	* ``plt.hist()``
	* ``plt.hist2d()``
	* ``plt.hexbin()``
* Customized Legend
	* 1 số tham số: loc, ncol, fancybox, shadow, frameon, framealpha
	* Có thể chọn ra những element nào cần hiển thị legend
	* Legend là sự giải thích cho các đối tượng trên plot, vì thế legend luôn tham chiếu đến đối tượng mà chúng giải thích. Khi cần vẽ thêm các legend mà đối tượng hiển thị ko tồn tại thì ta cần làm *giả* chúng bằng cách vẽ thêm 1 lớp rỗng (xem VD trong sách)
	* Để tạo nhiều legend cần dùng hàm ``ax.add_artist()``
* Custom Colorbars
* Multiple Subplots
	* ``plt.axes()``
	* ``plt.subplot()``
	* ``plt.subplots()``
	* ``plt.GridSpec()``
* Text and Annotation
	* ``plt.text()``
	* Sử dụng tham số transform (trong hàm plt.text()) để xác định tọa độ truyền vào được tính theo hệ tọa độ nào
		* ``ax.transData``: theo giá trị dữ liệu
		* ``ax.transAxes``: theo vùng diện tích của axes
		* ``fig.transFigure``: theo vùng diện tích của figure
	* ``plt.annotate()``: vẽ mũi tên và text chú thích
* Custom Ticks
	* Major và minor ticks
	* Tùy chỉnh location (locator) và label (formatter)
		


# Các hàm hay sử dụng

* ``plt.style.use('seaborn')``
* ``fig.savefig('fname.jpg')``
* ``fig = plt.figure(num=None, figsize=None, dpi=None,...)``: 
	* Tạo figure mới với ++id nếu num is None 
	* Tạo figure mới với id = num nếu tham số num được truyền vào và figure với id đó không tồn tại
	* Trả về figure với id = num nếu figure với id đó tồn tại
* ``ax = plt.axes(...)``: thêm 1 axes mới vào figure hiện tại và set axes này thành axes hiện tại
* ``ax = plt.subplot(nrows, ncols, index, **kwargs)``: Trong figure hiện tại, tạo và return 1 axes tại vị trí index trong lưới nrows * ncols
* ``fig, ax = plt.subplots(nrows=1, ncols=1,...)``: tạo figure mới
* ``plt.plot(x,y,color='green',linestyle='-')``: vẽ 1 line gồm các điểm (x[i],y[i])
* ``plt.axis()``: get/set axis. Có thể set x-y limit
* ``plt.title()``
* ``plt.xlabel()``
* ``plt.legend()``
* ``ax.set(title='',xlabel='',...)``
* ``plt.scatter(x,y,marker='o')``
* ``plt.errorbar(x, y, yerr=dy, fmt='o', color='black', ecolor='lightgray', elinewidth=3, capsize=0);``
* ``plt.fill_between(xfit, yfit - dyfit, yfit + dyfit, color='gray', alpha=0.2)``
* ``plt.contour(X, Y, Z, 20, cmap='RdGy')``
* ``plt.contourf(X, Y, Z, 20, cmap='RdGy')``
* ``plt.clabel(contours, inline=True, fontsize=8)``
* ``plt.imshow(Z, extent=[0, 5, 0, 5], origin='lower', cmap='RdGy', alpha=0.5)``
* ``plt.hist(data, bins=30, normed=True, alpha=0.5, histtype='stepfilled', color='steelblue', edgecolor='none');``
* ``ax.add_artist()``
* ``ax.text()``
* ``ax.annotate()``
* ``ax.xaxis.set_major_locator()``
* ``ax.yaxis.set_minor_formatter()``

# Reference
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) 
