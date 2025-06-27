# list of all numbers
num = [56, 75, 1, 46, 100, 97, 75, 46, 46] 

# single numbers
non_duplicate_num = [] 

# duplicated numbers
duplicate_num = [] 

# For loop to iterate over numbers list.
for x in num:
    if x not in non_duplicate_num and x not in duplicate_num:
        non_duplicate_num.append(x)
    else:
        duplicate_num.append(x)    

print("Non Duplicate Numbers: ", non_duplicate_num)
print("Duplicate Numbers: ", duplicate_num)