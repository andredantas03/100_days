# class User:
#     def __init__(self,name):
#         self.name = name
#         self.is_authenticated = False
#
# def is_authenticated_decorator_fabric(n):
#     print(n)
#     def is_authenticated_decorator(func):
#         def wrapper(*args,**kwargs):
#             if args[0].is_authenticated == True:
#                 func(args[0])
#         return wrapper
#     return is_authenticated_decorator
#
# @is_authenticated_decorator_fabric(n=3)
# def create_a_blog_post(user):
#     print(f"This is {user.name}'s new blog post")
#
# #Quando você chama create_a_blog_post(angela), na verdade está chamando wrapper(angela).
# #O wrapper recebe *args (que contém (angela,)) e verifica args[0].is_authenticated.
#
# angela = User('angela')
# angela.is_authenticated = True
# create_a_blog_post(angela)


def logging_decorator(func):
    def wrapper(*args):
        print(f'the function has name: {func.__name__}({args})')
        result = func(*args)
        print(f'It returned: {result}')

    return wrapper



@logging_decorator
def a_function(*args):
    return sum(args)


a_function(1, 2, 3)