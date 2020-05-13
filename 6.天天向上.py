'''
dayfactor=0.005    
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("天天向上：{:.2f}  天天向下：{:.2f}".format(dayup,daydown))
'''

'''
dayup=1.0
dayfactor=0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print('工作日的力量：{:.2f}'.format(dayup))
'''


def dayup(df):
    dayup=1.0
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup

dayfactor = 0.01
while dayup(dayfactor) < 37.78:
    dayfactor +=0.001

print("运行结果：{:.3f}".format(dayfactor))
