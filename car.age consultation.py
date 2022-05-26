driving = input ("請問您有沒有駕照?(有/沒有)")
if driving != "有" and driving != "沒有":
    print("只能輸入 有/沒有!!")
    raise SystemExit
age = input ("請問您的年齡?")

if driving == "有":
    if int(age) >= 18:
        print("您符合開車條件!!")
    else:
        print("您不符合開車條件!!")
elif driving == "沒有":
    if int(age) >= 18:
        print("您可以報考駕照，學習完上路了!!")
    else:
        print(f"再過{18-int(age)}就可以考駕照了")
