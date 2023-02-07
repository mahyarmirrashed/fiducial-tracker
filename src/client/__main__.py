#!/home/mmirrashed/.conda/envs/tracker/bin/python
from src.common import display

from ._args import args
from ._comms import Communicator

try:
  with Communicator(args.port) as comms:
    while req := comms.recv():
      display("\n".join(map(repr, req.fiducials)))
except KeyboardInterrupt:
  display("Client is exiting...")
