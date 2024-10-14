def func(temp):
    if temp<0:
        print("suggest to wear heavy coat")
    elif temp>=0 or temp<=15:
        print("suggest to wear a jacket")
    elif temp>15 or temp<=25:
        print("suggest to wear a sweater")
    elif temp>25:
        print("suggest to wear t-shirt and shorts")

temp=int(input("enter the urrent temperature="))
func(temp)