from pydantic import NonNegativeInt
from types import TracebackType
from typing import Optional, Union
from typing_extensions import Self

from src.common.models import VideoStreamRequestMessage

import ormsgpack
import zmq


class Communicator:
  def __init__(
    self, location_stream_port: NonNegativeInt, video_stream_port: NonNegativeInt
  ) -> None:
    """Communicator with fiducial tracker clients and receivers."""
    self._location_stream_port = location_stream_port
    self._video_stream_port = video_stream_port

  def __enter__(self) -> Self:
    self._context = zmq.Context()
    self._location_stream_socket = self._context.socket(zmq.PUB)
    self._location_stream_socket.bind(f"tcp://*:{self._location_stream_port}")
    self._video_stream_socket = self._context.socket(zmq.SUB)
    self._video_stream_socket.bind(f"tcp://*:{self._video_stream_port}")
    self._video_stream_socket.setsockopt(zmq.SUBSCRIBE, b"")

    return self

  def __exit__(
    self,
    exc_type: Union[BaseException, None],
    exc_value: Union[BaseException, None],
    traceback: Union[TracebackType, None],
  ) -> None:
    self._location_stream_socket.close()
    self._video_stream_socket.close()
    self._context.term()

  def receive(self) -> Optional[VideoStreamRequestMessage]:
    if (msg := self._video_stream_socket.recv()) is not None:
      return VideoStreamRequestMessage(**ormsgpack.unpackb(msg))
    return None
