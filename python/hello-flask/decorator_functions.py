# import time

# python decorator function
# def delay_decorator (function):
#   def wrapper_function():
#     time.sleep(2)
#     function()
#     function()
  
#   return wrapper_function

# @delay_decorator
# def say_hello():
#   print('Hello')

# @delay_decorator
# def say_bye():
#   print('Bye')

# def say_greeting():
#   print('How are you?')

# # say_hello()
# greet = delay_decorator(say_greeting)
# greet()

# def speed_calc_decorator(function):
#   def wrapper_function():
#     start_time = time.time()
#     function()
#     end_time = time.time()
#     print(f'{function.__name__} run speed: {end_time - start_time}s')
  
#   return wrapper_function

# @speed_calc_decorator
# def fast_function():
#   for i in range(10):
#     i + i

# @speed_calc_decorator
# def slow_function():
#   for i in range(15):
#     i + i


class User:
  def __init__(self, name):
    self.name = name;
    self.is_logged_in = False

def is_authenticated_decorator(function):
  def wrapper_func(*args, **kwargs):
    if args[0].is_logged_in == True:
      function(args[0])
  return wrapper_func


@is_authenticated_decorator
def create_blog_post(user):
  print(f"This is {user.name}'s new blog post.")

new_user = User('Jamal')
new_user.is_logged_in = True
create_blog_post(new_user);