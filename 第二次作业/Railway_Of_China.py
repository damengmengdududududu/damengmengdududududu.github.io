
from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType


c = (
    Geo()
    .add_schema(
            maptype="china",
            itemstyle_opts=opts.ItemStyleOpts(color="grey", border_color="black"),)
    .add(
        "",
        [("通辽", 10), ("北京", 60), ("满洲里", 10), ("哈尔滨", 50), ("绥芬河", 10)],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "",
        [("长春", 10), ("沈阳", 50), ("大连", 50), ("天津", 50), ("济南", 50), ("连云港", 10),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "",
        [("徐州", 10), ("南京", 50), ("上海", 60), ("合肥", 50), ("杭州", 50), ("南昌", 50),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "",
        [("福州", 50), ("厦门", 50), ("石家庄", 50), ("郑州", 50), ("武汉", 50), ("长沙", 50),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "",
        [("株洲", 10), ("广州", 50), ("香港", 50), ("呼和浩特", 50), ("柳州", 10), ("南宁", 50),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "",
        [("湛江", 10), ("包头", 10), ("银川", 50), ("兰州", 50), ("太原", 50), ("宝鸡", 10),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "",
        [("西安", 50), ("成都", 50), ("重庆", 50), ("贵阳", 50), ("昆明", 50), ("大理", 10),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "",
        [("西宁", 50), ("格尔木", 10), ("拉萨", 50), ("乌鲁木齐", 50), ("库尔勒", 10), ("喀什", 10),],
         #城市标记参数是由元组项组成的列表
        type_=ChartType.SCATTER,
        color="white",
    )
    .add(
        "京广线",
        [("北京", "石家庄"), ("石家庄", "郑州"), ("郑州", "武汉"),
         ("武汉", "长沙"), ("长沙", "株洲"), ("株洲", "广州")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "京九线",
        [("北京", "南昌"), ("南昌", "香港")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "陇海线",
        [("连云港", "徐州"), ("徐州", "郑州"), ("郑州", "西安"),
         ("西安", "宝鸡"), ("宝鸡", "兰州")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "兰新线",
        [("兰州", "乌鲁木齐"),("乌鲁木齐", "库尔勒"),("库尔勒", "喀什")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "滨绥线",
        [("哈尔滨", "绥芬河")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "滨州线",
        [("哈尔滨", "满洲里")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
     .add(
        "沪杭线",
        [("上海", "杭州")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "湘黔线",
        [("长沙", "贵阳")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
     .add(
        "成昆线",
        [("成都", "昆明"),("成都", "重庆")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "青藏线",
        [("西宁", "格尔木"),("格尔木", "拉萨")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "贵昆线",
        [("贵阳", "昆明"),("昆明", "大理")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
     .add(
        "浙赣线",
        [("杭州", "南昌"),("南昌", "株洲"),("南昌", "福州"),("南昌", "厦门")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "京包线",
        [("北京", "呼和浩特"),("呼和浩特", "包头")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "宝成线",
        [("宝鸡", "西安"),("宝鸡", "成都")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "包兰线",
        [("包头", "银川"),("银川", "兰州")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "京哈线",
        [("北京", "通辽"), ("通辽", "长春"), ("长春", "哈尔滨")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "哈大线",
        [("哈尔滨", "长春"), ("长春", "沈阳"), ("沈阳", "大连")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "京沪线",
        [("北京", "天津"), ("天津", "济南"), ("济南", "徐州"), ("徐州", "南京"), ("南京", "上海"), ("南京", "合肥")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .add(
        "焦柳线",
        [("呼和浩特", "太原"), ("太原", "柳州"), ("柳州", "南宁"), ("柳州", "湛江")],
         #连线方向参数是由元组项组成的列表
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="yellow"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.1),
        # curve为正时，曲线是凸的；为负时，曲线是凹的
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="中国铁路路线图"))
    
    .render('./output/中国铁路路线图.html')
)

