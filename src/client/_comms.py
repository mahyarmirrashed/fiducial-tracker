from types import TracebackType
from typing import Optional, Union

import ormsgpack
import zmq
from typing_extensions import Self

from src.common.models import LocationStreamMessage, SocketAddress


class Communicator:
  def __init__(self, address: SocketAddress) -> None:
    """Communicator with fiducial tracker server."""
    self._address = address

  def __enter__(self) -> Self:
    self._context = zmq.Context()
    self._socket = self._context.socket(zmq.SUB)
    self._socket.connect(f"tcp://{self._address}")
    self._socket.setsockopt(zmq.SUBSCRIBE, b"")

    return self

  def __exit__(
    self,
    exc_type: Union[BaseException, None],
    exc_value: Union[BaseException, None],
    traceback: Union[TracebackType, None],
  ) -> None:
    self._socket.close()
    self._context.term()

  def recv(self) -> Optional[LocationStreamMessage]:
    if (msg := self._socket.recv()) is not None:
      return LocationStreamMessage.from_dict(ormsgpack.unpackb(msg))
    return None
