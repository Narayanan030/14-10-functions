def func(li1,li2):
    li1.append(li2)
    print(li1)

li1=[1,2,3,4,5,6]
li2=int(input("enter the number="))
func(li1,li2)