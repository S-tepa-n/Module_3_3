# 1
def print_params(a=1, b='string', c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
print()
# 2
values_list = (12, 'hello', True)
values_dict = {'a': 2, 'b': 'world', 'c': True}
print_params(*values_list)
print_params(**values_dict)
print()
# 3
values_list_2 = (54.32,'string')
print_params(*values_list_2, 42)
