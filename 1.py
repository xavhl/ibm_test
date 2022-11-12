from collections import Counter

num_t_available = input()
t_available = input()
num_t_request = input()
t_request = input()

t_stock = Counter(t_available.split())
t_req = Counter(t_request.split())

for t_size, cnt in t_stock.items():
    if cnt < t_req[t_size]:
        print('No')
        break
else:
    print('Yes')