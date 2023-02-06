from argparse import ArgumentParser

from src.common import FileType, IntegerRangeType

ALLOWABLE_VIDEO_TYPES = ['mp4', 'webm']
DEFAULT_VIDEO_STREAM_PORT = 5000

parser = ArgumentParser(description="Fiducial tracker client.")

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

args = parser.parse_args()

args.source = args.input if args.input is not None else args.camera
