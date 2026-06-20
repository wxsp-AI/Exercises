

## working whith while loop 

# checking Divisibility of input number

while True : 
    num = int(input("Enter a number : ")) 
    if num % 15 == 0 : 
        print("FizzBuzz") 
    elif num % 3 == 0 : 
        print("Fizz") 
    elif num % 5 == 0 : 
        print("Buzz") 
    else : 
        print(num) 

#################################### 

# getting 2 inputs of name and favorite book and add them into dict as key and value 
dic = {}
while True : 
    name = input("Whats ur name ?\n ") 
    f_book = input("Whats ur favorite book ?\n")
    dic[name] = f_book 
    ask = input("is there any body else ? yes/no \n") 
    if ask == "yes" : 
        continue 
    break 
for k,v in dic.items() : 
    print(f"{k} love reading {v}")

#################################### 

# pop items using while and append to another list 

shopping_cart = ['milk', 'bread', 'eggs', 'apple'] 
purchased_item = [] 
while shopping_cart : 
    p_item = shopping_cart.pop() 
    purchased_item.append(p_item) 
    print(f" puchasing : {p_item}")
print(purchased_item) 

#################################### 


# checking if name in the list get two input and add them into dict as items (name as key and other two as value)

users = ['admin', 'john', 'sara', 'mike'] 
user_info = {} 
while True : 
    name = input("Enter ur name : (exit) to end \n") 
    if name in users : 
        age = int(input("How old are u ? \n")) 
        city = input("Where are u from ? \n") 
        user_info[name] = [age , city] 
    elif name == "exit" : 
        break
    else : 
        print("user not found")  
print(user_info)
    
