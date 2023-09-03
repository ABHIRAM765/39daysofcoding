a = [0, 1, 2, 3, 4, 5]
b = [8,1,11,3,16,5]
s_a = set(a)
s_b= set(b)
duplicates = s_a.intersection(s_b)
if duplicates:
    print("Duplicates found:", duplicates)
else:
    print("No duplicates found.")