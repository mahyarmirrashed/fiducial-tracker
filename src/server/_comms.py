from types import TracebackType
from typing import List, Optional, Union

import ormsgpack
import zmq
from typing_extensions import Self

from src.common.models import (
  Fiducial,
  LocationStreamMessage,
  SocketAddress,
  VideoStreamRequestMessage,
  VideoStreamResponseMessage,
)


class Communicator:
  def __init__(
    self,
    location_stream_address: SocketAddress,
    video_stream_address: SocketAddress,
  ) -> None:
    """Communicator with fiducial tracker cameras and clients."""
    self._location_stream_address = location_stream_address
    self._video_stream_address = video_stream_address

  def __enter__(self) -> Self:
    self._context = zmq.Context()
    self._location_stream_socket = self._context.socket(zmq.PUB)
    self._location_stream_socket.bind(f"tcp://*:{self._location_stream_address.port}")
    self._video_stream_socket = self._context.socket(zmq.REP)
    self._video_stream_socket.bind(f"tcp://*:{self._video_stream_address.port}")

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

  def recv_video_stream(self) -> Optional[VideoStreamRequestMessage]:
    if (msg := self._video_stream_socket.recv()) is not None:
      return VideoStreamRequestMessage.from_dict(ormsgpack.unpackb(msg))
    return None

  def send_location_stream(self, fiducials: List[Fiducial]) -> None:
    self._location_stream_socket.send(
      ormsgpack.packb(
        LocationStreamMessage(fiducials=fiducials).to_dict(),
      )
    )

  def send_video_stream(self, recommended_fps: Union[float, int]) -> None:
    self._video_stream_socket.send(
      ormsgpack.packb(
        VideoStreamResponseMessage(recommended_fps=float(recommended_fps)).to_dict(),
      )
    )
