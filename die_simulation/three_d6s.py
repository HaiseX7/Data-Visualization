from die_simulation import ThreeDieSimulation

ds = ThreeDieSimulation(6, 6, 6, 1_000_000)
ds.make_plotly()
ds.make_matplotlib()