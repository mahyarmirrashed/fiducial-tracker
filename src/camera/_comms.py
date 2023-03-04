import datetime
import uuid
from types import TracebackType
from typing import List, Optional, Union

import numpy as np
import ormsgpack
import zmq
from typing_extensions import Self

from src.common.models import (
  Point,
  SocketAddress,
  VideoStreamRequestMessage,
  VideoStreamResponseMessage,
)

_DEFAULT_TIMEOUT = 5_000  # milliseconds


class Commmunicator:
  def __init__(
    self,
    address: SocketAddress,
    uuid: uuid.UUID,
    corners: List[Point],
  ) -> None:
    """Communicator with fiducial tracker server."""
    self._address = address
    self._uuid = uuid
    self._top_left_corner = corners[0]
    self._bottom_right_corner = corners[1]

  def __enter__(self) -> Self:
    self._context = zmq.Context()
    self._socket = self._context.socket(zmq.REQ)
    self._socket.setsockopt(zmq.REQ_RELAXED, True)
    self._socket.setsockopt(zmq.LINGER, False)
    self._socket.connect(f"tcp://{self._address}")

    return self

  def __exit__(
    self,
    exc_type: Union[BaseException, None],
    exc_value: Union[BaseException, None],
    traceback: Union[TracebackType, None],
  ) -> None:
    self._socket.close()
    self._context.term()

  def send(self, frame: np.ndarray) -> None:
    self._socket.send(
      ormsgpack.packb(
        VideoStreamRequestMessage(
          camera_id=self._uuid,
          frame=frame.tobytes(),
          shape=frame.shape,
          timestamp=datetime.datetime.now(),
          top_left_corner=self._top_left_corner,
          bottom_right_corner=self._bottom_right_corner,
        ).to_dict()
      )
    )

  def recv(self) -> Optional[VideoStreamResponseMessage]:
    if self._socket.poll(_DEFAULT_TIMEOUT, zmq.POLLIN):
      return VideoStreamResponseMessage.from_dict(
        ormsgpack.unpackb(self._socket.recv())
      )
    return None
