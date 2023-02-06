#!/home/mmirrashed/.conda/envs/tracker/bin/python
from src.common import display

from ._args import args
from ._comms import Communicator

try:
  with Communicator(args.port) as comms:
    while req := comms.recv():
      pass
except KeyboardInterrupt:
  display("Receiver is exiting...")
