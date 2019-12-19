#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set()
    for a in set_1:
        if not a in set_2:
            set_3.add(a)
    for a in set_2:
        if not a in set_3:
            set_3.add(a)
    return set_3
