#counts number of times fizz shows up in a list

def fizz_count(x):
    count=0
    for item in x:
        if item == "fizz":
            count = count + 1
    return count  
    
    
#counts the number of numbers above 10 in a list 

def count_small(numbers):
    total = 0
    for n in numbers:
        if n < 10:
            total = total + 1
    return total

lost = [4, 8, 15, 16, 23, 42]
small = count_small(lost)
print small