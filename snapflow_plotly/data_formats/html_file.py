from __future__ import annotations

from typing import Any, Dict, List, Optional, TextIO, Type, TypeVar, cast

import dcp.storage.base as storage
from commonmodel import (
    FieldType,
    Schema,
)
from dcp.data_format.base import DataFormat, DataFormatBase
from dcp.data_format.handler import FormatHandler

HtmlFile = TypeVar("HtmlFile")


SAMPLE_SIZE_CHARACTERS = 1024 * 10


class HtmlFileFormat(DataFormatBase[HtmlFile]):
    natural_storage_class = storage.FileSystemStorageClass
    nickname = "html"


class HtmlFileHandler(FormatHandler):
    for_data_formats = [HtmlFileFormat]
    for_storage_classes = [storage.FileSystemStorageClass]
    delimiter = ","

    def infer_data_format(
        self, name: str, storage: storage.Storage
    ) -> Optional[DataFormat]:
        if name.endswith(".html"):
            return HtmlFileFormat
        # TODO: how hacky is this? very
        with storage.get_api().open(name) as f:
            s = f.read(SAMPLE_SIZE_CHARACTERS)
            if s.strip().lower().startswith("<html"):
                return HtmlFileFormat
        return None

    def infer_field_names(self, name, storage) -> List[str]:
        return []

    def infer_field_type(
        self, name: str, storage: storage.Storage, field: str
    ) -> FieldType:
        raise NotImplementedError

    def cast_to_field_type(
        self, name: str, storage: storage.Storage, field: str, field_type: FieldType
    ):
        # This is a no-op, files have no inherent data types
        pass

    def create_empty(self, name, storage, schema: Schema):
        # Not sure you'd really ever want to do this?
        with storage.get_api().open(name, "w") as f:
            pass
