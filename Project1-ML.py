import numpy as np
import matplotlib.pyplot as plt 

#1 making a function for getting a plot 

def plot_line(x,y,title): 
    fig , ax = plt.subplots(figsize=(8,6)) 
    ax.plot(x,
            y,
            color='red', 
            linestyle='--')
    ax.set_title(title) 
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.grid(True) 
    ax.legend()
    plt.show() 

x1 = [4,7,9,12] 
y1 = [3,7,8,9] 
plot_line(x1,y1,'plot') 

#2 making a class init gets x & y and adding 2 methods 1 for getting plot with size and color and 2 add labels 

class SccatterPloter : 
    def __init__(self,x,y): 
        self.x = x 
        self.y = y 
        self.fig ,self.ax = fig , ax = plt.subplots(figsize=(8,6))

    def plot(self,size=30,color='blue'): 
         
        self.ax.plot(self.x ,
                self.y,
                color, 
                size)
          
    def add_labels(self, xlabel, ylabel, title): 
        self.ax.set_title(title) 
        self.ax.set_xlabel(xlabel) 
        self.ax.set_ylabel(ylabel) 

    
x = [3,6,7,9] 
y = [5,6,8,91] 
o1 = SccatterPloter(x,y) # one object of the class
o1.plot() 
o1.add_labels('x','y','plot') 
plt.show() 

#3  making 
class BaseChart:

    def show(self):
        plt.show()


class BarChart(BaseChart):

    def __init__(self, categories, values):
        self.c = categories
        self.v = values

        self.fig, self.ax = plt.subplots(figsize=(8, 6))

    def plot(self):

        self.ax.bar(self.c, self.v, color='blue')

        self.ax.set_title('Bar plot')
        self.ax.set_xlabel('Categories')
        self.ax.set_ylabel('Values')


c1 = ['A','B','C','D']
v1 = [10,20,15,25] 
ch = BarChart(c1,v1) 
ch.plot() 
ch.show() 

#4 making a function for showing histogram and show mean with a red line and show var 


def plot_histogram(data, bins=10, color='green'):

    mean = np.mean(data)
    var = np.var(data)

    fig, ax = plt.subplots(figsize=(8, 6))

    ax.hist(data, bins=bins, color=color)

    

    ax.set_title(f' var: {var:.2f}') # using .2f to display only two decimal places of var

    ax.set_xlabel('Values')
    ax.set_ylabel('Frequency')
    ax.axvline(mean, color='red', linestyle='--', label='Mean') #learn this by researching 
    ax.legend()

    plt.show()


data = np.random.normal(25,40,1000)

plot_histogram(data)  

#5 make a function ,getting a list of datas and make a box plot for each 

def plot_box(data):

    fig, ax = plt.subplots(figsize=(8, 6))


    ax.boxplot(
        data,    
        patch_artist=True
        )

    ax.set_title('Box Plot')
    ax.set_xlabel('Groups') 
    ax.set_xticklabels([1,2,3]) #label of each box plot 

    plt.show()


data = [
    [10, 12, 14, 15, 16, 18, 50],
    [20, 22, 24, 25, 26, 28, 80],
    [5, 7, 8, 9, 10, 12, 40]
]

plot_box(data)

