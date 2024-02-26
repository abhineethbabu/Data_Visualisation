import ctypes

# Load the shared library
my_lib = ctypes.CDLL('./mycppfunction.so')  # Adjust the path accordingly

# Specify the argument and result types of the function
my_lib.my_cpp_function.argtypes = (ctypes.c_int, ctypes.c_int)
my_lib.my_cpp_function.restype = ctypes.c_int

# Call the C++ function
result = my_lib.my_cpp_function(10, 20)
print("Result from C++ function:", result)
