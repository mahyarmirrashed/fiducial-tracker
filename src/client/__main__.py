#!/home/mmirrashed/.conda/envs/tracker/bin/python
from ._args import args
from ._comms import Communicator
from ._database import DatabaseConnection
from ._logger import logger

try:
  with Communicator(args.location_stream_address) as comms:
    with DatabaseConnection(args.firebase_certificate) as conn:
      logger.info("Starting client.")

      while req := comms.recv():
        logger.debug(f"Received tracked fiducials: {req.fiducials}.")

        if args.firebase_certificate is not None:
          conn.store({fiducial.id: fiducial.to_dict() for fiducial in req.fiducials})
except KeyboardInterrupt:
  logger.info("Ending client.")
