import ctypes

lib = ctypes.CDLL("/home/fercuellar/Desktop/Robotica/catkin_ws/src/midterm/Scripts/libreria/libmy_library.so")

x = ctypes.c_float(1)
y = ctypes.c_float(2)
z = ctypes.c_float(3)


lib.multiply_coords(ctypes.pointer(x),ctypes.pointer(y),ctypes.pointer(z))

print(z.value)