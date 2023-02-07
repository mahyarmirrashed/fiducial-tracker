from pydantic import NonNegativeInt
from types import TracebackType
from typing import Union
from typing_extensions import Self

from src.common.models import VideoStreamRequestMessage

import datetime
import numpy as np
import ormsgpack
import qoi
import uuid
import zmq


class Commmunicator:
  def __init__(self, port: NonNegativeInt, uuid: uuid.UUID) -> None:
    """Communicator with fiducial tracker server."""
    self._port = port
    self._uuid = uuid

  def __enter__(self) -> Self:
    self._context = zmq.Context()
    self._socket = self._context.socket(zmq.PUB)
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
        VideoStreamRequestMessage(
          camera_id=self._uuid,
          encoded_frame=qoi.encode(frame),
          timestamp=datetime.datetime.now(),
          bottom_left_corner=None,
          top_right_corner=None,
        ).dict()
      )
    )
