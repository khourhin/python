from bokeh.charts import Scatter, Bar, output_file, show
from bokeh.sampledata.iris import flowers as data
from bokeh.models import HoverTool
from collections import Counter

hover = HoverTool(
        tooltips=[
            ('desc', '@species'),
        ]
    )

TOOLS = ['crosshair','wheel_zoom', 'box_zoom', 'resize', 'reset', hover]


def scatter_plot():
    scatter = Scatter(data, x='petal_length', y='petal_width',
                      color='species', marker='species',
                      title='Iris', legend=False, tools=TOOLS)

    output_file("iris_simple.html", title="iris_simple.py example")

    show(scatter)


def bar_hist_plot():
    # Did not succeed to make histograms work with strings except like so:
    a = (Counter(data['species']))
    d = {
        'species': a.keys(),
        'counts': a.values()
    }
    hist_plot = Bar(d, label='species', legend=None)
    output_file('/tmp/serial_plotter_plot.html', title='Serial Plotter plot')
    show(hist_plot)

bar_hist_plot()
