def doubler (f):
    def g(x):
        return 2 * f(x)
    return g

def some_func_with_one_arg(x):
    return x*7

dbl_one_arg=doubler(some_func_with_one_arg)

print dbl_one_arg(2) #14 *2 =28

def double_for_multiple(f):
    def g(*args, **kwargs):
        return 2 * f(*args, **kwargs)
    return g

def some_func_with_mult_arguments(x,y,z):
    return x+y+z

dbl_mult_arg=double_for_multiple(some_func_with_mult_arguments)

print dbl_mult_arg(1,2,3) # 6 *2 =12


def print_args(*args, **kwargs):
    print ("args", args)
    print ("Kwargs", kwargs)

print_args(1,2,3, key="arun", value="somevalue")





