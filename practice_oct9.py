# l = [20,30,60,89,40,60,90]

# l[-2] = 100
# print(l)

# l = [20,30,60,89,40,60,90]
# half = len(l) // 2
# print(sum(l[:half]))
    
# l = [20,30,60,89,40,60,90]
# s = len(l)    
# c = l[3::]
# print(sum(c))
#    

l = [20,30,60,89,40,100,90]
new_list = []
for i in range(0,len(l)//2+1):
    s = 0
    s = l[i] + l[len(l)-i-1]
    new_list.append(s)

print(new_list) 

l = [110, 130, 100, 178]
new_list = []
for i in range(0,len(l)//2+1):
    s = 0
    s = l[i] + l[len(l)-i-1]
    new_list.append(s)

print(new_list)


l = [110, 130, 100, 178]
new_list = []

for i in range(len(l)//2):
    s = l[i] + l[len(l)-i-1]
    new_list.append(s)

print(new_list)


l = [288, 230]
new_list = []

for i in range(len(l)//2):
    s = l[i] + l[len(l)-i-1]
    new_list.append(s)

print(new_list)