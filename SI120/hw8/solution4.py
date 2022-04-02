def mul(X, a, b, s):
        '''
        mul(X, a, b, s) = (X-a)*(X-(a+s))*...*(X-s)
        '''
        res = 1
        for i in range(a, b + 1, s):
                if not X - i :
                        pass
                else:
                        res *= (X - i)
        print(res)
        return res


# print(mul(0,-5,-3,2))

s = [ 150550125355646, 944474507418938, 110040335185999, 676042268761809, 193274108888331, 904128547609081, 354197665334455, 416432161112962,  283942097426448] 
res = 0 
for i in range(1,10):
        res += mul(0, 1, 9, 1) // mul(i, 1, 9, 1) * s[i-1]
print(res)