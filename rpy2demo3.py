from rpy2.robjects import FloatVector
from rpy2.robjects.packages import importr
import rpy2.robjects as robjects

stats=importr('stats')
base=importr('base')
v1=FloatVector([4.17,5.58,5.18,6.11,4.50,4.61,5.17,4.53,5.33,5.14])
v2=FloatVector([4.81,4.17,4.41,3.59,5.87,3.83,6.03,4.89,4.32,4.69])

#线性回归
robjects.globalenv['v1']=v1 #将v1设为r中的全局变量
robjects.globalenv['v2']=v2 #将v1设为r中的全局变量
fit=stats.lm('v1~v2')
#print(stats.anova(fit))
#print(base.summary(fit))
#print(fit.names)
print(fit.rx('coefficients'))