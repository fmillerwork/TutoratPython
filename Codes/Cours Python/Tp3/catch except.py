text1="fzfozfzf"
text2="sqsdfgs"

print(text1+text2)
print(2*text1)


try: 
    print(text1.index("o"))
except :
    print ("o est pas dans le string")


try:
    text1.index("m")
except :
    print ("m est pas dans le string")
