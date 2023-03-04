from typing import Any, Dict

import decouple
import firebase_admin as fb
from firebase_admin import db

from ._args import args
from ._logger import logger


class _FirebaseConnection:
  def __init__(self) -> None:
    self._initialized = False
    self._ref: db.Reference

    self._establish_connection()

  def _establish_connection(self) -> None:
    if args.firebase_certificate is not None:
      logger.debug("Initializing Firebase connection.")

      try:
        fb.initialize_app(
          fb.credentials.Certificate(args.firebase_certificate),
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


conn = _FirebaseConnection()
