#Pattern 1
# n = int(input("Enter no. of rows: "))

# for i in range (n):
#     for j in range (1,n+1):
#         print(j, end="")

#     for k in range (n,0,-1):
#         print(k, end="")
#     print()

#Pattern 2
# for k in range (3):
#     for i in range (4):
#         for j in range (1,6):
#             print(j, end ="")
#     print()

#Pattern 3
# a="ABCDE"
# for i in range (len(a),0,-1):
#     print(a[:i]) 

#Pattern 4
a="ABCDEF"
for i in range (len(a)):
    for j in range (1,len(a)):
        print(a[:i],end="")
    for k in range (len(a),0,-1):
        print(a[k:])
    print()



