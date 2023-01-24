#!/home/mmirrashed/.conda/envs/tracker/bin/python
from argparse import ArgumentParser
from src.helpers import FileType, IntegerRangeType

import random
import time
import zmq

DEFAULT_COLLECTOR_PORT = 5000

parser = ArgumentParser(description="Fiducial tracker client.")

parser.add_argument(
  "-p",
  "--port",
  type=IntegerRangeType(1024, 65536),
  default=DEFAULT_COLLECTOR_PORT,
  help="Port number for publishing captured video stream",
)
parser.add_argument(
  "-i",
  "--input",
  type=FileType([".mp4", ".webm"]),
  required=True,
  help="Path to video file",
)

args = parser.parse_args()

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.connect(f"tcp://localhost:{args.port}")

while True:
  msg = {"captured": time.time(), "payload": "Ping!"}
  time.sleep(random.random())
  publisher.send_json(msg)
