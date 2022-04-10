def check(lst_classes):
    lst_check = input().split()
    for classes in lst_classes:
        if lst_check[1] == classes[0]:
            if lst_check[0] in classes[1:]:
                return "Yes"
        elif lst_check[0] == lst_check[1]:
            return "Yes"
    return "No"


def enter_classes():
    n = int(input())
    lst_classes = [input().replace(': ', '') for i in range(n)]
    lst_classes_separat = []
    for c in lst_classes:
        lst_classes_separat.append(c.split())
    for c in lst_classes_separat:
        for i in range(len(lst_classes_separat)):
            for j in range(1, len(lst_classes_separat[i])):
                if c[0] == lst_classes_separat[i][j]:
                    lst_classes_separat[i].extend(c[1:])
    return lst_classes_separat

lst_classes = enter_classes().copy()
q = int(input())
for i in range(q):
    print(check(lst_classes))

