#corgan prisbrey CIS129 lab 5

keep_going = 'y'
payout_per_bottle = .1

while keep_going == 'y':
    total_bottles = 0
    counter = 1
    today_bottles = 0
    total_payout = 0

    while counter <= 7:
        today_bottles = int(input(f"Enter number of bottles for day #{counter}:  "))
        total_bottles += today_bottles
        counter += 1
   
    total_payout = total_bottles * payout_per_bottle
    
    print()

    print(f"The total number of bottles collected is {total_bottles}")
    print(f"The total paid out is $ {total_payout}")

    print()

    print("Do you want to enter another week's worth of data?")
    keep_going = input("(Enter y or n): ")
    print()
