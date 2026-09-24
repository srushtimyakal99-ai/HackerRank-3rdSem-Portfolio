def dynamicArray(n, queries):
    seqList = [[] for _ in range(n)]
    answer = []
    lastAnswer = 0

    for query in queries:
        type_ = query[0]
        x = query[1]
        y = query[2]

        index = (x ^ lastAnswer) % n

        if type_ == 1:
            seqList[index].append(y)

        elif type_ == 2:
            lastAnswer = seqList[index][y % len(seqList[index])]
            answer.append(lastAnswer)

    return answer


n, q = map(int, input("Enter n and q: ").split())

queries = []

print("Enter the queries:")

for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)

result = dynamicArray(n, queries)

print("Output:")

for value in result:
    print(value)