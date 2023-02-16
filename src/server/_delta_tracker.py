from time import time
from typing import Generator


def time_since_last_call() -> Generator[float, None, None]:
  last_call_time = time()

  while True:
    current_time = time()

    yield current_time - last_call_time

    last_call_time = current_time
