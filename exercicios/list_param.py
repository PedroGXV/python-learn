

def list_param(*list):
    count = 0
    for item in list:
        count += 1
        print(f'item n°{count} = {item}')

list_param(12, 'teste', 0, [45, 55])