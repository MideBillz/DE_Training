# #Keyword arguments (*kwargs)
#
# def main():
#     kitten(Buffy = 'meow', Mount = 'everest', Ride = 'or die')
#
#     # x = dict(Buffy = 'meow', Mount = 'everest', Ride = 'or die')
#     # kitten(**x) It can also be used this way
#
# def kitten(**kwargs):
#     if len (kwargs):
#         for k in kwargs:
#             print('Kitten {} says {}'.format(k, kwargs[k]))
#     else: print('no keyword')
#

# def main():
#      x = kitten()
#      print(type(x), x)
#
# def kitten():
#     print('Meow.')
#     return dict(w = 1, x = 2, y = 3, z = 4,)
#
#

# def main():
#     for i in inclusive_range(3, 25, 2):
#         print (i, end = ' ')
#     print()
#
# def inclusive_range(*args):
#     numargs = len(args)
#     start = 0
#     step = 1
#
#     #initialize parameters
#     if numargs < 1:
#         raise TypeError(f'expected: at least 1 argument, got {numargs}')
#     elif numargs == 1:
#         stop = args[0]
#     elif numargs == 2:
#         (start, stop) = args
#     elif numargs == 3:
#         (start, stop, step) = args
#     else: raise TypeError(f'expected: at most 3 arguments, got {numargs}')
#
#     #generator
#     i = start
#     while i <= stop:
#         yield i
#         i += step
#
#Note: Everything in python is an object, even a function is a type of object

# def f1():
#     print('This is f1')
#
# x = f1
# x()

# def f1(f):
#     def f2():
#         print('This is before the function call')
#         f()
#         print('This is after the function call')
#     return f2
#
# def f3():
#     print('This is f3')
#
# x = f1(f3)
# x() # To be reviewed

# def main():
#     a = set("We're gonna need a bigger boat.")
#     b = set("Sorry Dave, can't do that.")
#     print_set(sorted(a))
#     print_set(sorted(b))
#
# def print_set(o):
#     print('{', end = '')
#     for x in o: print(x, end ='')
#     print('}')
#

# def main():
#     seq = range(1, 11)
#     print_list(seq)
#
# def print_list(o):
#     for x in o: print(x, end=' ')
#     print()
#
# if __name__ == '__main__': main()