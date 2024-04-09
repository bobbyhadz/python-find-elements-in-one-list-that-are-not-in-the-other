# Find elements in one list that are not in the other

list_1 = ['a', 'b', 'c']

list_2 = ['a', 'd', 'e']

result_1 = list(set(list_2).difference(list_1))
print(result_1)  # 👉️ ['e', 'd']

# --------------------------------------

result_2 = list(set(list_1).difference(list_2))
print(result_2)  # 👉️ ['b', 'c']