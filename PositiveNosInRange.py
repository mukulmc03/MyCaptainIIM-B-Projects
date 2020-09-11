#Program to print positive nos in range

def PositiveNos(list):
    print("Postive Numbers in give range are")
    for i in list:
        if i >= 0:
            print(i)
        else:
            continue

list = []
n = int(input("Enter size of list: "))

for j in range(0, n):
    print("Enter number at location", j, ":")
    item = int(input())
    list.append(item)
print("Given List is ", list)
PositiveNos(list)