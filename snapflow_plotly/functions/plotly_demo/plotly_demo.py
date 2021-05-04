from __future__ import annotations

import plotly.express as px
from snapflow import DataBlock, datafunction, Context


@datafunction(namespace="plotly")
def plotly_demo(
    ctx: Context,
) -> Records[PlotlyJson]:
    df = px.data.iris()
    fig = px.density_contour(
        df,
        x="sepal_width",
        y="sepal_length",
        color="species",
        marginal_x="rug",
        marginal_y="histogram",
    )
    return [fig.to_plotly_json()]
