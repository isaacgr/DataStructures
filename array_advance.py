def array_advance(arr):
    furthest_reached = 0
    last_idx = len(arr) - 1
    i = 0
    while i <= furthest_reached and furthest_reached < last_idx:
        furthest_reached = max(furthest_reached, arr[i] + i)
        i += 1
    return furthest_reached >= last_idx

arr = [3,3,1,0,2,0,1]
print array_advance(arr)

arr = [3,2,0,0,2,0,1]
print array_advance(arr)
