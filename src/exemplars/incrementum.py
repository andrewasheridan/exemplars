"""Incrementa Lib."""
__all__ = [
    "Incrementum",
    "IncrementumReadDTO",
    "IncrementumWriteDTO",
]

from dataclasses import dataclass

from litestar.dto import DataclassDTO, DTOConfig


@dataclass
class Incrementum:
    """Incrementum."""

    nomen: str
    """The name of the counter."""

    valorem: int = 1
    """The value that it holds."""


class IncrementumWriteDTO(DataclassDTO[Incrementum]):
    """Serializing outbound response data."""

    config = DTOConfig()
    """Config objects to define properties of the DTO."""


class IncrementumReadDTO(DataclassDTO[Incrementum]):
    """Serializing and validation of request data."""

    config = DTOConfig()
    """Config objects to define properties of the DTO."""
