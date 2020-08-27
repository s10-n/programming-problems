taxRate = {0:0,
           10000: 0.10,
           30000: 0.25,
           100000: 0.40}

def tax(income):
    for i in taxRate:
        if income < i:
            print('Tax rate: ' + str(income * taxRate.get(i)))
            break


tax(0)
tax(10000)
tax(10009)
tax(10010) 
tax(12000) 
tax(56789) 
tax(1234567)
