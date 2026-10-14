# input_str = "aaabbbcca"
# result = {}
# for i in input_str:
#     if i not in result:
#         result[i] = 1
#     else:
#         result[i] +=1 

# print(result)


s = "aaabbbcca"
def remove_duplicates(s):
    new_str = []
    for n in s:
        if n not in new_str:
            new_str.append(n)
    return new_str

nl = remove_duplicates(s)

freq = {}
for i in nl:
    freq[i] = s.count(i)

print("nl =", nl)
print("freq =", freq)