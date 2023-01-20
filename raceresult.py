def raceresult(user):
    opp_1 = 9.58
    opp_2 = 10.34
    opp_3 = 12.27
    win_point = 0
    
    if user < opp_1 and user < opp_2 and user < opp_3:
        return("You won golden medal!")
    elif user < opp_1 and user < opp_2 or user < opp_2 and user < opp_3 or user < opp_1 and user < opp_3:
        return("You won silver medal.")
    elif user < opp_1 or user < opp_2 or user < opp_3:
        return("You won bronze medal.")
    else:
        return("You won no medal.")

print(raceresult(10))