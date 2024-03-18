
data = [3, 1, 6, 8, 12, 4, 9, 11, 2, 10]
target = int(input("target = "))

long = len(data) - 1
print("len: ", long)
low = 0
print("low: ", low)
i = 0
data.sort()
print(data)


while True:
    middle = (long + low) // 2
    print("middle: ", middle)
    if data[middle] == target:
        print(f"bu son {middle}-indexda joylashgan")
        i += 1
        break

    elif data[middle] < target:
        low = middle + 1

    elif data[middle] > target:
        long = middle - 1

    i += 1

print("Qadamlar soni: ", i)
