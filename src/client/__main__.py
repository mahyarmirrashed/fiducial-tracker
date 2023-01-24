#!/home/mmirrashed/.conda/envs/tracker/bin/python
from ._args import args

import random
import time
import zmq


context = zmq.Context()
publisher = context.socket(zmq.PUB)
publisher.connect(f"tcp://localhost:{args.port}")

while True:
  msg = {"captured": time.time(), "payload": "Ping!"}
  time.sleep(random.random())
  publisher.send_json(msg)
