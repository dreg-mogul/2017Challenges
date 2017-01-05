array1 = [2,3,4,2,3,5,4,6,4,6,9,10,9,8,7,8,10,7]
array2 = [2,'a','l',3,'l',4,'k',2,3,4,'a',6,'c',4,'m',6,'m','k',9,10,9,8,7,8,10,7]

def test(str):
 r = [x for x in str if str.count(x) == 1]
 for x in r: print(x)

test(array1)
test(array2)
