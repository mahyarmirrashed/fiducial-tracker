import os
from argparse import ArgumentTypeError
from typing import Any, List, Union


class FileType:
  def __init__(self, allowed_extensions: Union[List[str], str] = []) -> None:
    """Validates that a provided video file."""
    if not FileType._is_str(allowed_extensions):
      if not FileType._is_list_of_str(allowed_extensions):
        raise ValueError("Must be an array of strings")

    self._allowed_extensions = allowed_extensions

  def __call__(self, arg: Any) -> str:
    if not FileType._is_str(arg):
      raise ArgumentTypeError("Must be a string")
    elif arg.split(".")[-1] not in self._allowed_extensions:
      raise ArgumentTypeError(f"Must end with one of: {self._allowed_extensions}")
    elif not os.path.exists(arg):
      raise ArgumentTypeError("Must be valid path")
    elif not os.access(arg, os.R_OK):
      raise ArgumentTypeError(f'Missing read permissions for "{arg}"')
    return str(arg)

  @staticmethod
  def _is_str(value: Any) -> bool:
    return value is not None and isinstance(value, str)

  @staticmethod
  def _is_list_of_str(values: Any) -> bool:
    return (
      values is not None
      and isinstance(values, list)
      and all(FileType._is_str(value) for value in values)
    )
