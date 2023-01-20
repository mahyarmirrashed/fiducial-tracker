#!/home/mmirrashed/.conda/envs/tracker/bin/python
from argparse import ArgumentParser
from src.helpers import IntegerRange

import time
import zmq

DEFAULT_PUBLISHER_PORT = 5000

parser = ArgumentParser(description="Fiducial tracker receiver.")

parser.add_argument(
  "-p",
  "--port",
  type=IntegerRange(1024, 65536),
  default=DEFAULT_PUBLISHER_PORT,
  help="Port number for collecting tracked fiducial locations from server",
)

args = parser.parse_args()

context = zmq.Context()
subscriber = context.socket(zmq.SUB)
subscriber.connect(f"tcp://localhost:{args.port}")
subscriber.setsockopt(zmq.SUBSCRIBE, b"")

count = 0
avg = 0

while True:
  start = time.time()
  res = subscriber.recv_string()
  end = time.time()
  avg *= count
  avg += (end - start)
  count += 1
  avg /= count
  print(f"{res}, avg res time: {avg:.3f}")