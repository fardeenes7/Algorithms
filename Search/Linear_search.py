array = [10,15,20,25,30,35,40,50,60,70,80,90,100]
x = int(input("Enter the number you want to search: "))

def search(x):
    for index in range(len(array)):
        if array[index] == x:
            return index   
    return -1


result = search(x)
if result == -1:
    print("{} not found on the array.".format(x))
else:
    print("{} found in index {}.".format(x,result))