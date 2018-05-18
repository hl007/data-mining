from rpy2.robjects.packages import importr
import rpy2.robjects as robjects


def chisq_test(categorical_var1,categorical_var2):
    pass


data_frame=robjects.r('data.frame')
xtabs=robjects.r('xtabs')
v1=robjects.StrVector(['female','female','male','male'])
v2=robjects.StrVector(['yes','yes','no','no'])
mydata=data_frame(v1.r_repr(),v2.r_repr())
print(mydata)
#mytable=xtabs(mydata)

# importr('vcd')
# rcode='xtabs(~Treatment+Improved,data=Arthritis)'
# res=robjects.r(rcode)
# chisq_test=robjects.r('chisq.test')
# res2=chisq_test(res)
# print(res2)
