def multi_multiplicacao(*params):
    multi = 1

    for item in params:
        multi *= item
    
    print(multi)

multi_multiplicacao(1, 2)