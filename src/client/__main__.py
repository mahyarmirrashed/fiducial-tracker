#!/home/mmirrashed/.conda/envs/tracker/bin/python
from argparse import ArgumentParser
from src.helpers import IntegerRange

import random
import time
import zmq

DEFAULT_COLLECTOR_PORT = 5000

parser = ArgumentParser(description="Fiducial tracker client.")

parser.add_argument(
  "-p",
  "--port",
  type=IntegerRange(1024, 65536),
  default=DEFAULT_COLLECTOR_PORT,
  help="Port number for publishing captured video stream",
)

args = parser.parse_args()

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.connect(f"tcp://localhost:{args.port}")

while True:
  publisher.send_string("Ping!")
  time.sleep(random.random())
