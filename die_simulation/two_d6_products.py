from die_simulation import TwoDieProductSimulation

ds = TwoDieProductSimulation(6, 6, 1_000_000)
#ds.make_plotly()
ds.make_matplotlib()