
## work with def 
# get arguments for brand and model and if year is given show that in output too
def car(brand,model,year = '') : 
    if year : 
        print(f"Name : {brand} | Model : {model} | Made in {year}") 
    else : 
        print(f"Name : {brand} | Model : {model}") 
car('Audi','a4',2013)
car('Audi','a4')

#############################################

# get title and author as argument and return an str 

def book(title,Author): 
    return f"book_info(\"{title}\", \"{Author}\")" 
a = book('python','Eric Matthes')
print(a) 

##############################################

# getting name and print an message until user input q 

def hi(f_name,l_name): 
    print(f"HI {f_name} {l_name}") 
while True : 
    x = input("Enter ur first name : (q) to end \n ") 
    if x == 'q' : 
        break
    y = input("Enter ur last name : ")
    hi(x,y) 

############################################### 

# printing name and type with def and set an default value for type 

def animal(name,type = 'cat'): 
    print(f"{name} : {type}") 

animal('jessi') 
animal('rex','dog') 

###############################################

# pop items from a list and append it to another using def
def resturant(x,y): 
    while  x : 
        c = x.pop() # completed order  
        print(f"Preparing {c}")  
        y.append(c) 
        
    print(y) 

orders = [
    "Pizza",
    "Burger",
    "Pasta"] 
completed_orders = []  

resturant(orders,completed_orders)

##########################################

def build_student(first_name,last_name,**z): 
    z["first_name"] = first_name 
    z["last_name"] = last_name 
    print(z)
build_student(
    "Ali",
    "Ahmadi",
    university="Sharif",
    major="Computer",
    age=22
)


#########################################
# getting some elements and add them too a dict as a value and append the dict to a list and cointinue this procces until user input q
def uni_student(): 
    li = []
    while True : 
        d = {}
        f = input('Enter ur first name : (q) for end \n ')  
        if f == 'q' : 
            break
        l = input('Enter ur last name : ') 
        m = input('Enter ur major : ') 
        a = int(input('Enter ur age : ')) 

        d['first_name'] = f
        d['last_name'] = l 
        d['major'] = m 
        d['age'] = a 
        li.append(d)   
    print(li)

uni_student()
