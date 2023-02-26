#Algorithm

"""
    start
    get gold karat
    if gold karat = 18
    gold price = 18 * 148.94
    print gold price
    else if gold karat = 21
    gold price = 21 * 173.76
    print gold price
    else if gold karat = 22
    gold price = 22 * 182.03
    print gold price
    else if gold karat = 24
    gold price = 192.58 * 24
    print gold price
    stop
    
"""

karat = int(input('Enter gold karat: '))
# we checking if the gold karat is either 18,21,22 or 24
if karat == 24:
    gold_price = 192.58 * karat
    print('Karat: ', karat, 'Weigh: 192.58', 'Gold Price: ', gold_price )
    # check if the karat is 22
elif karat == 22:
    gold_price = 182.03 * karat
    print('Karat: ', karat, 'Weigh: 182.03', 'Gold Price: ', gold_price)
    # check if the karat is 21
elif karat == 21:
    gold_price = 173.76 * 21
    print('Karat: ', karat, 'Weigh: 173.76', 'Gold Price: ', gold_price )
    # check if the karat is 18
elif karat == 18:
    gold_price = 148.94 * 18
    print('Karat: ', karat, 'Weigh: 148.94', 'Gold Price: ', gold_price )
    # if user enters any other number then the programs prints wrong input
else:
    print('Wrong input')