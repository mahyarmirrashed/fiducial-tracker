from ctypes import c_char_p, c_float, c_int, POINTER, Structure


class _BoxStruct(Structure):
  _fields_ = [
    ("x", c_float),
    ("y", c_float),
    ("w", c_float),
    ("h", c_float),
  ]


class DetectionStruct(Structure):
  _fields_ = [
    ("bbox", _BoxStruct),
    ("classes", c_int),
    ("best_class_idx", c_int),
    ("prob", POINTER(c_float)),
    ("mask", POINTER(c_float)),
    ("objectness", c_float),
    ("sort_class", c_int),
    ("uc", POINTER(c_float)),
    ("points", c_int),
    ("embeddings", POINTER(c_float)),
    ("embedding_size", c_int),
    ("sim", c_float),
    ("track_id", c_int),
  ]


class DetectionNumberPairStruct(Structure):
  _fields_ = [
    ("num", c_int),
    ("dets", POINTER(DetectionStruct)),
  ]


class ImageStruct(Structure):
  _fields_ = [
    ("w", c_int),
    ("h", c_int),
    ("c", c_int),
    ("data", POINTER(c_float)),
  ]


class MetadataStruct(Structure):
  _fields_ = [
    ("classes", c_int),
    ("names", POINTER(c_char_p)),
  ]
