count = 0
for i in range(1, 147):
    for j in range(i + 1, 148):
        if i == j:
            continue
        for k in range(i + 2, 149):
            if k == j or k == i:
                continue
            for m in range(i + 3, 150):
                if m == i or m == j or m == k:
                    continue
                for n in range(i, 151):
                    if n == i or n == j or n == k or n == m:
                        continue
                    count += 1
                    print(count, 'a =', i, 'b =', j, 'c =', k, 'd =', m, 'e =', n)
                    if i ** 5 + j ** 5 + k ** 5 + m ** 5 == n ** 5:
                        print('$', i, j, k, m, n)
                        print('$', i + j + k + m + n)
