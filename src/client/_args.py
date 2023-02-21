from argparse import ArgumentParser

from src.common import IntegerRangeType

_DEFAULT_LOCATION_STREAM_PORT = 6000


parser = ArgumentParser(description="Fiducial tracker client.")

parser.add_argument(
  "-p",
  "--port",
  type=IntegerRangeType(1024, 65536),
  default=_DEFAULT_LOCATION_STREAM_PORT,
  help="Port number for collecting tracked fiducial locations",
)

args = parser.parse_args()
