
# FileNotFound
# with open('a_file.txt') as file:
#     file.read()

# KeyError
# a_dictionary = { "key": "value"}

# value = a_dictionary["non_existent_key"]

# IndexError
# fruit_list = ['Apple', 'Banna', 'Pear']
# fruit = fruit_list[3]

# TypeError
# text = 'abc'
# print(text + 5)

# try:
#     file = open('a_text.txt')
#     dict = { "key": "value" }
#     value = dict['key']
# except FileNotFoundError:
#     # print('There was an error!')
#     file = open('a_text.txt', 'w')
#     file.write('Something')
# except KeyError as error_message:
#     print(f'That key {error_message} does not exist!')
# else:
#     content = file.read()
#     print(content)
# finally:
#     # file.close()
#     # print('File was closed!')
#     raise TypeError('This is an error that I made up')

# height = float(input('Height: '))
# weight = int(input('Weight: '))

# if height > 3:
#     raise ValueError('Human height should not be over 3 meters')

# bmi = weight / height ** 2
# print(bmi)

fruits = ['Apple', 'Banana', 'Orange']

def make_pie(index):
    try: 
        fruit = fruits[index]
    except IndexError:
        print('Fruit Pie')
    else:
        print(fruit + ' pie')

make_pie(4) # raises index error on list with less than 5 items

facebook_posts = []

total_likes = 0

for posts in facebook_posts:
    try:
        total_likes = total_likes + posts['Likes']
    except KeyError:
        pass

print(total_likes)
