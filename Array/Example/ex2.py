# input
# 4
# 1 2 3 4
# 1 10

# output
# 1 10 2 3 4

# JS
# var a = [1, 2, 3, 4]
# var n = 4
# var k = 1
# var x =10

# for(var i = n; i >= k+1; i--){
#   a[i] = a[i-1];
#   console.log(a)
# }

n = int(input())

tempAr = []
for i in range(n):
    tempAr.append(input())

k = int(input())
x = input()
tempAr.insert(k, x)
print(' '.join(tempAr))