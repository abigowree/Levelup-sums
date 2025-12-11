str="Gulab Jamun Recipe Tips for Soft & Perfect Gulab Jamun"
count=0
res=str.split()
string="Jamun"
for i in res:
    if i in string:
        count+=1

print(count)



str="heeellloooo"
res=""
for i in str:
    if i not in res:
        res+=i
print(res) 





data = "abi,99|priya,98|ram,100"

records = data.split("|") 

max_name = ""
max_mark = 0

for rec in records:
    name, mark = rec.split(",")   
    mark = int(mark)             
    
    if mark > max_mark:
        max_mark = mark
        max_name = name

print("Top Scorer:", max_name, max_mark)



def highest(words):
    vowels = "aeiouAEIOU"
    max_count = 0
    result = ""

    for word in words:
        count = 0
        for ch in word:
            if ch in vowels:
                count += 1
        if count > max_count:
            max_count = count
            result = word

    return result

print(highest(["education", "rhythm", "beauty", "queue", "try"]))



def twice(string):
    res=""
    for i in string:
        if i not in res:
            res+=i
    print(res)

twice("one two three one four two one")    



def sort_by_length(sentence):
    words = sentence.split()
    words.sort(key=len)
    return words


print(sort_by_length("python is a powerful programming language"))




def replace_vowels(sentence):
    vowels = "aeiouAEIOU"
    result = ""

    for ch in sentence:
        if ch in vowels:
            result += "*"
        else:
            result += ch

    return result



print(replace_vowels("Python is amazing"))


def long_words(sentence):
    words = sentence.split()   # break into list
    result = []                # store answer

    for w in words:
        if len(w) > 4:        # check length
            result.append(w)

    return result


print(long_words("This is a python program"))



def remove_duplicates(s):
    result = ""
    
    for ch in s:
        if ch not in result:
            result += ch
    
    return result


print(remove_duplicates("programming"))



def all_substrings(s):
    result = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            result.append(s[i:j])
    return result

print(all_substrings("abc"))


