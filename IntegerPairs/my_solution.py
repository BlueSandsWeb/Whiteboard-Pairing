def integerPairs(arr, k):
    answers = []
    printOut = ''
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if i + j == 11:
                answers.append([i, j])
                if len(printOut) == 0:
                    printOut += f"'{i} {j}'"
                else:
                    printOut += f", '{i} {j}'"

    print(printOut)

integerPairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11 )
integerPairs([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 15 )

