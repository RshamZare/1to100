# #compute all the multiples of 3,5 
# # less than 100 

num_list = range(1,100)
total = 0

for i in num_list:
    if i % 3 == 0 and i % 5 == 0:
        total += i

print(total)

total4 = 0
for item in range(1, 100):
    if item % 3 == 0 or item % 5 == 0:
        total4 += item

print(total4)