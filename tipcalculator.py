def tip_calc(bill, p_tip):
    total = bill + bill*p_tip/100
    return total

print(tip_calc(200, 4))