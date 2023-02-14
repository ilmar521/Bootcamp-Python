def get_full_name(first_name='', middle_name='', last_name=''):
    if middle_name == '':
        print(first_name + " " + last_name)
    else:
        print(first_name + " " + middle_name + " " + last_name)


get_full_name(first_name="john", middle_name="hooker", last_name="lee")
get_full_name(first_name="bruce", last_name="lee")
