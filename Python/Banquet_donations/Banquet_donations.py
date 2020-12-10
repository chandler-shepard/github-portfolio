# Make sure you have also downloaded donation.py and have it saved in the
# same location as Banquet_donations.py

import donation
amount = donation.get_donation()
# this will make the 200 donations then it will sort the number also in order
# from least to greatest.
def get_donations(num):
    total = []
    for i in range(num):
        total.append(donation.get_donation())
    return(sorted(total))

# this will add all the donations together then tell if the goal was met

def get_total(total):
    
    if int(total) >= 2017:
        print("The total amount of money raised is: " + str(total))
        print("The fundraising goal was met!")
    else:
        print("The total amount of money raised is: " + str(total))
        print("The fundraising goal was not met.")
    
    
# this will figure out how many of each bill goes into the total amount that was donated
# as it figures the amount of bills it will subtract that amount from the total
def atm_count(total):
# gets the total amount of donation money

# sets variables to count how many of each bill
    count100 = 0
    count20 = 0
    count10 = 0
    count5 = 0
    count1 = 0
# finds how many 100 bills are in it then subtracts the amount in currency from the toal
    if total >= 100:
        count100 += total // 100
        total -=  count100 * 100
# does the same as 100 but this is for 20s
    if total >= 20:
        count20 += total // 20
        total -= count20 * 20
# this calculates how many 10's
    if total >= 10:
        count10 += total // 10
        total -= count10 * 10
# this is calculating how many 5's
    if total >= 5:
        count5 += total // 5
        total -= count5 * 5
# this calculates how many 1's
    if total >= 1:
        count1 += total // 1
        total -= count1 * 1
    print("$100 bills: " + str(count100))
    print("$20 bills: " + str(count20))
    print("$10 bills: " + str(count10))
    print("$5 bills: " + str(count5))
    print("$1 bills: " + str(count1))

    
# MAIN


# get all of the donations and output the values
print("Here are the donation amounts and in order")
# will use a previous definition
all_donations = get_donations(200)
print(all_donations)
totalamount = sum(all_donations)


# Run the program a few times and notice that the amount changes.



print()

# Section 2 - Compute basic categories
# sets the variables to count how many of each donation type there is
small = 0
medium = 0
large = 0
# runs through the donations and will determine what donation type they are
for num in all_donations:
    if num <= 5:
        small += 1
    if num >= 6 and num <=15:
        medium += 1
    if num >= 16 and num <= 20:
        large += 1
#prints how many donation types there are of each 
print("There were " + str(small) + " small donations ($5 or less)")
print("There were " + str(medium) + " medium donations ($6 - $15)")
print("There were " + str(large) + " large donations ($16 or more)")
print()
# Section 3 - Compute success or failure
 # See if goal of $2017 is met
print(get_total(totalamount))

# Section 4 - What can you expect from the bank?
# will set the saying as a variable 
saying = "The bank cashed this amount out as:"

# prints the saying and below will match the length of the saying with -'s
print(saying)
print(len(saying) * "-")

# this is where the amounts of bills taken from the total are printed
# uses the definiton atm_count()
print(atm_count(totalamount))






