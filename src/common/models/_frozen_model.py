"""Defines a frozen model with JSON encoder configurations."""

from orjson import dumps as _dumps, loads
from pydantic import BaseModel, Extra

import orjson


def dumps(v, *, default):
  return _dumps(v, default=default, option=orjson.OPT_SERIALIZE_NUMPY).decode()


class FrozenModel(BaseModel):
  """Frozen model configured with orjson extensions."""

  class Config:
    extra = Extra.forbid
    frozen = True
    json_loads = loads
    json_dumps = dumps
