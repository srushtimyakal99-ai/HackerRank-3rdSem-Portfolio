def matchingStrings(stringList, queries):
    frequency = {}

    for s in stringList:
        frequency[s] = frequency.get(s, 0) + 1

    result = []

    for q in queries:
        result.append(frequency.get(q, 0))

    return result


n = int(input("Enter number of strings: "))

stringList = []

print("Enter the strings:")

for i in range(n):
    stringList.append(input())

q = int(input("Enter number of queries: "))

queries = []

print("Enter the queries:")

for i in range(q):
    queries.append(input())

result = matchingStrings(stringList, queries)

print("Output:")

for value in result:
    print(value)