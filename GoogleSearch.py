'''
На вход подается натуральное число, затем столько же строк, затем число поисковых запросов,
затем поисковые запросы. Написать программу, которая выводит все введенные строки, в 
которых встречаются одновременно все поисковые запросы.
'''
n = int(input())
a = []
for _ in range(n):
    s = input()
    a.append(s)

k = int(input())
a_query = []
for _ in range(k):
    s = input()
    a_query.append(s)

for s in a:
    count = 0
    for query in a_query:
        if s.lower().find(query.lower()) != -1:
            count += 1
    if count == len(a_query):
        print(s)