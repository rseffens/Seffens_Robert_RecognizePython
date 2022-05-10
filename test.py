# fruit = ('blueberry', 'strawberry', 'banana')
# # tuple - Identified by the () around it.
# print(type(fruit))

# pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# print(pizza_toppings[1])

# person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# print(person['name'])
# person['name'] = 'George'
# person['eye_color'] = 'blue'
# print(person)

# num1 = 42
# num2 = 2.3

# if num1 > 45:
#     print("It's greater")
# else:
#     print("It's lower")

# boolean = True
# # Primative data type
# string = 'Hello World'
# # Primative data type

# if len(string) < 5:
#     print("It's a short word!")
# elif len(string) > 15:
#     print("It's a long word!")
# else:
#     print("Just right!")

# # for x in range(5):
# #     print(x)
# # for x in range(2,5):
# #     print(x)
# # for x in range(2,10,3):
# #     print(x)
# # x = 0
# # while(x < 5):
# #     print(x)
# #     x += 1

#     # pizza_toppings.pop()
# # print(pizza_toppings)
    
#     # print(pizza_toppings.pop(1))

# pizza_toppings.append('pineapples')

# print(pizza_toppings)

# for topping in pizza_toppings:
#     if topping == 'Pepperoni':
#         continue
#     print('After 1st if statement')
#     if topping == 'Olives':
#         break

# def print_hello_ten_times():
#     for num in range(10):
#         print(num)
#         print('Hello')

# print_hello_ten_times()

def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times(4)