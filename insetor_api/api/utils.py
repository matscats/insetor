from dataclasses import asdict, is_dataclass
from django.core.exceptions import ValidationError
import typing


def serialize_dataclass(val: typing.Any):
    if not is_dataclass(val) or isinstance(val, type):
        raise ValidationError(f"Not a dataclass, got type: {type(val)}")
    return {key: value for key, value in asdict(val).items() if value is not None}
