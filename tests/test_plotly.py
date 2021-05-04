from snapflow import graph, produce


def test_demo():
    from snapflow_plotly import module as sf_plotly

    g = graph()

    # Initial graph
    node1 = g.create_node(
        sf_plotly.functions.plotly_demo,
    )
    blocks = produce(node1, modules=[sf_plotly])
    output = blocks[0]
    records = output.as_records()
    assert len(records) == 1
    assert set(records[0].keys()) == set(["data", "layout"])


if __name__ == "__main__":
    test_demo()