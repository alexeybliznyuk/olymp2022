class Bell:
    def __init__(self, *sm, **args):

        self.flagg = 0
        self.smm = sm
        self.args = dict(sorted(args.items()))

    def print_info(self):
        count = 0
        for var_name, inf in self.args.items():

            print(f"{var_name}: {inf}", end="")
            # print(len(self.args))
            count += 1
            if count != len(self.args):
                print(", ", end="")

        if len(self.args) > 0 and len(self.smm) > 0:
            print("; ", end="")
        cnt = 0
        for vaar in self.smm:
            print(vaar, end="")
            cnt += 1
            if cnt != len(self.smm):
                print(", ", end="")
        # for i in self.args:
        #     print(i)
        if len(self.args) == 0 and len(self.smm) == 0:
            print("-")
        else:
            print()


class LittleBell(Bell):
    def __str__(self):
        return "ding"

    def sound(self):
        print("ding")


class BigBell(Bell):
    # def __init__(self):
    # self.flagg = 0
    def __str__(self):
        if self.flagg == 0:
            self.flagg = 1
            return "ding"
        else:
            self.flagg = 0
            return "dong"

    def sound(self):
        if self.flagg == 0:
            self.flagg = 1
            print("ding")
        else:
            self.flagg = 0
            print("dong")


class BellTower:
    def __init__(self, *args):
        self.bell_list = []
        for i in range(len(args)):
            self.bell_list.append(args[i])

        # self.bell_list = list(*args)
        # print(self.bell_list[0], self.bell_list[0])
        self.flg = 0

    def append(self, nb):
        self.bell_list.append(nb)

    def sound(self):
        # print("qwe")
        # print(len(self.bell_list))
        for i in range(len(self.bell_list)):
            # print(self.bell_list[i])
            # print(type(self.bell_list[i]))
            # if str(self.bell_list[i]) == "sb":
            #     print("ding")
            # elif str(self.bell_list[i]) == "bb":
            #     if self.flg == 0:
            #         print("ding")
            #         self.flg = 1
            #     elif self.flg == 1:
            #         print("dong")
            print(self.bell_list[i])
        print("...")


# qwe = BellTower(LittleBell(), LittleBell())
# qwe.sound()


# Bell("бронзовый").print_info()
# LittleBell("медный", нота="ля").print_info()
# BigBell(название="Корноухий", вес="1275 пудов").print_info()


