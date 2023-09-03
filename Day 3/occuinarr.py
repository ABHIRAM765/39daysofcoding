key = 1
A = [0, 1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1, 0]
count_in_A = A.count(key)
count_in_B = B.count(key)
total_occurrences = count_in_A + count_in_B
print("The key", key ,"occurs" ,total_occurrences, "times in the arrays.")