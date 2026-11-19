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

