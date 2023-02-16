from ctypes import (
  _NamedFuncPointer,
  CDLL,
  c_char_p,
  c_float,
  c_int,
  c_void_p,
  pointer,
  POINTER,
)
from typing import Any, List, Tuple, Union

import os

from ._structures import (
  DetectionNumberPairStruct,
  DetectionStruct,
  ImageStruct,
  MetadataStruct,
)
from ._types import BoundingBox, Network, Prediction

DEFAULT_NAME_POSIX = "libdarknet.so"
DEFAULT_NAME_WINDOWS = "darknet.dll"


class Darknet:
  def __init__(self) -> None:
    if os.name == "posix":
      self._load(f"{os.path.dirname(__file__)}/{DEFAULT_NAME_POSIX}")
    elif os.name == "nt":
      os.environ["PATH"] = f"{os.path.dirname(__file__)};{os.environ['PATH']}"
      self._load(DEFAULT_NAME_WINDOWS)
    else:
      raise RuntimeError("Unsupported operating system")

    self._setup_bindings()

  def _get_detections_from_image(
    self,
    network: Network,
    image: ImageStruct,
    threshold: float = 0.5,
    hierarching_threshold: float = 0.5,
  ) -> Tuple[List[DetectionStruct], int]:
    _detection_count = pointer(c_int(0))
    detections: List[DetectionStruct] = self._lib.get_network_boxes(
      network.get(),
      image.w,
      image.h,
      threshold,
      hierarching_threshold,
      None,
      0,
      _detection_count,
      0,
    )
    detection_count: int = _detection_count[0]

    return detections, detection_count

  def _get_predictions_from_detections(
    self,
    detections: List[DetectionStruct],
    detection_count: int,
    class_names: List[str],
  ) -> List[Prediction]:
    valid_predictions: List[Prediction] = []

    for i in range(detection_count):
      for idx, class_name in enumerate(class_names):
        if detections[i].prob[idx] > 0:
          _bbox = detections[i].bbox
          _confidence = detections[i].prob[idx]
          valid_predictions.append(
            Prediction(
              class_name=str(class_name),
              confidence=round(_confidence * 100, 2),
              bounding_box=BoundingBox(x=_bbox.x, y=_bbox.y, w=_bbox.w, h=_bbox.h),
            )
          )

    return valid_predictions

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

  def get_predictions(
    self,
    network: Network,
    image: ImageStruct,
    threshold: float = 0.5,
    hierarching_threshold: float = 0.5,
    non_max_suppression: float = 0.45,
  ) -> List[Prediction]:
    detections, detection_count = self._get_detections_from_image(
      network, image, threshold, hierarching_threshold
    )

    if non_max_suppression > 0:
      self._lib.do_nms_sort(
        detections, detection_count, len(network.get_class_names()), non_max_suppression
      )

    predictions = self._get_predictions_from_detections(
      detections, detection_count, network.get_class_names()
    )

    self._lib.free_detections(detections, detection_count)

    return sorted(predictions, key=lambda prediction: prediction.confidence)

  def get_network_height(self, network: Network) -> int:
    return self._lib.network_height(network.get())

  def get_network_width(self, network: Network) -> int:
    return self._lib.network_width(network.get())

  def load(self, config_path: str, data_path: str, weights_path: str) -> Network:
    return Network(
      network=self._lib.load_network_custom(
        config_path.encode("ascii"), weights_path.encode("ascii"), 0, 1
      ),
      metadata=self._lib.load_meta(data_path.encode("ascii")),
    )
