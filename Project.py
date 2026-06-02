
#1 Getting length , min and max 

num = [10,20,30,40,50]
print(f"Length : {len(num)} | max : {max(num)} | min : {min(num)}") 

#2 checking and item existance 
print(30 in num) 

#3 remove repeated elements and make a sorted list 
r_num = [2,3,4,6,7,1,3,6,9,5] 
print(sorted(set(r_num)))

#4 slice the list 
print(r_num[3:6]) 

#5 work with for  
students = ['ali','zahra','mohammad','leyla','ariya'] 
for s in students: 
    print(f"Welcome {s.title()}") 
#6 | 1 to 10 power by 3 
print([f"{x} ** 3 : {x ** 3} " for x in range(1,11)]) 

#7 the sum of numbers in a list with for 
total = 0
for n in num : 
    total += n 
print(total) 

#8 square of 1 to 20 with list Comprehension 
print([f"{x} ** 2 : {x ** 2}" for x in range(1,21)]) 

#9 show even numbers from 1 to 50 
print([x for x in range(2,51,2)])



