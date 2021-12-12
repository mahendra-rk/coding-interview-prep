def balancedBrackets(string):
    pairs = {')':'(', '}':'{', ']':'['}
    stack = []
    for item in string:
        if item in pairs.keys(): # check if closing bracket
            if stack and stack[-1] == pairs[item]: # check if last item in stack is bracket pair ith current bracket
                stack.pop()
            else:
                return False
        elif item in pairs.values(): # append opening bracket to stack
            stack.append(item) 
    return not stack
    