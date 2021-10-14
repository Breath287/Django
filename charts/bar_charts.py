from pyecharts.charts import Bar
from pyecharts import options as opts

# draw a bar chart
bar = (
    Bar()
    .add_xaxis(['sweater', 'woolen', 'T-shirt', 'pants', 'heels', 'socks'])
    .add_yaxis('MerchantA', [5, 20, 26, 10, 75, 90])
    .add_yaxis('MerchantB', [15, 6, 45, 20, 35, 66])
    .set_global_opts(title_opts=opts.TitleOpts(title='Merchant', subtitle='Goods'))
)

# rendering in jupyter
bar.render_notebook()