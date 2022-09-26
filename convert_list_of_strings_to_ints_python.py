a=['1','4','5','7','9']
b=[int(p) for p in a]
print(b)

e=['12','14','16']
print(list(map(int, e)))

a=["1","3","6"]
ints = []
for i in a:
      ints.append(int(i))
      print(i)
a=["3","6","9"]
ints = [eval(x) for x in a] 
print(ints)

a = ["2","3.9","6","9.6"]
ints = [round(float(s) for s in a)]
print(ints)