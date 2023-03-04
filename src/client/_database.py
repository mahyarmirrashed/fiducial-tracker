from types import TracebackType
from typing import Any, Dict, Union

import decouple
import firebase_admin as fb
from firebase_admin import db
from typing_extensions import Self

from ._logger import logger


class DatabaseConnection:
  def __init__(self, certificate: Union[str, None]) -> None:
    self._certificate = certificate

    self._initialized = False
    self._ref: db.Reference

  def __enter__(self) -> Self:
    self._establish_connection()

    return self

  def __exit__(
    self,
    exc_type: Union[BaseException, None],
    exc_value: Union[BaseException, None],
    traceback: Union[TracebackType, None],
  ) -> None:
    if self._initialized:
      fb.delete_app(self._app)

  def _establish_connection(self) -> None:
    if self._certificate is not None:
      logger.debug("Initializing Firebase connection.")

      try:
        self._app = fb.initialize_app(
          fb.credentials.Certificate(self._certificate),
          {"databaseURL": decouple.config("FIREBASE_DATABASE_URL")},
        )
      except decouple.UndefinedValueError:
        logger.error("FIREBASE_DATABASE_URL environment variable not set.")
      except ValueError:
        logger.error("Invalid Firebase certificate file.")
      else:
        logger.debug("Initialized Firebase connection.")

        self._initialized = True
        self._ref = db.reference("/")

  def store(self, json: Dict[Any, Any]) -> None:
    if self._initialized:
      logger.debug("Storing data to Firebase RTDB.")

      self._ref.set(json)

      logger.debug("Completed storing data to Firebase RTDB.")
    else:
      logger.warn("Firebase connection not established. Cannot store information.")
