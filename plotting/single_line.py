import plotly.graph_objects as go

def plot_ts(x, y, title:str = "Time Series Plot"):
    """Plot time series given x axis data and y axis data"""
    
    fig = go.Figure([
        go.Scatter(x=x, y=y)
    ])

    fig.update_layout(title = title)
    fig.update_xaxes()
    fig.show()

def plot_generator(gen, *args, **kwargs):
    """Plot a timeseries generator (having a `generate` method that returns x and y data)"""
    x, y = gen.generate()
    plot_ts(x, y, *args, **kwargs)
