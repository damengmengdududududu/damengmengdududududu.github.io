import matplotlib
import matplotlib.pyplot as plt



# 指定所用中文的字体
import os
if os.name == "nt": # Windows系统
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体
else: # MacOS系统
    plt.rcParams["font.family"] = 'Arial Unicode MS'  
plt.rcParams['axes.unicode_minus'] = False  # 支持负号的正常显示



src_filename = './data/output.csv'

src_file = open(src_filename, 'r')
line_list = src_file.readlines()
src_file.close()

word_list = []
cnt_list = []

del line_list[0] #删除csv文件中的标题行

for line in line_list:
    line = line.replace('\n', '')
    word_cnt = line.split(',')
    word_list.append(word_cnt[0])
    cnt_list.append(int(word_cnt[1]))


n = 10#过大的话人名会重叠

plt.bar(range(n), cnt_list[0:n])
plt.xticks(range(n), word_list[0:n])
plt.yticks(range(0,max(cnt_list)+100,100))
plt.savefig("./output/三体-人物词频柱状图.png")
plt.show()