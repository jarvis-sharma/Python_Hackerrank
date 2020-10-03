cube = lambda x: x*x*x

def fibonacci(n):
    # return a list of fibonacci numbers
    li=[]
    if n>2:
        li.append(0)
        li.append(1)
        for i in range(n-2):
            li.append(li[i]+li[i+1])
        return li  
    elif n==2:
        return [0,1]
    elif n==1:
        return [0]
    else:
        return []  
