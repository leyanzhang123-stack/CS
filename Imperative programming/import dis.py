import dis

def fun():
    s = 0
    for i in range(5, 16):
        s += i
    return s
 
dis.dis(fun)