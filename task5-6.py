def print_even_value(inp_list,i = 0): # пятое задание
    if inp_list[i] % 2 == 0:
        print(inp_list[i])
    if i >= len(inp_list) - 1:
            return True
    return print_even_value(inp_list,i + 1)

def print_even_ind(inp_list,i = 0): # шестое задание
    if i > len(inp_list):
        return True
    if i % 2 == 0:
        print(inp_list[i])
    return print_even_ind(inp_list,i + 2)