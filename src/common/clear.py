import os


def clear() -> None:
  os.system("cls" if os.name == "nt" else "clear")


def display(msg: str) -> None:
  clear()
  print(msg)
