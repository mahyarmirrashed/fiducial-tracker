"""Define base Pydantic models for NumPy's N-dimensional arrays (np.ndarray)."""

from __future__ import annotations

from pydantic.fields import ModelField
from typing import Any, Dict, Generic, Union

from ._types import ndarray, T

import abc
import numpy as np
import typing

if typing.TYPE_CHECKING:
  from pydantic.typing import CallableGenerator


class _BaseNDArray(abc.ABC):
  @classmethod
  def __get_validators__(cls) -> CallableGenerator:
    yield cls.validate

  @classmethod
  def __modify_schema__(
    cls, field_schema: Dict[str, Any], field: Union[ModelField, None]
  ) -> None:
    field_schema.update({"type": cls._field_type(field)})

  @staticmethod
  def _field_type(field: Union[ModelField, None]) -> str:
    if field and field.sub_fields:
      return f"np.ndarray[{field.sub_fields[0]}]"
    return "np.ndarray"

  @staticmethod
  def _validate(val: Any, field: ModelField) -> ndarray:
    if field.sub_fields:
      return np.asarray(val, dtype=field.sub_fields[0].type_)
    return np.asarray(val)

  @classmethod
  @abc.abstractmethod
  def validate(cls, val: Any, field: ModelField) -> ndarray:
    ...


class NDArray(Generic[T], ndarray, _BaseNDArray):
  @classmethod
  def validate(cls, val: Any, field: ModelField) -> ndarray:
    return super()._validate(val, field)
