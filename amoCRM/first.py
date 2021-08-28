forms = ['программист', 'программиста', 'программистов']


# Choose the form of the word depending on the entered number
def print_appropriate_form(number: str):
    number_length = len(number)

    if number_length == 0 or not is_number(number) or int(number) < 0:
        print('wrong input')
    elif number_length == 1:
        print(number, ' ', default_rule(int(number[-1])))
    else:
        if int(number[-2] + number[-1]) in range(10, 20):
            print(number, ' ', forms[2])
        else:
            print(number, ' ', default_rule(int(number[-1])))


# Get appropriate form for a number in the range from 0 to 9 inclusive
def default_rule(number):
    if number == 1:
        return forms[0]
    elif number in range(2, 5):
        return forms[1]
    else:
        return forms[2]


# Check if the string contains only digits
def is_number(number):
    for character in number:
        if not character.isdigit():
            return False
    return True


for i in range(0, 1150):
    print_appropriate_form(str(i))

print_appropriate_form('2d3')
