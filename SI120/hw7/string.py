a = ""
import sys
for line in sys.stdin:
        tmpStr = line.split()
        print("&" + "".join(tmpStr) + "\\")

# a= list(a)
# b = len(a)
# c = b // 30
# d = 0
# for i in range(c):
#         a.insert(d, '&')
#         d += 30
#         a.insert(d, '\\')
# a="".join(a)
# print(str(a))
