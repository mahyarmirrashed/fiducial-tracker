import logging

from src.common import logger_factory

from ._args import args

logger = logger_factory("server")

if args.show_status:
  logger.setLevel(logging.CRITICAL)
