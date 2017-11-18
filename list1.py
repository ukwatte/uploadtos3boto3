list = [12,23,43,88,76,34,54,56,99,23.5,45,99]

def getgreaterthan50 (list):
    h3 = sorted(i for i in list if i >= 50)
    print(sum(h3))

getgreaterthan50(list)
print(sum(list))
