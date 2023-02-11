from ctypes import _NamedFuncPointer, CDLL, c_char_p, c_float, c_int, c_void_p, POINTER
from typing import Any, Union

import os

from ._structures import (
  DetectionNumberPairStruct,
  DetectionStruct,
  ImageStruct,
  MetadataStruct,
)

DEFAULT_NAME_POSIX = "libdarknet.so"
DEFAULT_NAME_WINDOWS = "darknet.dll"


class Library:
  def __init__(self) -> None:
    if os.name == "posix":
      self._load(f"{os.path.dirname(__file__)}/{DEFAULT_NAME_POSIX}")
    elif os.name == "nt":
      os.environ["PATH"] = f"{os.path.dirname(__file__)};{os.environ['PATH']}"
      self._load(DEFAULT_NAME_WINDOWS)
    else:
      raise RuntimeError("Unsupported operating system")

    self._setup_bindings()

  def _load(self, path: str) -> None:
    self._lib = CDLL(path)

  def _setup_binding(
    self,
    funcptr: _NamedFuncPointer,
    argstype: Union[Any, None],
    restype: Union[Any, None],
  ) -> None:
    if argstype is not None:
      funcptr.argtypes = argstype
    if restype is not None:
      funcptr.restype = restype

  def _setup_bindings(self) -> None:
    self._setup_binding(self._lib.network_width, [c_void_p], c_int)  # fmt: skip
    self._setup_binding(self._lib.network_height, [c_void_p], c_int)  # fmt: skip
    self._setup_binding(self._lib.copy_image_from_bytes, [ImageStruct, c_char_p], None)
    self._setup_binding(self._lib.network_predict_ptr, [c_void_p, POINTER(c_float)], POINTER(c_float))  # fmt: skip
    self._setup_binding(self._lib.cuda_set_device, None, None)  # fmt: skip
    self._setup_binding(self._lib.init_cpu, None, None)  # fmt: skip
    self._setup_binding(self._lib.make_image, [c_int, c_int, c_int], ImageStruct)  # fmt: skip
    self._setup_binding(self._lib.get_network_boxes, [c_void_p, c_int, c_int, c_float, c_float, POINTER(c_int), c_int, POINTER(c_int), c_int], POINTER(DetectionStruct))  # fmt: skip
    self._setup_binding(self._lib.make_network_boxes, [c_void_p], POINTER(DetectionStruct))  # fmt: skip
    self._setup_binding(self._lib.free_detections, [POINTER(DetectionStruct), c_int], None)  # fmt: skip
    self._setup_binding(self._lib.free_batch_detections, [POINTER(DetectionNumberPairStruct), c_int], None)  # fmt: skip
    self._setup_binding(self._lib.free_ptrs, [POINTER(c_void_p), c_int], None)  # fmt: skip
    self._setup_binding(self._lib.network_predict_ptr, [c_void_p, POINTER(c_float)], None)  # fmt: skip
    self._setup_binding(self._lib.reset_rnn, [c_void_p], None)  # fmt: skip
    self._setup_binding(self._lib.load_network, [c_char_p, c_char_p, c_int], c_void_p)  # fmt: skip
    self._setup_binding(self._lib.load_network_custom, [c_char_p, c_char_p, c_int, c_int], c_void_p)  # fmt: skip
    self._setup_binding(self._lib.free_network_ptr, [c_void_p], c_void_p)  # fmt: skip
    self._setup_binding(self._lib.do_nms_obj, [POINTER(DetectionStruct), c_int, c_int, c_float], None)  # fmt: skip
    self._setup_binding(self._lib.do_nms_sort, [POINTER(DetectionStruct), c_int, c_int, c_float], None)  # fmt: skip
    self._setup_binding(self._lib.free_image, [ImageStruct], None)  # fmt: skip
    self._setup_binding(self._lib.letterbox_image, [ImageStruct, c_int, c_int], ImageStruct)  # fmt: skip
    self._setup_binding(self._lib.get_metadata, [c_char_p], MetadataStruct)  # fmt: skip
    self._setup_binding(self._lib.load_image_color, [c_char_p, c_int, c_int], ImageStruct)  # fmt: skip
    self._setup_binding(self._lib.rgbgr_image, [ImageStruct], None)  # fmt: skip
    self._setup_binding(self._lib.network_predict_image, [c_void_p, ImageStruct], POINTER(c_float))  # fmt: skip
    self._setup_binding(self._lib.network_predict_image_letterbox, [c_void_p, ImageStruct], POINTER(c_float))  # fmt: skip
    self._setup_binding(self._lib.network_predict_batch,[c_void_p, ImageStruct, c_int, c_int, c_int, c_float, c_float, POINTER(c_int), c_int, c_int], POINTER(DetectionNumberPairStruct))  # fmt: skip
