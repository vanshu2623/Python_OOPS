# s = "Ankit Kumar Tiwari"

# words = 1
# for char in s:
#     if char == " ":
#         words += 1

# print(words)

# s = "Ankit Kumar Tiwari"

# words = ""
# for char in s:
#     if char == " ":
#         print(words)
#         words = ""
#     else:
#         words += char  

# print(words)

def my_split(st):
    words_list =[]

    word = ""
    for i,ch in enumerate(st):
        