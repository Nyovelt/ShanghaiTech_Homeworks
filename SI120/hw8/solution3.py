import collections
import sys
from itertools import combinations, permutations
sys.setrecursionlimit(10000000) #Enlarge maximum recursion depth 

def Exgcd(a: int, b: int):
    '''
            gcd(a,b)=ax+by
    '''
    if (not b):
        return [1, 0]
    x, y = Exgcd(b, a % b)
    return [y, x - a // b * y]

def inv(x: int, mod: int):
        return Exgcd(x, mod)[0] % mod

def TSSS(mod: int, **args) -> int:
        '''
        args: dic{}

        return secret s = f(0) by Lagrange Interpolation
        '''
        s = 0
        for i in args:
                terms = 1 #Terms of each f(i)delta_i(0)
                deno = 1  #Denominator
                for j in args:
                        if i == j:
                                continue
                        terms = terms * (0 - int(j))
                        deno = deno * (int(i) -int(j))
                s += args[i] * terms * inv(deno, mod)
                s %= mod
        return s

def remove(list:list, element):
        for i in list:
                if i == element:
                        list.remove(i)


d = {
    '1': 150550125355646,
    '2': 944474507418938,
    '3': 110040335185999,
    '4': 676042268761809,
    '5': 193274108888331,
    '6': 904128547609081,
    '7': 354197665334455,
    '8': 416432161112962,
    '9': 283942097426448
}


C = list(combinations([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
num = [1,2,3,4,5,6,7,8,9]
list = list()
for i in C:
        dic = dict()
        for j in range(5):
                dic[str(i[j])] = d[str(i[j])]
        print(i)
        print(TSSS(1125899906900597, **dic))
        list.append(TSSS(1125899906900597, **dic))
        print()
        if (TSSS(1125899906900597, **dic) == 516971327093293):
                for j in range(5):
                        remove(num,i[j])
print(num)

print(list)
dict_num = {}
for item in list:
    if item not in dict_num.keys():
        dict_num[item] = list.count(item)

import operator
sorted(dict_num.items(),key=operator.itemgetter(1))

print (dict_num)