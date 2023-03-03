from argparse import ArgumentParser

from src.common import IntegerRangeType

_DEFAULT_LOCATION_STREAM_PORT = 6000


_parser = ArgumentParser(description="Fiducial tracker client.")

_parser.add_argument(
  "--port",
  type=IntegerRangeType(1024, 65536),
  default=_DEFAULT_LOCATION_STREAM_PORT,
  help="Port number for collecting tracked fiducial locations",
)

args = _parser.parse_args()
