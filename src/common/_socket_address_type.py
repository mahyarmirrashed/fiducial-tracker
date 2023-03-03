import socket
from argparse import ArgumentTypeError
from typing import Any

from src.common.models import SocketAddress


class SocketAddressType:
  def __call__(self, arg: Any) -> SocketAddress:
    try:
      host, port = arg.split(":")
      address = SocketAddress(host=host, port=int(port))
    except ValueError:
      raise ArgumentTypeError("Invalid socket address")

    if not SocketAddressType._within_port_range(address.port):
      raise ValueError("Port number must be in [0, 65536) range")

    try:
      socket.inet_aton(socket.gethostbyname(address.host))
    except socket.error:
      raise ArgumentTypeError("Invalid socket address")
    else:
      return address

  @staticmethod
  def _within_port_range(port: int) -> bool:
    return port in range(2**16)
