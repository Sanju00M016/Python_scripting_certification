#problem 2

string = input("Enter the list of items:->")
string.split(",")
find_str = input("Enter the elements which you need to find:->")

list_str = str(string)

if find_str in list_str:
    print("the element %s is found at position "%(find_str),list_str.index(find_str)+1)
else:
    print("The Element %s is not present in given list"%(find_str))

