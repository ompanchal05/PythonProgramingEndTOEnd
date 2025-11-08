#WAP for the doing the  Tensorflow

# Import TensorFlow
import tensorflow as tf

# Print TensorFlow version
print("TensorFlow version:", tf.__version__)

# ------------------------------
# 1️⃣ Create Constant Tensors
# ------------------------------
a = tf.constant(5)
b = tf.constant(10)

# ------------------------------
# 2️⃣ Perform Basic Operations
# ------------------------------
add = tf.add(a, b)
sub = tf.subtract(a, b)
mul = tf.multiply(a, b)
div = tf.divide(a, b)

# ------------------------------
# 3️⃣ Print Results
# ------------------------------
print("Addition: ", add.numpy())
print("Subtraction: ", sub.numpy())
print("Multiplication: ", mul.numpy())
print("Division: ", div.numpy())

# ------------------------------
# 4️⃣ Matrix Operations
# ------------------------------
matrix1 = tf.constant([[1, 2], [3, 4]])
matrix2 = tf.constant([[5, 6], [7, 8]])

matrix_sum = tf.add(matrix1, matrix2)
matrix_product = tf.matmul(matrix1, matrix2)

print("\nMatrix 1:\n", matrix1.numpy())
print("Matrix 2:\n", matrix2.numpy())
print("Matrix Sum:\n", matrix_sum.numpy())
print("Matrix Product:\n", matrix_product.numpy())

# ------------------------------
# 5️⃣ Using Variables and Updating Values
# ------------------------------
x = tf.Variable(10)

print("\nBefore update:", x.numpy())

x.assign_add(5)
print("After adding 5:", x.numpy())

x.assign_sub(3)
print("After subtracting 3:", x.numpy())