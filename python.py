num1 = 42   
# variable declaration intiger 
num2 = 2.3
# # variable declaration of float
boolean = True
# Primative data type
string = 'Hello World'
# Primative data type
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# composite - list - array in js
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# composite dictionary - object in js
fruit = ('blueberry', 'strawberry', 'banana')
# tuple - Identified by the () around it.
print(type(fruit))
# log statement, since type is first, it will just return 'tuple'
print(pizza_toppings[1])
# log statement - prints Sausage
pizza_toppings.append('Mushrooms')
# list add value, add mushrooms to the end. 
print(person['name'])
# log statment
person['name'] = 'George'
# list add value, returns no response as we do not have a list of names, only a dictionary. 
person['eye_color'] = 'blue'
# dictionary add value
print(fruit[2])
# log statement, will return banana

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
    # if/else statement. 

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)
# for loop starting at 0, stopping at 4, incramenting by 1 and breaking at 4

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
# initially will print Hello 10 times because we default to x=10
print_hello_x_or_ten_times(4)
# prints hello 4 times as we swithc out the x for 4, so it will run 4 times. 


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)