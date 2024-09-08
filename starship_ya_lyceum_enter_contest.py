def remove_duplicates(list1):
    temp = []
    for x in list1:
        if x not in temp:
            temp.append(x)
    return temp


def starship(*args, price="Hrundig"):
    answ = {}
    price = price.lower()
    print(price)
    for i in range(len(args)):
        # check_map = {}
        cur_arg = args[i][0]
        # kkk = str(len(list(set(args[i][0]) & set(price))))
        kkk = str(len(list(set(cur_arg.lower()) & set(price))))
        if kkk not in answ:
            answ[kkk] = []
            listt = answ[kkk]
            listt.append(args[i][1])
        elif kkk in answ:
            listt = answ[kkk]
            listt.append(args[i][1])
        # c_list = listt
        # listt = list(set(c_list))
        # listt = list(dict.fromkeys(c_list))
        # print(f"ЭТО LISTT :  ")
        # print(*listt)
        # answ[kkk] = remove_duplicates(listt)
        listt = remove_duplicates(listt)
        listt = sorted(listt, reverse=True)
        # print(args[i])

        # for j in range(len(args[i])):
        #     if args[i][j][0] in price:
    # kks = answ.keys()
    for i in range(10000):
        # lst = answ[kks[i]]
        if str(i) in answ:
            answ[str(i)] = sorted(answ[str(i)], reverse=True)
            answ[str(i)] = remove_duplicates(answ[str(i)])
    # answ['2'] = sorted(answ['2'], reverse=True)
    # for key, value in answ.items():
    #     value = sorted(value, reverse=True)
    return answ
