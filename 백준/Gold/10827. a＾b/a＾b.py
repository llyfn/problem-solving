a, b = input().split()
d = len(a) - a.find(".") - 1
a = int(a.replace(".", ""))
b = int(b)
a **= b
a = str(a)
d *= b
if len(a) < d: a = "0" * (d - len(a)) + a
a = a[:-d] + "." + a[-d:]
if a[0] == ".": a = "0" + a
print(a)
