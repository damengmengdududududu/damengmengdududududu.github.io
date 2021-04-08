from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.faker import Faker

v1 = [29255, 7431, 9394, 7514, 32049, 9804, 9642, 14297, 9617, 9091, 20363, 6575]
v2 = [1789, 1123, 1461, 1405, 1762, 1178, 1511, 1657, 1395, 1315, 1422, 931]
v3 = [50, 20, 13, 17, 10, 3, 6, 15, 43, 22, 7, 19]


bar = (
    Bar()
    .add_xaxis(Faker.months)
    .add_yaxis("明日方舟", v1)
    .add_yaxis("阴阳师", v2)
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} 万元"), interval=5
        )
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Overlap-bar+line"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} 名")),
    )
)

line = (
        Line()
        .add_xaxis(Faker.months)
        .add_yaxis("榜单差距", v3, yaxis_index=1)# 使用的 y 轴的 index，在单个图表实例中存在多个 y 轴的时候有用
)


bar = (
    Bar()
    .add_xaxis(Faker.months)
    .add_yaxis("明日方舟", v1)
    .add_yaxis("阴阳师", v2)
    .extend_axis(
        yaxis=opts.AxisOpts(
            axislabel_opts=opts.LabelOpts(formatter="{value} 名"), interval=5
        )
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2020明日方舟&阴阳师月流水及热度排名差"),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} 万元")),
    )
)

#line.overlap(bar)
#line.render()
bar.overlap(line)
bar.render("./output/明日方舟与阴阳师手游流水对比图.html")