#!/home/mmirrashed/.conda/envs/tracker/bin/python
from ._args import args
from ._comms import Communicator
from ._logger import logger

try:
  with Communicator(args.port) as comms:
    logger.info("Starting client.")

    while req := comms.recv():
      logger.debug(f"Received tracked fiducials: {req.fiducials}.")
except KeyboardInterrupt:
  logger.info("Ending client.")
