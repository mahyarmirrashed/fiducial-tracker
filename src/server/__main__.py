#!/home/mmirrashed/.conda/envs/tracker/bin/python
from argparse import ArgumentParser
from src.helpers import IntegerRange

import random
import time
import zmq

DEFAULT_COLLECTOR_PORT = 5000
DEFAULT_PUBLISHER_PORT = 6000

parser = ArgumentParser(description="Fiducial tracking server.")

parser.add_argument(
  "--collector",
  type=IntegerRange(1024, 65536),
  default=DEFAULT_COLLECTOR_PORT,
  help="Port number for collecting video streams",
)
parser.add_argument(
  "--publisher",
  type=IntegerRange(1024, 65536),
  default=DEFAULT_PUBLISHER_PORT,
  help="Port number for publishing tracked fiducial locations",
)

args = parser.parse_args()

context = zmq.Context()
collector = context.socket(zmq.SUB)
collector.bind(f"tcp://*:{args.collector}")
publisher = context.socket(zmq.PUB)
publisher.bind(f"tcp://*:{args.publisher}")

while True:
  publisher.send_string("Ping!")
  time.sleep(random.random())
