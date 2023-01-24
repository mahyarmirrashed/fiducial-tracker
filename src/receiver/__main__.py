#!/home/mmirrashed/.conda/envs/tracker/bin/python
from ._args import args

import time
import zmq


context = zmq.Context()
receiver = context.socket(zmq.SUB)
receiver.connect(f"tcp://localhost:{args.port}")
receiver.setsockopt(zmq.SUBSCRIBE, b"")

count = 0
avg = 0

while True:
  start = time.time()
  res = receiver.recv_string()
  end = time.time()
  avg *= count
  avg += end - start
  count += 1
  avg /= count
  print(f"{res}, avg res time: {avg:.3f}")
