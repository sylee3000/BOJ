N = int(input())
exp = input()
operand = {}
for i in range(N):
    operand[chr(65 + i)] = int(input())
stack = []
for i in exp:
    if 'A' <= i and i <= 'Z':
        stack.append(operand[i])
    else:
        op2 = stack.pop()
        op1 = stack.pop()
        if i == '+':
            stack.append(op1 + op2)
        elif i == '-':
            stack.append(op1 - op2)
        elif i == '*':
            stack.append(op1 * op2)
        elif i == '/':
            stack.append(op1 / op2)
print(f'{stack[0]:.2f}')