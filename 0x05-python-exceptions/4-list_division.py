#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    my_list_3 = []
    for i in range(list_length):
        try:
            my_list_3.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            my_list_3.append(0)
        except ZeroDivisionError:
            print("division by 0")
            my_list_3.append(0)
        except IndexError:
            print("out of range")
            my_list_3.append(0)
        finally:
            pass
    return my_list_3
