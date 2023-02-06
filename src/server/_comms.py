from pydantic import NonNegativeInt
from types import TracebackType
from typing import Optional, Union
from typing_extensions import Self

from src.common.models import VideoStreamRequestMessage

import ormsgpack
import zmq


class Communicator:
  def __init__(
    self, collector_port: NonNegativeInt, publisher_port: NonNegativeInt
  ) -> None:
    """Communicator with fiducial tracker clients and receivers."""
    self._collector_port = collector_port
    self._publisher_port = publisher_port

  def __enter__(self) -> Self:
    self._context = zmq.Context()
    self._collector_socket = self._context.socket(zmq.SUB)
    self._collector_socket.bind(f"tcp://*:{self._collector_port}")
    self._collector_socket.setsockopt(zmq.SUBSCRIBE, b"")
    self._publisher_socket = self._context.socket(zmq.PUB)
    self._publisher_socket.bind(f"tcp://*:{self._publisher_port}")

    return self

  def __exit__(
    self,
    exc_type: Union[BaseException, None],
    exc_value: Union[BaseException, None],
    traceback: Union[TracebackType, None],
  ) -> None:
    self._collector_socket.close()
    self._publisher_socket.close()
    self._context.term()

  def receive(self) -> Optional[VideoStreamRequestMessage]:
    if (msg := self._collector_socket.recv()) is not None:
      return VideoStreamRequestMessage(**ormsgpack.unpackb(msg))
    return None
