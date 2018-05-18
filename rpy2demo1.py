from rpy2.robjects.packages import importr
import rpy2.robjects as robjects

#导入r包
base=importr('base')

#获取r对象
pi=robjects.r['pi'] #执行r代码，结果是r向量
piplus2=pi+2
print(piplus2.r_repr()) #r_repr()以r形式展示向量
pi0plus2=pi[0]+2 #获取pi值
print(pi0plus2)

#向r代码字符串中插入r对象
letters=robjects.r['letters']
rcode='paste (%s,collapse="-")' % letters.r_repr()
res=robjects.r(rcode)
print(res.r_repr())

#创建r向量
v=robjects.StrVector(['abc','def'])
robjects.IntVector([1,2,3])
robjects.FloatVector([1.1,1.2,1.3])
print(v.r_repr())

#创建r矩阵
v2=robjects.FloatVector([1.1,1.2,1.3,1.4])
m=robjects.r['matrix'](v2,nrow=2)
print(m)

#调用r函数
rsum=robjects.r('sum')
res2=rsum(robjects.IntVector([1,2,3]))
print(res2[0])

#r函数关键词也可用
rsort=robjects.r('sort')
res3=rsort(robjects.IntVector([1,2,3]),decreasing=True)
print(res3.r_repr())
