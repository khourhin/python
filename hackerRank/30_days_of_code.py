def day2():
    """
    Operators
    """
    meal_cost = float(input("Meal cost:"))
    tip_percent = int(input("Tip percent:")) / 100.0
    tax_percent = int(input("Tax percent")) / 100.0

    total_cost = meal_cost + meal_cost * tip_percent + meal_cost * tax_percent
    
    print("The total meal cost is {:.0f} dollars.".format(total_cost))

    
def day5():
    """
    Loops
    """
    number = int(input())
    
    for i in range(1, 11):
        print("{0} x {1} = {2}".format(number, i, number*i))


def day6(n_tests, word_list):
    """
    Let's Review
    """

    for word in word_list:
        print("{0} {1}".format(word[0::2], word[1::2]))


def day7(inlist):

    rev_list = " ".join([i for i in reversed(inlist)])
    print(rev_list)

def day8():
    import fileinput
    inp = fileinput.input()
    
    phone_dict = {}
    n_test = int(next(inp))
    
    for n in range(n_test):
        name, phone = next(inp).strip().split()
        phone_dict[name] = phone
        
    for line in inp:
        query = line.strip()
        if query in phone_dict:
            print("{0}={1}".format(query, phone_dict[query]))
        else:
            print("Not found")
