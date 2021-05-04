from typing import TypeVar
from snapflow import SnapflowModule


# Schemas (for type hinting in python)
ExampleSchema = TypeVar("ExampleSchema")


module = SnapflowModule(
    "example",
    py_module_path=__file__,
    py_module_name=__name__,
    schemas=["schemas/schema.yml"],
    snaps=[Snap],
)
module.export()
