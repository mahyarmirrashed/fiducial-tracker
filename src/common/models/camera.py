"""Defines a camera source model."""

import uuid
from dataclasses import dataclass, field
from typing import Union


@dataclass
class Camera:
  src: Union[int, str]
  id: uuid.UUID = field(default_factory=uuid.uuid4, init=False, repr=False)
