"""Define property dimension types for NumPy arrays."""

from __future__ import annotations

from pydantic.fields import ModelField
from typing import Any, Dict
from typing_extensions import Self

from ._ndarray import NDArray

import numpy as np
import pydantic
import typing

if typing.TYPE_CHECKING:
  from pydantic.typing import CallableGenerator


class _BaseDType:
  @classmethod
  def __get_validators__(cls) -> CallableGenerator:
    yield cls.validate

  @classmethod
  def __modify_schema__(cls, field_schema: Dict[str, Any]) -> None:
    field_schema.update({"type": cls.__name__})

  @classmethod
  def validate(cls, val: Any, field: ModelField) -> Self:
    if field.sub_fields:
      raise pydantic.ValidationError(f"{cls.__name__} has no subfields", val)
    elif not isinstance(val, cls):
      return cls(val)  # type: ignore
    return val


class _longdouble(np.longdouble, _BaseDType):
  pass


class _double(np.double, _BaseDType):
  pass


class _single(np.single, _BaseDType):
  pass


class _half(np.half, _BaseDType):
  pass


class _int_(np.int_, _BaseDType):
  pass


class _intc(np.intc, _BaseDType):
  pass


class _short(np.short, _BaseDType):
  pass


class _byte(np.byte, _BaseDType):
  pass


class _uint(np.uint, _BaseDType):
  pass


class _uintc(np.uintc, _BaseDType):
  pass


class _ushort(np.ushort, _BaseDType):
  pass


class _ubyte(np.ubyte, _BaseDType):
  pass


class _clongdouble(np.clongdouble, _BaseDType):
  pass


class _cdouble(np.cdouble, _BaseDType):
  pass


class _csingle(np.csingle, _BaseDType):
  pass


_float128 = _longdouble
_float64 = _double
_float32 = _single
_float16 = _half

_int64 = _int_
_int32 = _intc
_int16 = _short
_int8 = _byte

_uint64 = _uint
_uint32 = _uintc
_uint16 = _ushort
_uint8 = _ubyte

_complex256 = _clongdouble
_complex128 = _cdouble
_complex64 = _csingle

NDArrayFp128 = NDArray[_float128]
NDArrayFp64 = NDArray[_float64]
NDArrayFp32 = NDArray[_float32]
NDArrayFp16 = NDArray[_float16]

NDArrayInt64 = NDArray[_int64]
NDArrayInt32 = NDArray[_int32]
NDArrayInt16 = NDArray[_int16]
NDArrayInt8 = NDArray[_int8]

NDArrayUint64 = NDArray[_uint64]
NDArrayUint32 = NDArray[_uint32]
NDArrayUint16 = NDArray[_uint16]
NDArrayUint8 = NDArray[_uint8]

NDArrayComplex256 = NDArray[_complex256]
NDArrayComplex128 = NDArray[_complex128]
NDArrayComplex64 = NDArray[_complex64]
