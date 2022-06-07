while True:
    string = input()
    if string == '.':
        break
    else:
        is_balanced = True
        par = []
        for i in string:
            if i == '(' or i == '[':
                par.append(i)
            elif i == ')':
                if not par or par.pop() != '(':
                    is_balanced = False
                    break
            elif i == ']':
                if not par or par.pop() != '[':
                    is_balanced = False
                    break
        if not is_balanced or par:
            print('no')
        else:
            print('yes')