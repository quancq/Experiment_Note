Tensorflow Fundamentals
======================

# 1. Tensorflow Basic

* Cấu trúc chương trình gồm 2 phần
	* Định nghĩa đồ thị tính toán (construct computation graph)
	* Thực hiện tính toán (execution)

* Dynamic - Static shape
	* Static shape của 1 tensor được suy ra từ biểu thức khai báo (nhưng trong khai báo đó có thể có dimension có size = None, nghĩa là size đó chỉ được xác định chính xác tại thời điểm sess.run()). Cách tính Static shape: tensor.get_shape().as_list()
	* Dynamic shape của 1 tensor cho biết shape đầy đủ, đúng của tensor. Cách tính dynamic shape: tf.shape()

# Other (Tip, Tricks, Recipe,...)

* Gọi ``tf.reset_default_graph()`` ở đầu chương trình để xóa các node trong default graph, sau đó mới tạo node mới để tránh trùng lặp (chỉ khi dùng Jupyter notebook mới cần)

* Dùng ``tf.placeholder()``: để đẩy data vào khi run đồ thị

* ``tf.get_variable()``

# Popular function/code

* ``tf.stack()``
* ``tf.squeeze()``
* ``tf.nn.l2_loss()``
* ``tf.train.AdamOptimizer()``
* ``tf.global_variables_initializer()``
* ````
* ````


# References