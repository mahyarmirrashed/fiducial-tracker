#!/home/mmirrashed/.conda/envs/tracker/bin/python
from src.common import display

from ._args import args
from ._comms import Communicator

import cv2
import qoi

try:
  with Communicator(args.location_stream_port, args.video_stream_port) as comms:
    while req := comms.receive():
      cv2.imshow("FRAME", qoi.decode(req.encoded_frame))

      if cv2.waitKey(1) & 0xFF == ord("q"):
        break
except KeyboardInterrupt:
  display("Server is exiting...")
