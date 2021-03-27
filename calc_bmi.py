def get_bmi(heigth,weigth):
    h = int(heigth) / 100
    calc_bmi = int(weigth) / (h * h)
    ok_weigth = h * h * 22
    result = (calc_bmi,ok_weigth)
    return result
