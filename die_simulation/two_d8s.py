from die_simulation import TwoDieSimulation

ds = TwoDieSimulation(8, 8, 1_000_000)
ds.make_plotly()
ds.make_matplotlib()