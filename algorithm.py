list = [5, 78, 2, 38, 6, 91, 3]

for j in range(len(list)):
    for i in range(len(list)-1-j):
        if list[i] > list[i+1]:
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp

print(list)

def search(list, num):
    for element in range(len(list)):
        if num == element:
            print(f"Eksistē: {i}")
            return
    print("Neeksistē")

search(list, 2)
search(list, 23)

