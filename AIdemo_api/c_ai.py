#coding:utf8
# a = "234567"
# b = "1234567890"
#
# c = a
# d = b
# b = c
# a = d
# print a
# print b

# import random
#
# a = random.randint(0,10)
# print a
# while 1:
#     if input() == a:
#         print "猜对了"
#         break
#     else:
#         print "再来一次"

# for i in range(28,10000):
#     s=0
#     for k in range(28,i):
#         if i%k==0:
#             s=s+k
#     if i==s:
#         print i
#
# l = [ ]
# for n in range (28,10000):
#     for a in range (28,n):
#         if n%a ==0:
#             l.append(a)
#     if sum(l)==n:
#         print l
#         print n
#     l = []

a = [1,24,5,6,45,67,32,12,4]
fla = 0
for i in range(len(a)-1):
    for j in range(len(a) - i - 1):
        print a[j],a[j+1]
        if a[j] > a[j + 1]:
            a[j],a[j+1] = a[j+1],a[j]
print a