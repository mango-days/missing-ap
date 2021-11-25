# note : works for more than 1 missing values
ap = [ 2, 8, 6, 10, 14 ]
sum_of_ap = sum ( ap )

def hcf(a,b):
    if (a==0) and (b==0): return 0
    if (a==0): return b
    if (b==0): return a
    if (a<0) and (b<0) : print("error")
    if (a==b): return a
    if (a>b): return hcf(a-b,b)
    if (a<b): return hcf(a,b-a)
    
d = hcf ( min ( ap ) , max ( ap ) )
a = min ( ap )
for index in range ( a , (len(ap)+1)*d + 1, d ) :
    if index not in ap : print ( index )