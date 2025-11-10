

def main():
    switch = 1
    
    while(switch):

        switch = 0

    return;

#simple calculator app functions
def add(a:int | float, b: int | float):
    return a + b

def subtract(a:int | float, b: int | float):
    return a - b

def multiply(a:int | float, b: int | float):
    return a * b

def divide(a:int | float, b: int | float):
    return a / b

def modulo(a:int | float, b: int | float):
    return a % b

def power(a:int | float, b: int | float):
    return pow(a, b)

def abs(a:int | float):
    return abs(a)

def sqrt(a:int | float):
    return sqrt(a)

def max(a:int | float, b: int | float):
    return max(a,b)

def min(a:int | float, b: int | float):
    return min(a,b)

#run from main
if __name__ == "__main__":
    main()