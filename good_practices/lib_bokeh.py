from bokeh.charts import Scatter, output_file, show
from bokeh.sampledata.iris import flowers as data
from bokeh.models import HoverTool

hover = HoverTool(
        tooltips=[
            ('desc', '@species'),
        ]
    )

TOOLS = ['crosshair','wheel_zoom', 'box_zoom', 'resize', 'reset', hover]

scatter = Scatter(data, x='petal_length', y='petal_width',
                  color='species', marker='species',
                  title='Iris', legend=False, tools=TOOLS)

output_file("iris_simple.html", title="iris_simple.py example")

show(scatter)
