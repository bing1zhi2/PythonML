# coding: utf-8

'''
插值是离散函数逼近的重要方法，利用它可通过函数在有限个点处的取值状况，估算出函数在其他点处的近似值。与拟合不同的是，要求曲线通过所有的已知数据。SciPy的interpolate模块提供了许多对数据进行插值运算的函数，范围涵盖简单的一维插值到复杂多维插值求解。当样本数据变化归因于一个独立的变量时，就使用一维插值；反之样本数据归因于多个独立变量时，使用多维插值。
计算插值有两种基本的方法，1、对一个完整的数据集去拟合一个函数；2、对数据集的不同部分拟合出不同的函数，而函数之间的曲线平滑对接。第二种方法又叫做仿样内插法，当数据拟合函数形式非常复杂时，这是一种非常强大的工具。我们首先介绍怎样对简单函数进行一维插值运算，然后进一步深入比较复杂的多维插值运算。

‘zero’ 、'nearest'	阶梯插值，相当于0阶B样条曲线
‘slinear’ 、'linear'	线性插值，用一条直线连接所有的取样点，相当于一阶B样条曲线
‘quadratic’ 、'cubic'	二阶和三阶B样条曲线，更高阶的曲线可以直接使用整数值指定
'''

import numpy as np
from scipy.interpolate import interp1d

#创建待插值的数据
x = np.linspace(0, 10*np.pi, 20)
y = np.cos(x)

# 分别用linear和quadratic插值
fl = interp1d(x, y, kind='linear')
fq = interp1d(x, y, kind='quadratic')

#设置x的最大值和最小值以防止插值数据越界
xint = np.linspace(x.min(), x.max(), 1000)
yintl = fl(xint)
yintq = fq(xint)

import pylab as pl
pl.plot(xint,fl(xint), color="green", label = "Linear")
pl.plot(xint,fq(xint), color="yellow", label ="Quadratic")
pl.legend(loc = "best")
pl.show()

