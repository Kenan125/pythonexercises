while True:
    try:

        num1 = float(input("enter number"))
        num2 = float(input("enter second number"))
    except:
        print("wrong type please try again")
        continue
    cmmtxt = input("choose command from below: \nadd \nsubtract \nmultiply \ndivide \n")
    if cmmtxt == "add":
        ans = num2 + num1
        print(ans)
        print("Do you want to continue")
        cnt = input()
        if cnt == "Yes":
            continue
        elif cnt == "No":
            break
    elif cmmtxt == "subtract":
        ans = num1 - num2
        print(ans)
        print("Do you want to continue")
        cnt = input()
        if cnt == "Yes":
            continue
        elif cnt == "No":
            break
    elif cmmtxt == "multiply":
        ans = num2 * num1
        print(ans)
        print("Do you want to continue")
        cnt = input()
        if cnt == "Yes":
            continue
        elif cnt == "No":
            break
    elif cmmtxt == "divide":
        ans = num1 / num2
        print(ans)
        print("Do you want to continue")
        cnt = input()
        if cnt == "Yes":
            continue
        elif cnt == "No":
            break
    else:
        print("wrong command please try again")
        continue
