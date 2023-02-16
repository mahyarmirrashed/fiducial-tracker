from types import TracebackType
from typing import Optional, Union
from typing_extensions import Self

from src.common.models import LocationStreamMessage

import ormsgpack
import zmq


class Communicator:
  def __init__(self, port: int) -> None:
    """Communicator with fiducial tracker server."""
    self._port = port

  def __enter__(self) -> Self:
    self._context = zmq.Context()
    self._socket = self._context.socket(zmq.SUB)
    self._socket.connect(f"tcp://localhost:{self._port}")
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
      return LocationStreamMessage(**ormsgpack.unpackb(msg))
    return None
