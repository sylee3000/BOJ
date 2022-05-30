while True:
    case = input()
    if case == "0":
        break
    else:
        if case == case[len(case) - 1::-1]:
            print('yes')
        else:
            print('no')