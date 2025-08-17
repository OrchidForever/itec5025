import tensorflow as tf	
import numpy as np

# Basic TensorFlow Hello World
print ("TensorFlow version:", tf.__version__)

#print("Hello, Chatbot!")

# Create a constant tensor
hello = tf.constant('Hello, Chatbot!')

print(hello.numpy().decode('utf-8'))  # Use .numpy() to get the value

print("Session ended.")