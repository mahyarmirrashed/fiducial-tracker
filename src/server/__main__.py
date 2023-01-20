#!/home/mmirrashed/.conda/envs/tracker/bin/python
from argparse import ArgumentParser
from src.helpers import IntegerRange

import time
import zmq

ALLOWABLE_MESSAGE_DELAY = 0.5
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
collector.setsockopt(zmq.SUBSCRIBE, b"")
publisher = context.socket(zmq.PUB)
publisher.bind(f"tcp://*:{args.publisher}")


count_recvd = 0
count_dropped = 0

while True:
  msg = collector.recv_json()

  count_recvd += 1

  if isinstance(msg, dict):
    if time.time() - msg["captured"] <= ALLOWABLE_MESSAGE_DELAY:
      publisher.send_string(msg["payload"])
    else:
      count_dropped += 1
      print(f"Discarded payload... (% dropped: {100*(count_dropped/count_recvd):.1f})")
