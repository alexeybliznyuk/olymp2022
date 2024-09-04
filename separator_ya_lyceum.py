def separator(data):
    sp_list = []
    sp_list = data.split(" ")
    right_list = []
    wrong_list = []
    for i in range(len(sp_list)):
        if condition(int(sp_list[i])):
            right_list.append(int(sp_list[i]))
        else:
            wrong_list.append(int(sp_list[i]))
    
    return [right_list, wrong_list]
