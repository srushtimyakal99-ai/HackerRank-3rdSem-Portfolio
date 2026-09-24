def compareTriplets(a, b):
    alice = 0
    bob = 0

    for i in range(3):
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1

    return [alice, bob]


a = list(map(int, input("Enter Alice's ratings: ").split()))
b = list(map(int, input("Enter Bob's ratings: ").split()))

result = compareTriplets(a, b)

print("Alice:", result[0])
print("Bob:", result[1])