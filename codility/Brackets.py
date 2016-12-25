def solution(S):
    stk = []
    
    for char in S:
        if char == '['or char == '{' or  char == '(':
            stk.append(char)
        else:
            if len(stk) == 0:
                return 0
            left = stk.pop()
            if not isPair(left, char):
                return 0
                
    if len(stk) == 0:
        return 1
    return 0
        

def isPair(left, right):
    if left == '{' and right == '}':
        return True
    if left == '[' and right == ']':
        return True
    if left == '(' and right == ')':
        return True
    return False
