list = [12,23,43,88,76,34,54,56,99,23.5]
print(list)
b = sum(list)
print(b)
c = len(list)
print(c)

d = float(b/c)
print("Average = ",d)
j2 = sorted(i for i in list if i >= 50)
print(j2)
j2sum = sum(j2)
print(j2sum)

def getgreaterthan50 (list):
