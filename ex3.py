def func(str1):
    all_freq={}
    for i in str1:
        if i in all_freq:
            all_freq[i] +=1
        else:
            all_freq[i]=1
    print("the number of occurance \n"+str(all_freq))
    
str1="visibility"
func(str1)