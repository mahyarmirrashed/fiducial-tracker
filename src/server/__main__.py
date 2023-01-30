#!/home/mmirrashed/.conda/envs/tracker/bin/python
from src.common import display

from ._args import args
from ._comms import Communicator

import cv2

try:
  with Communicator(args.collector, args.publisher) as comms:
    while req := comms.receive():
      print(req.frame.shape)
      cv2.imshow("FRAME", req.frame)

      if cv2.waitKey(1) & 0xFF == ord("q"):
        break
except KeyboardInterrupt:
  display("Server is exiting...")
