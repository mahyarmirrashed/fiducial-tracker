"""Defines a frozen model with JSON encoder configurations."""

from pydantic import BaseModel, Extra


class FrozenModel(BaseModel):
  """Frozen model configured with orjson extensions."""

  class Config:
    extra = Extra.forbid
    frozen = True
