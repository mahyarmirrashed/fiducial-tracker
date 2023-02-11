from ctypes import c_float, Structure


class _BoxStruct(Structure):
  _fields_ = [
    ("x", c_float),
    ("y", c_float),
    ("w", c_float),
    ("h", c_float),
  ]
