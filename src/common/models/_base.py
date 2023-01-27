"""Defines a frozen model with extended JSON abilities."""


from orjson import dumps, loads
from pydantic import BaseModel


class _FrozenModel(BaseModel):
  """Frozen model configured with orjson extensions."""

  class Config:
    frozen = True
    json_loads = loads
    json_dumps = lambda v, *, default: dumps(v, default=default).decode()


class BaseMessage(_FrozenModel):
  """Base message."""

  pass
