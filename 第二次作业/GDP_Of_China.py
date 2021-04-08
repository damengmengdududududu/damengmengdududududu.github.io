from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map

# 2019年全国省份GDP
data ={
"广东":107671,
"山东":71067,
"河南":54259,
"四川":46615,
"江苏":99631,
"河北":35104,
"湖南":39752,
"安徽":37114,
"湖北":45828,
"浙江":62352,
"广西":21237,
"云南":23223,
"江西":24757,
"辽宁":24909,
"福建":42395,
"陕西":25793,
"黑龙江":13612,
"山西":17026,
"贵州":16769,
"重庆":23605,
"吉林":11726,
"甘肃":8718,
"内蒙古":17212,
"新疆":13597,
"上海":38155,
"北京":35371,
"天津":14104,
"海南":5308,
"宁夏":3748,
"青海":2965,
"西藏":1697,
}


map_data = list(data.items()) 

c = (
    Map()
    .add("2019年各省份GDP（单位：亿元）", 
         data_pair=map_data, 
         maptype="china",
         is_map_symbol_show=False, # 不描点             
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2019年全国31省市GDP数据分级设色图"),
        visualmap_opts=opts.VisualMapOpts(min_=1697, max_=107671, is_piecewise=True),
    )
)

c.render('./output/中国GDP数据地图.html')