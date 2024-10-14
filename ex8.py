def func(usern,paswd):
    if usern=="user123" and paswd=="pass123":
        print("login is successful")
    else:
        print("login is failed")

usern=input("enter the username:")
paswd=input("enter the password:")
func(usern,paswd)