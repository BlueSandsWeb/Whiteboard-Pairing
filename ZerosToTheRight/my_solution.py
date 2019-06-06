def zeros_to_the_right(arr):
    count = 0
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            move_item = arr.pop(i)
            arr.append(move_item)
            count += 1
    print(arr)
    return count


print("Number of non-zero integers: ", zeros_to_the_right([0, 3, 1, 0, -2]))
# should print:
# [-2, 3, 1, 0, 0]
# Number of non-zero integers: 3

print("Number of non-zero integers: ",
      zeros_to_the_right([1, 2, 3, 0, 4, 0, 0]))
# should print:
# [1, 2, 3, 4, 0, 0, 0]
# Number of non-zero integers: 4

print("Number of non-zero integers: ", zeros_to_the_right([4, 1, 2, 5]))
# should print:
# [4, 1, 2, 5]
# Number of non-zero integers: 4

print("Number of non-zero integers: ", zeros_to_the_right([0, 0, 0, 0, 0]))
# should print:
# [0, 0, 0, 0, 0]
# Number of non-zero integers: 0

print("Number of non-zero integers: ",
      zeros_to_the_right([0, 0, 0, 0, 3, 2, 1]))
# should print:
# [1, 2, 3, 0, 0, 0, 0]
# Number of non-zero integers: 3
