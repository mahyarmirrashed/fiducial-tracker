from argparse import ArgumentParser

from src.common import FloatRangeType, IntegerRangeType

_DEFAULT_VIDEO_STREAM_PORT = 5000
_DEFAULT_LOCATION_STREAM_PORT = 6000
_DEFAULT_PUBLISH_FREQUENCY = 1.0

_parser = ArgumentParser(description="Fiducial tracking server.")

_parser.add_argument(
  "--video-stream-port",
  type=IntegerRangeType(1024, 65536),
  default=_DEFAULT_VIDEO_STREAM_PORT,
  help="Port number for collecting video streams",
)
_parser.add_argument(
  "--location-stream-port",
  type=IntegerRangeType(1024, 65536),
  default=_DEFAULT_LOCATION_STREAM_PORT,
  help="Port number for publishing tracked fiducial locations",
)
_parser.add_argument(
  "--frequency",
  type=FloatRangeType(lower=0.01),
  default=_DEFAULT_PUBLISH_FREQUENCY,
  help="Frequency to publish tracked fiducial locations",
)
_parser.add_argument(
  "--display-raw-frames",
  action="store_true",
  help="Show raw frames from video streams",
)
_parser.add_argument(
  "--display-processed-frames",
  action="store_true",
  help="Show processed frames from video streams with bounding boxes",
)
_parser.add_argument(
  "--save-raw-frames",
  action="store_true",
  help="Stored the raw frames from video streams",
)
_parser.add_argument(
  "--save-processed-frames",
  action="store_true",
  help="Store the processed frames from video streams with bounding boxes",
)


args = _parser.parse_args()
