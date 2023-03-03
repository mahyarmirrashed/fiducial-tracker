import typing
from dataclasses import asdict as _to_dict
from dataclasses import fields, is_dataclass
from typing import Any, Dict, Mapping, Type, TypeVar

T = TypeVar("T", bound="DictMixin")
U = TypeVar("U")


def _from_dict(cls: Type[U], src: Mapping[str, Any]) -> U:
  field_types_lookup = {field.name: field.type for field in fields(cls)}

  constructor_inputs = {}

  for field_name, value in src.items():
    try:
      if isinstance(value, list):
        list_type = typing.get_args(field_types_lookup[field_name])[0]
        constructor_inputs[field_name] = [_from_dict(list_type, item) for item in value]
      else:
        field_type = field_types_lookup[field_name]
        constructor_inputs[field_name] = _from_dict(field_type, value)
    except TypeError:
      # breaking recursion if not a dataclass
      constructor_inputs[field_name] = value
    except KeyError:
      # field not defined on dataclass, pass as plain field value
      constructor_inputs[field_name] = value

  return cls(**constructor_inputs)


class DictMixin:
  @classmethod
  def from_dict(cls: Type[T], src: Mapping[str, Any]) -> T:
    return _from_dict(cls, src)

  def to_dict(self) -> Dict[str, Any]:
    if is_dataclass(self):
      return _to_dict(self)
    return dict()
