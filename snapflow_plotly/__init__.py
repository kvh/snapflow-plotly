from typing import TypeVar
from snapflow import SnapflowModule

# from .data_formats.html_file import HtmlFile, HtmlFileFormat, HtmlFileHandler

PlotlyJson = TypeVar("PlotlyJson")

module = SnapflowModule(
    "plotly",
    py_module_path=__file__,
    py_module_name=__name__,
)
