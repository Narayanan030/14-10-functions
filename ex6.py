def func(paswd):
    rent=input("renter the password:")
    if rent==paswd:
        print("login is successful")
    else:
        print("login is failed")

paswd=input("enter the password:")
func(paswd)