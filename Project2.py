

# using for and get the average of the elements an check if they are not an number remove them but make others too int 
num_l = ['10',20,30,'ap',40,50,'one'] 
total = 0 
for i in num_l : 
    if i == str(i): 
        num_l.remove('ap')
        num_l[-1] = 1 

        total += int(i) 
    elif i == int(i): 
        total += i 
average = total / len(num_l) 
print(f"Average : {average}")   

# digital scale : making weight to mass using for and if and else  
w_l = [100,300,500] 
m_l = [] 
g = 9.8 
for i in w_l: 
    m = i / g  
    m_l.append(m) 
for x in m_l : 
    print(f"{x} kg") 
# don't know where too use if and else 

    
    
# making multiplication table using for 
x = 11 
a = 1
for i in range(1,x): 
    for k in range(a,x): 
        print(f"{i}*{k} = {i*k}") 
    a += 1 

# use a for avoid repetition 
