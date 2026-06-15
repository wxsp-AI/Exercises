

### using dictionary and work with it 

# getting average battery and total drones count 
battery_t = 0 # battery total
battery_c = 0  # battery count 
drones_c = 0 # drones count
drones = [
    {
        "id": 1,
        "battery": 90,
        "status": "idle"
    },

    {
        "id": 2,
        "battery": 25,
        "status": "idle"
    }
]

for i in drones : 
    battery_t += i["battery"] 
    battery_c += 1  
    if i["status"] == "idle" : 
        drones_c += 1 

average_battery = battery_t / battery_c 

print(f"average_battery : {average_battery} , idle drones count : {drones_c}")


############################################################

# getting each sattelite targets count 
# getting all targets count 
# getting the sattelite with the most targets 
# getting average sattelites height  
s_heights = []
satellites = {
    "S-1": {
        "altitude": 550,
        "targets": ["Tehran", "Paris", "Berlin"]
    },

    "S-2": {
        "altitude": 700,
        "targets": ["Tokyo", "London"]
    }
}
t_s_t_c = 0 # total satellites targets count
s_t = {} # satellite targets
s_w_m_t = 0 # sattelite with most target 
s_w_m_t_n = "" # satellite with most target name
s_h = 0 # satellites height
s_c = 0 # satellites count
for x in satellites : 
    e_s_t = len(satellites[x]["targets"]) 
    s_h += satellites[x]["altitude"]
    print(f"{x} targets : {e_s_t}") 
    t_s_t_c += e_s_t  
    s_t[x] = e_s_t   
    s_c += 1 


for k,v in s_t.items() : 
    if v > s_w_m_t : 
        s_w_m_t = v 
        s_w_m_t_n = k
print(f"most targets {s_w_m_t_n} with {s_w_m_t} targets")

average_h_s = s_h / s_c # average height satellites
print(f"total targets : {t_s_t_c}")  
print(f"average height : {average_h_s}")
#############################################################

# salary  of each part 
# salary of whole company 
# employee with the most salary 
# average salary of each part 
# average salary of whole company 

company = {
    "Engineering": {
        "employees": [
            {"name": "Ali", "salary": 3000},
            {"name": "Sara", "salary": 3500}
        ]
    },

    "AI": {
        "employees": [
            {"name": "Reza", "salary": 5000}
        ]
    }
} 
e_p_s = 0 # each part salary 
c_t_s = 0 # company total salary
e_p_e_c = 0 # each part employees count 
h_c_e_c = 0 # whole company employees count 
e_w_m_s =  0 # employee with most salary 
e_w_m_s_n = "" # emloyee wth the most salary name

for k,v in company.items() : 
    for i in v["employees"]: 
        e_p_s += i["salary"] 
        c_t_s += i["salary"] 
        e_p_e_c += 1 
        h_c_e_c += 1 
        if i["salary"] > e_w_m_s : 
            e_w_m_s = i["salary"]  
            e_w_m_s_n = i["name"]
    print(f"{k} salary : {e_p_s} | average salary : {e_p_s/e_p_e_c}") 
    e_p_s = 0 
    e_p_e_c = 0
print(f"{e_w_m_s_n} has the most salary with ${e_w_m_s}")
print(f"total salary of company : {c_t_s} | average salary : {c_t_s/h_c_e_c}")
    


###############################################################

# each customer name 
# the products that been purchased
# each customer total purchases 
# the customer with the most purchase 
# total sold of the store 

store = {
    "am": [
        {"name": "Laptop", "price": 1200},
        {"name": "Mouse", "price": 50},
    ],

    "ap": [
        {"name": "Phone", "price": 800},
        {"name": "Headphone", "price": 100},
    ]
}  
e_c_t_p = 0 # each customer total purchase  
c_w_m_p = 0 # customer with most purchase 
c_w_m_p_n = "" # customer with most purchase name 
s_t_s = 0 # store total solds
for k,v in store.items() : 
    print(f"customer name : {k}") 
    for i in v : 
        print(f"product name : {i["name"]}")  
        e_c_t_p += i["price"]   
        s_t_s += i["price"]
    if e_c_t_p > c_w_m_p : 
        c_w_m_p = e_c_t_p 
        c_w_m_p_n = k 


    print(f"{k} total purchase is {e_c_t_p}")
    e_c_t_p = 0
print(f"{c_w_m_p_n} has purchase the most with {c_w_m_p}") 
print(f"store total solds is {s_t_s}")