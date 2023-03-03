import logging


class _ColoredFormatter(logging.Formatter):
  """Defines custom colored logging for logger."""

  _FORMAT = (
    "{}[{}]\x1b[39;49;1m %(asctime)s %(name)s %(module)s:%(lineno)d\x1b[0m %(message)s"
  )

  _FORMATS = {
    logging.DEBUG: _FORMAT.format("\x1b[30;47m", "DEBG"),
    logging.INFO: _FORMAT.format("\x1b[30;42m", "INFO"),
    logging.WARNING: _FORMAT.format("\x1b[30;43m", "WARN"),
    logging.ERROR: _FORMAT.format("\x1b[30;41m", "ERRO"),
    logging.CRITICAL: _FORMAT.format("\x1b[31;40;1m", "CRIT"),
  }

  def format(self, record: logging.LogRecord) -> str:
    """Format the incoming record according to our styles."""
    return logging.Formatter(
      fmt=self._FORMATS.get(record.levelno),
      datefmt="%H:%M:%S",
    ).format(record)


def logger_factory(name: str, level: int = logging.DEBUG) -> logging.Logger:
  logger = logging.getLogger(name)
  logger.setLevel(level)

  console_handler = logging.StreamHandler()
  console_handler.setLevel(level=level)
  console_handler.setFormatter(_ColoredFormatter())

  logger.addHandler(console_handler)

  return logger
