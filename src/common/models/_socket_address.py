from dataclasses import dataclass


@dataclass(frozen=True)
class SocketAddress:
  host: str
  port: int

  def __repr__(self) -> str:
    return f"{self.host}:{self.port}"

  def __str__(self) -> str:
    return repr(self)
