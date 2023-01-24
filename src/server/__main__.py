#!/home/mmirrashed/.conda/envs/tracker/bin/python
from ._args import args

import time
import zmq

ALLOWABLE_MESSAGE_DELAY = 0.5


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
