"""Defines a frozen model with JSON encoder configurations."""

from orjson import dumps, loads
from pydantic import BaseModel, Extra


class FrozenModel(BaseModel):
  """Frozen model configured with orjson extensions."""

  class Config:
    extra = Extra.forbid
    frozen = True
    json_loads = loads
    json_dumps = lambda v, *, default: dumps(v, default=default).decode()
