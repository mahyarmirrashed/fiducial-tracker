from argparse import ArgumentParser
from src.common import FileType, IntegerRangeType

DEFAULT_COLLECTOR_PORT = 5000

parser = ArgumentParser(description="Fiducial tracker client.")

parser.add_argument(
  "-p",
  "--port",
  type=IntegerRangeType(1024, 65536),
  default=DEFAULT_COLLECTOR_PORT,
  help="Port number for publishing captured video stream",
)

group = parser.add_mutually_exclusive_group(required=True)

group.add_argument(
  "-i",
  "--input",
  type=FileType(["mp4", "webm"]),
  help="Path to video file",
)
group.add_argument(
  "-c",
  "--camera",
  type=IntegerRangeType(lower=0),
  help="Camera to use (e.g. 0)",
)

args = parser.parse_args()

args.source = args.input if args.input is not None else args.camera
