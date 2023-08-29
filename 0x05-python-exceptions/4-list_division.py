#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(0, list_length):
        number = 0
        try:
            number = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            continue
        except (ValueError, TypeError):
            print("wrong type")
            continue
        except IndexError:
            print("out of range")
            continue
        finally:
            result.append(number)
    return result
