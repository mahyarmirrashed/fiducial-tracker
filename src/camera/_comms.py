from types import TracebackType
from typing import List, Optional, Union
from typing_extensions import Self

from src.common.models import (
  Point,
  VideoStreamRequestMessage,
  VideoStreamResponseMessage,
)

import dataclasses
import datetime
import numpy as np
import ormsgpack
import qoi
import uuid
import zmq

_DEFAULT_TIMEOUT = 5_000  # milliseconds


class Commmunicator:
  def __init__(
    self,
    port: int,
    uuid: uuid.UUID,
    corners: List[Point],
  ) -> None:
    """Communicator with fiducial tracker server."""
    self._port = port
    self._uuid = uuid
    self._bottom_left_corner = corners[0]
    self._top_right_corner = corners[1]

  def __enter__(self) -> Self:
    self._context = zmq.Context()
    self._socket = self._context.socket(zmq.REQ)
    self._socket.setsockopt(zmq.REQ_RELAXED, True)
    self._socket.connect(f"tcp://localhost:{self._port}")

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
        dataclasses.asdict(
          VideoStreamRequestMessage(
            camera_id=self._uuid,
            frame_encoded=qoi.encode(frame),
            timestamp=datetime.datetime.now(),
            bottom_left_corner=self._bottom_left_corner,
            top_right_corner=self._top_right_corner,
          )
        )
      )
    )

  def recv(self) -> Optional[VideoStreamResponseMessage]:
    if self._socket.poll(_DEFAULT_TIMEOUT, zmq.POLLIN):
      return VideoStreamResponseMessage(**ormsgpack.unpackb(self._socket.recv()))
    return None
