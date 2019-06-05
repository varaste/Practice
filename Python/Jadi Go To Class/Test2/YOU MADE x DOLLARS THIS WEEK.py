htime = int(input("Please Enter Yor Work Time: "))
if htime < 0 or htime > 168 :
    print("INVALID")
elif htime < 40:
    me40 = htime * 8
    print("YOU MADE " , me40 , " DOLLARS THIS WEEK")
elif (htime <= 50) and (htime >= 40):
    me50 = ((htime - 40) * 9 ) + 320
    print("YOU MADE " , me50 , " DOLLARS THIS WEEK")
elif htime > 50:
    me100 = ((htime - 50) * 10) + 320 + 90
    print("YOU MADE " , me100 , " DOLLARS THIS WEEK")
