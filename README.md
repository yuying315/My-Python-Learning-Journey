# My-Python-Learning-Journey
## 一、项目简介
这个仓库用来集中保存我在本学期 Python 课程中编写的小程序，解决的是「练习代码散落在本地各个文件夹、过一段时间连自己都找不到最终版本、也说不清每个程序是干什么的」这个问题。

把代码放进同一个 GitHub 仓库之后，我可以：

- 按课程进度归档每一次练习，随时回看自己写过的代码；
- 用提交记录留下每次修改的原因，看到自己一点点改进的过程；
- 通过这份 README，让别人（也包括几个月后的我）不用逐行读代码就知道每个程序的用途和运行方式。

目前仓库收录 **2 个** 本学期编写、功能完整且可直接运行的 Python 程序，以及这份 `README.md`。
## 二、文件说明
| 文件名 | 用途 |
| --- | --- |
| `[function_bmi.py]` | 输入实验者身高体重并计算bmi，计算后判断bmi指数是否正常 |
| `[yuan.py]` | 输入圆的半径（/矩形的长宽）可计算其周长与面积 |
| `README.md` | 项目简介、文件说明、代码说明、学习心得与规划 | 
## 三、代码说明
### 1、`[function_bmi.py]`
`[程序完成bmi计算与判断实验者bmi水平是否处于正常范围的功能，使用bmi计算公式“体重/（身高*身高）”与if条件句实现]`
```python
def fun_bmi(name, h, w):
    bmi = w/(h*h)
    print(name + "的身高：" + str(h) + "米，体重：" + str(w) + "kg")
    print(name + "的bmi：" + str(bmi))
    if bmi < 18.5:
        print("u are too light\n")
    if bmi >= 18.5 and bmi < 24.9:
        print("normal weight\n")
    if bmi >= 24.9 and bmi < 29.9:
        print("u are too heavy\n")
    if bmi >= 29.9:
        print("u are fat")
a = fun_bmi('zyy', 1.68, 57)
b = fun_bmi('yy', 1.80, 70)
```
### 2、`[yuan.py]`
`[输入圆的半径或矩形的长宽数值，可由圆和矩形的周长、面积计算公式输出圆或矩形的周长或面积]`
```python
import math
PI = math.pi
def circle(r):
    zc = 2*PI*r
    mj = PI*r*r
    print("圆的周长为：" + str(zc) + ",面积为：" + str(mj))

def square(a, b):
    zc = (a + b)*2
    mj = a*b
    print("矩形的周长为：" + str(zc) + ",面积为：" + str(mj))
a = circle(2)
b = square(1,2)
```
# 四、学习心得与规划
写 README 前，我翻了 GitHub 上几个 Python 入门项目。
好的项目往往胜在说明清楚：开头一句话讲清项目解决什么问题，用表格列出每个文件的用途，结尾给出能直接复制运行的命令；提交记录也一小步一小步，说明写得具体。反观我自己，练习文件散落本地、命名随意，过几周就分不清哪个是最终版本。
写 README 也是一次代码复查：为把文件说明和代码说明写准，我重读了两个程序，发现有的变量名连自己都要愣一下才解释得清，有些已知条件也出现了一些错误，因此进行了一些修改。
接下来我打算：每次课后在 README 补一次「新学的语法和踩过的坑」；学期末按主题整理目录，挑一个程序做重构，补上函数拆分和异常处理。让它成为一份更具体的学习记录。
