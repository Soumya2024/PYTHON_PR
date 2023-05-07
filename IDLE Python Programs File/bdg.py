n = int(input())
budget = int(input())
actors = list(map(int, input().split()))

i, j = 0, n - 1
min_diff = float('inf')
min_i, min_j = i, j

while i < j:
    total_fee = actors[i] + actors[j]
    diff = abs(total_fee - budget)
    if diff < min_diff:
        min_diff = diff
        min_i, min_j = i, j
    if total_fee >= budget:
        j -= 1
    else:
        i += 1

print(actors[min_i])
print(actors[min_j])

