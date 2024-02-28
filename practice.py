'''
# Selection Sort - 
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

my_ls = [4, 9, 2, 6, 1, 8, 4, 5, 2]
print(selection_sort(my_ls))



# Insertion Sort - 
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

my_ls = [4, 9, 2, 6, 1, 8, 4, 5, 2]
print(insertion_sort(my_ls))


# Binary Search (Using Recursion)- 
def binarySearch(arr, low, high, x):
    if high < low:
        return -1
    mid = (low + high) // 2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binarySearch(arr, low, mid-1, x)
    else:
        return binarySearch(arr, mid + 1, high, x)

arr = [4, 5, 2, 3, 1, 9, 10, 45]
result = binarySearch(arr, 0, len(arr)-1, 10)
print(result)



# Binary Search (Without Recursion)
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

arr = [4, 5, 2, 3, 1, 9, 10, 45]
result = binary_search(arr, 100)
print(result)

'''




# Single Inheritance -
class Item:
    def __init__(self):
        self.name = ''
        self.quantity = 0
    def set_name(self, nm):
        self.name = nm
    
    def set_quantity(self, qnty):
        self.quantity = qnty
    
    def display(self):
        print(self.name, self.quantity)

class Produce(Item):
    def __init__(self):
        Item.__init__(self)
        self.expiration = ''
    
    def set_expiration(self, expir):
        self.expiration = expir
    
    def get_expiration(self):
        return self.expiration
    



# Multiple Inheritance - 
class CarMaker:
    def __init__(self, maker):
        self.maker = maker

class CarModel:
    def __init__(self, model):
        self.model = model
    
class Car(CarMaker, CarModel):
    def __init__(self, maker, model):
        CarMaker.__init__(self, maker)
        CarModel.__init__(self, model)
    
    def printCars(self):
        print("The car is ", self.maker, self.model)

BMW = Car("bmw", "x6")
BMW.printCars()





# Multilevel Inheritance - 
class base:
    def __init__(self, maker):
        self.maker = maker
    
class child(base):
    def __init__(self, maker, model):
        base.__init__(self, maker)
        self.model = model

class grandchild(child):
    def __init__(self, maker, model, year):
        child.__init__(self, maker, model)
        self.year = year
    
    def printCars(self):
        print("The car is ", self.maker, self.model, self.year)

BMW = grandchild("bmw", "x6", 2022)
BMW.printCars()






# Hierarchical Inheritance - 
# When there is one parent having mutiple child classes 


# Hybrid Inheritance - 
# Mix of all types of inheritance 





# ----------------------------------------------------

# Insertion Sort - 

def ins_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr