#计算IBM
height,weight = eval(input("输入身高（米）和体重（公斤）并用逗号隔开："))
BMI = weight/pow(height,2)
print("BMI为：")
who,nat="",""
if BMI <18.5:
    who,nat="偏瘦","偏瘦"
elif 18.5<= BMI <24:
    who,nat="正常","正常"
elif 24<=BMI<25:
    who,nat="正常","偏胖"
elif 25<=BMI<28:
    who,nat="偏胖","偏胖"
elif 28<=BMI<30:
    who,nat="偏胖","肥胖"
else:
    who,nat="肥胖","肥胖"
print("BMI指标为：国际为{0}，国内为{1}".format(nat,who))
