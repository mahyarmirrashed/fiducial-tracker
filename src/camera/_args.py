from argparse import ArgumentParser

from src.common import FileType, IntegerRangeType, PointType

_ALLOWABLE_VIDEO_TYPES = ["mp4", "webm"]
_DEFAULT_VIDEO_STREAM_PORT = 5000

_parser = ArgumentParser(description="Fiducial tracker camera.")

_parser.add_argument(
  "-p",
  "--port",
  type=IntegerRangeType(1024, 65536),
  default=_DEFAULT_VIDEO_STREAM_PORT,
  help="Port number for publishing captured video stream",
)

_group = _parser.add_mutually_exclusive_group(required=True)

_group.add_argument(
  "-i",
  "--input",
  type=FileType(_ALLOWABLE_VIDEO_TYPES),
  help=f"Path to video file (e.g. {_ALLOWABLE_VIDEO_TYPES})",
)
_group.add_argument(
  "-c",
  "--camera",
  type=IntegerRangeType(lower=0),
  help="Camera to use (e.g. 0)",
)

_parser.add_argument(
  "--corners",
  type=PointType(),
  nargs=2,
  help="Corners (top_left, bottom_right) in real world coordinates",
)

args = _parser.parse_args()

args.src = args.input if args.camera is None else args.camera

if args.input and args.corners is None:
  _parser.error("-i/--input requires --corners")
