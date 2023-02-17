from argparse import ArgumentParser

from src.common import IntegerRangeType

DEFAULT_VIDEO_STREAM_PORT = 5000
DEFAULT_LOCATION_STREAM_PORT = 6000

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
  "--display-raw-frames",
  action="store_true",
  help="Show raw frames from video streams",
)
parser.add_argument(
  "--display-processed-frames",
  action="store_true",
  help="Show processed frames from video streams with bounding boxes",
)
parser.add_argument(
  "--save-raw-frames",
  action="store_true",
  help="Stored the raw frames from video streams",
)
parser.add_argument(
  "--save-processed-frames",
  action="store_true",
  help="Store the processed frames from video streams with bounding boxes",
)


args = parser.parse_args()
