# def modifyFibonacci(N,K,k):
#     result=k
#     for i in range(K,N):
#         x = 1
#         for j in range(0,K):
#             x *= result[(len(result)-1)-j]
#             x = x%(10**9+7)
#         result.append(x)
#         # print(x)1
#     # print(result)
#     print(result[len(result)-1],end="")
#
# if __name__ == '__main__':
#     T=int(input())
#     for t in range(0,T):
#         temp=input().split(' ')
#         N=int(temp[0])
#         K=int(temp[1])
#         temp=input().split(' ')
#         k=list()
#         for i in temp:
#             k.append(int(i))
#         print(modifyFibonacci(N,K,k))

# def modifyFibonacci(N,K,k):
#     result=k
#     x=1
#     for i in range(0,K):
#         x=x*k[i]
#     result.append(x)
#     for i in range(0,N-K):
#         # print(result[len(result)-1],result[len(result)-1-K])
#         print(len(result)-1,len(result)-1-K)
#         x = (result[len(result)-1]*result[len(result)-1])/result[len(result)-1-K]
#         x = x%(10**9+7)
#         result.append(x)
#         print(x)
#     print(result)
#     # print(result[len(result)-1]%(10**9+7))
#
# if __name__ == '__main__':
#     T=int(input())
#     for t in range(0,T):
#         temp=input().split(' ')
#         N=int(temp[0])
#         K=int(temp[1])
#         temp=input().split(' ')
#         k=list()
#         for i in temp:
#             k.append(int(i))
#         modifyFibonacci(N,K,k)

# s=[1, 2, 3, 6, 36, 648, 139968, 265173483, 322059237, 48473715]
# x=[1, 2, 3, 6, 36, 648, 139968, 265173483, 572059239, 845114970]

# if __name__ == '__main__':
zones = int(input())
size = int(input())
given = list()
for i in range(0, zones):
    x=list()
    for j in range(0, size):
        temp = input().split(' ')
        temp1 = [temp[0],int(temp[1])]
        x.append(temp1)
    given.append(x)
for i in range(0,zones*size):
    index=-1
    max=-1
    for j in range(0,zones):
        if(len(given[j])>0):
            if(given[j][0][1]>max):
                index=j
                max=given[j][0][1]
    print(given[index][0][0],given[index][0][1])
    given[index].pop(0)
