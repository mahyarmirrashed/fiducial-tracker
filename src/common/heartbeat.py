import time


class Heartbeat:
  def __init__(self, interval: float) -> None:
    self._beat_interval = interval
    self._last_beat = time.time()

  def has_interval_passed(self) -> bool:
    current_time = time.time()

    if current_time - self._last_beat > self._beat_interval:
      self._last_beat = current_time
      return True
    return False
