import calc_bmi as cabmi

print("BMI計算アプリ")
h = (input("身長:"))
w = (input("体重:"))
result = cabmi.get_bmi(h,w)
print(f"BMI:{result[0]}")
print(f"適正体重:{result[1]}")
if int(w) >= result[1]:
    print("食生活を見直しましょう")

