from argparse import ArgumentParser
from src.common import IntegerRangeType

DEFAULT_COLLECTOR_PORT = 5000
DEFAULT_PUBLISHER_PORT = 6000

parser = ArgumentParser(description="Fiducial tracking server.")

parser.add_argument(
  "--collector",
  type=IntegerRangeType(1024, 65536),
  default=DEFAULT_COLLECTOR_PORT,
  help="Port number for collecting video streams",
)
parser.add_argument(
  "--publisher",
  type=IntegerRangeType(1024, 65536),
  default=DEFAULT_PUBLISHER_PORT,
  help="Port number for publishing tracked fiducial locations",
)

args = parser.parse_args()