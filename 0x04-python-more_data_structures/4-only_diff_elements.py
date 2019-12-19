#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for a in set_1:
        if a not in set_2:
            set_3.add(a)
    for a in set_2:
        if a not in set_1:
            set_3.add(a)
    return set_3
