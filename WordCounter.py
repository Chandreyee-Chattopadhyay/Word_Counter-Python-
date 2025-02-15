import re

def CountWords(str):
    res=re.sub(r'[^\w\s]', '', str)  #it removes extra spaces from string, it only includes word character
    words=0
    for i in range(0,len(res)):
        words = res.split()
    return len(words)

print("Enter a sentence or paragraph")
lines = []
try:
    while True:
        line = input()
        if line == "":  # Stop when the user presses Enter twice
            break
        lines.append(line)

    str = "\n".join(lines)
except:
    str=""
if(len(str)==0):
        print("Number of words in the sentence are: ",len(str))
else:
    print("Number of words in a sentence are: ",CountWords(str))