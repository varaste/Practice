# 100/100 Accepted
def game(number):
    input_num = number
    int_input_num = int(input_num)
    dah = int_input_num//10
    yek = int_input_num%10
    difference = 0
    if dah > yek:
        difference = dah - yek
    else:
        difference = yek - dah
    return difference
    
