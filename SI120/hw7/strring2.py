import sys
a = input()
a = list(a)
d = 0
delta = 80
for i in range(len(a)//delta):
        a.insert(d, "&")
        d+=delta
        a.insert(d, "\\\\")
        d += 1
        a.insert(d, "\n")
        d += 1
a.insert(d, "&")
d=len(a) + 1
a.insert(d, "\\\\")
print("".join(a))