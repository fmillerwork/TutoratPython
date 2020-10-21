from string import punctuation

string = str(input("Enter a string "))

for i in punctuation:
    for j in string:
        if i == j:
            string = string.replace(j,"")

print(string)
