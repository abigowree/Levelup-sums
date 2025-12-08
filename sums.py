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