from random import randint

# def max1(n1, n2, n3):
#     rn = n1
#     if n2 > rn:
#         rn = n2
#     elif n3 > rn:
#         rn = n3
#     # return rn


def maximum(nlst):
    nnlst = nlst[0]
    for i in range(1, len(nlst)):
        if nlst[i] > nnlst:
            nnlst = nlst[i]
    return nnlst


def minimum(nlst):
    nnlst = nlst[0]
    for i in range(1, len(nlst)):
        if nlst[i] < nnlst:
            nnlst = nlst[i]
    return nnlst


lst = [randint(1, 20) for i in range(10)]


def sort(lst):
    new_lst1 = []
    while lst:
        new_lst1.append(minimum(lst))
        lst.remove(minimum(lst))
    return new_lst1


print(lst)

print(minimum(lst))

print(set(sort(lst)))
