Tensorflow Fundamentals
======================

# 1. Tensorflow Basic

* Cấu trúc chương trình gồm 2 phần
	* Định nghĩa đồ thị tính toán (construct computation graph)
	* Thực hiện tính toán (execution)

* Dynamic - Static shape
	* Static shape của 1 tensor được suy ra từ biểu thức khai báo trong pha graph construction (nhưng trong khai báo đó có thể có dimension có size = None, nghĩa là size đó chỉ được xác định chính xác tại thời điểm sess.run()). 
		* Cách tính static shape: tensor.get_shape().as_list()
		* Cách set static shape: tensor.set_shape([d1, d2])
	* Dynamic shape của 1 tensor cho biết shape đầy đủ, đúng của tensor. 
		* Cách tính dynamic shape: tf.shape(). Hàm này trả về 1 tensor biểu diễn shape, ta phải eval nó trong session để lấy về shape
		* Cách reshape: a = tf.reshape(a, [d1, d2])

* Name scope và variable scope
	* Mỗi node trong graph đều có tên (a.name). Khi tạo các node mà không chỉ định tên thì TF sẽ thiết lập tên mặc định. Để quản lý các node theo tên, TF đưa ra 2 context manager
	* Name scope: ``tf.name_scope("scope")``
		* Các biến tạo trong scope này sẽ có tên có prefix là "scope". Mục đích quản lý theo cây phân cấp để sau này khi visualize graph trên tensorboard sẽ dễ nhìn (các node cùng name scope sẽ được quy chung về 1 cụm, khi cần show kĩ cụm nào thì có thể expand ra)
		* Chú ý: các biến tạo bởi tf.get_varibale() không có prefix name là tên scope (không bị ảnh hưởng bởi tf.name_scope())
	* Variable scope: ``tf.variable_scope("scope")``
		* Khá giống name scope trong việc tạo ra prefix name cho các biến khai báo bên trong scope. Khác biệt nằm ở chỗ, variable scope tạo luôn prefix name cho các biến tạo bởi tf.get_variable()
	* Sử dụng theo mục đích
		* Mục đích của name scope để quản lý theo tên cụm (dễ nhìn khi dùng tensorboard)
			* Nếu chỉ tạo các biến (không cần tái sử dụng) và cần quản lý theo tên phân cấp thì dùng
				* ``tf.Variable`` để tạo biến
				* ``tf.name_scope()`` để tạo scope
		* Mục đích của variable scope để tạo khả năng chia sẻ các biến (tái sử dụng các biến tại một nơi bất kì trong chương trình)
			* Nếu cần tạo các biến có thể chia sẻ, tái sử dụng thì dùng
				* ``tf.get_variable()`` để tạo biến
				* ``tf.variable_scope()`` để tạo scope
	* Một số lưu ý khi dùng tf.variable_scope() và tf.get_variable()
		* tf.get_variable() có thể tạo biến mới, hoặc có thể tái sử dụng biến cũ (đã *tạo bởi tf.get_variable()*)
		* Để thiết lập cho phép tái sử dụng, có 2 cách
			* ``tf.variable_scope("scope", reuse=True)``. Mặc định reuse=False
			* ```
			with tf.variable_scope("scope") as scope:
			scope.reuse_variables()
			```
		* Nếu set **reuse=True** và gọi tf.get_variable() mà biến đó **chưa được tạo** bởi tf.get_variable() thì sinh ra error
		* Nếu set **reuse=False** và gọi tf.get_variable() mà biến đó **đã được tạo** bởi tf.get_variable() thì sinh ra error
		* Nếu set **reuse=tf.AUTO_REUSE** thì TF sẽ tạo biến mới nếu biến chưa tồn tại và tái sử dụng nếu biến đó đã được tạo
		* Với tf.AUTO_REUSE rất tiện lợi, nhưng nếu lạm dụng thì ta không thể kiểm soát được việc một biến không cần chia sẻ lại bị chia sẻ. Khi đó ta có thể dùng tf.make_template
			* ```
			conv3x32 = tf.make_template("conv3x32", lambda x: tf.layers.conv2d(x, 32, 3))
			features1 = conv3x32(image1)
			features2 = conv3x32(image2)  # Will reuse the convolution weights
			```
				
* Argument scope
	* Giúp code ngắn gọn hơn trong trường hợp khi gọi 1 hàm nhiều lần với nhiều bộ tham số trùng nhau
	* Ví dụ minh họa
		```
		with tf.contrib.framework.arg_scope(
		[fully_connected],
		normalizer_fn=batch_norm,
		normalizer_params=bn_params,
		activation_fn=tf.nn.elu):
			hidden1 = fully_connected(X, n_hidden1, scope="hidden1")
			hidden2 = fully_connected(hidden1, n_hidden2, scope="hidden2")
			logits = fully_connected(hidden2, n_outputs, scope="outputs", activation_fn=None)
		```

* Truyền data vào chương trình
	* Place holder
	* Dataset API

* Thứ tự thực hiện và điều khiển sự phụ thuộc

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
* ``tf.cond()``
* ``tf.py_func()``
* ``Dataset API``
* ``tf.control_dependencies()``
* ````
* ````
* ````
* ````


# References