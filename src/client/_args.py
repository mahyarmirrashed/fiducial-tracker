from argparse import ArgumentParser

from src.common import SocketAddressType
from src.common.models import SocketAddress

_DEFAULT_LOCATION_STREAM_ADDRESS = SocketAddress(host="localhost", port=6000)


_parser = ArgumentParser(description="Fiducial tracker client.")

_parser.add_argument(
  "--location-stream-address",
  type=SocketAddressType(),
  default=_DEFAULT_LOCATION_STREAM_ADDRESS,
  help="Socket address for collecting tracked fiducial locations",
)

args = _parser.parse_args()
