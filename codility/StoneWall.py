def solution(H):
    # write your code in Python 2.7
    stk = []
    num = 0;
    
    for blk in H:
        while len(stk) > 0 and stk[-1] > blk:
            stk.pop()
        if len(stk) == 0:
            stk.append(blk)
            num+=1
        elif stk[-1] < blk:
            stk.append(blk)
            num+=1
    
    return num
