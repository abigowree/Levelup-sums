city = ['Chennai','Bengaluru','Delhi']
summer = [100,220,400]
winter = [100,220,400]
monsoon = [100,220,400]

def rainfall(season):
    if season == 'summer':
        store = summer
    elif season == 'winter':
        store = winter
    elif season == 'monsoon':
        store = monsoon
    else:
        print("Invalid input")

    max = store[0]
    name = city[0]

    for i in range(1, len(store)):
        if store[i] > max:
            max = store[i]
            name = city[i]

    print(name)

rainfall("summer")




Master_list = [10,20, 30, 40, 50] 
Current_list = [40, 10, 20, 50]


for num in Master_list:
    if num not in Current_list:
        print(num)

