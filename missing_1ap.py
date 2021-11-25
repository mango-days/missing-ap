# note : works for not more than 1 missing value
ap = [ 2, 8, 6, 10, 12 ]
a = min ( ap )
l = max ( ap )
n = len ( ap ) + 1
sum_ap = ( n / 2 ) * ( a + l )
missing_value = sum_ap - sum ( ap )
print ( int ( missing_value ) )