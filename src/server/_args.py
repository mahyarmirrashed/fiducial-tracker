from argparse import ArgumentParser

from src.common import FileType, IntegerRangeType

import os

_CURRENT_FILE_PATH = str(os.path.dirname(os.path.realpath(__file__)))

DEFAULT_VIDEO_STREAM_PORT = 5000
DEFAULT_LOCATION_STREAM_PORT = 6000

DEFAULT_CONFIG_PATH = f"{_CURRENT_FILE_PATH}/darknet/cfg/yolov4.cfg"
DEFAULT_DATA_PATH = f"{_CURRENT_FILE_PATH}/darknet/cfg/coco.data"
DEFAULT_WEIGHTS_PATH = f"{_CURRENT_FILE_PATH}/darknet/cfg/yolov4.weights"

parser = ArgumentParser(description="Fiducial tracking server.")

parser.add_argument(
  "--video-stream-port",
  type=IntegerRangeType(1024, 65536),
  default=DEFAULT_VIDEO_STREAM_PORT,
  help="Port number for collecting video streams",
)
parser.add_argument(
  "--location-stream-port",
  type=IntegerRangeType(1024, 65536),
  default=DEFAULT_LOCATION_STREAM_PORT,
  help="Port number for publishing tracked fiducial locations",
)
parser.add_argument(
  "--config",
  type=FileType("cfg"),
  default=DEFAULT_CONFIG_PATH,
  help="Darknet network configuration",
)
parser.add_argument(
  "--data",
  type=FileType("data"),
  default=DEFAULT_DATA_PATH,
  help="Darknet network data",
)
parser.add_argument(
  "--weights",
  type=FileType("weights"),
  default=DEFAULT_WEIGHTS_PATH,
  help="Darknet network weights",
)


args = parser.parse_args()
