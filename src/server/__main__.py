#!/home/mmirrashed/.conda/envs/tracker/bin/python
from argparse import ArgumentParser
from src.helpers import IntegerRange

import random
import time
import zmq

DEFAULT_SERVER_PORT = 5000

# python -m src.server -p PORT
parser = ArgumentParser(description="Fiducial tracker server.")

parser.add_argument(
  "-p",
  "--port",
  type=IntegerRange(1024, 65536),
  default=DEFAULT_SERVER_PORT,
  help="Server port number",
)

args = parser.parse_args()

context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.bind(f"tcp://*:{args.port}")

while True:
  publisher.send_string("Ping!")
  time.sleep(random.random())
