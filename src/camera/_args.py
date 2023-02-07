from argparse import ArgumentParser

from src.common import FileType, IntegerRangeType, PointType

ALLOWABLE_VIDEO_TYPES = ["mp4", "webm"]
DEFAULT_VIDEO_STREAM_PORT = 5000

parser = ArgumentParser(description="Fiducial tracker camera.")

parser.add_argument(
  "-p",
  "--port",
  type=IntegerRangeType(1024, 65536),
  default=DEFAULT_VIDEO_STREAM_PORT,
  help="Port number for publishing captured video stream",
)

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument(
  "-i",
  "--input",
  type=FileType(ALLOWABLE_VIDEO_TYPES),
  help=f"Path to video file (e.g. {ALLOWABLE_VIDEO_TYPES})",
)
group.add_argument(
  "-c",
  "--camera",
  type=IntegerRangeType(lower=0),
  help="Camera to use (e.g. 0)",
)

parser.add_argument(
  "--bottom-left-corner",
  type=PointType(),
  help="Bottom left corner in real world coordinates",
)
parser.add_argument(
  "--top-right-corner",
  type=PointType(),
  help="Top right corner in real world coordinates",
)

args = parser.parse_args()

args.source = args.input if args.input is not None else args.camera
args.missing_corners = args.bottom_left_corner is None or args.top_right_corner is None

if args.input and args.missing_corners:
  parser.error("-i/--input requires --bottom-left-corner and --top-right-corner")

if (args.bottom_left_corner is None) ^ (args.top_right_corner is None):
  parser.error("both of the arguments --bottom-left-corner and --top-right-corner are required")  # fmt: skip
