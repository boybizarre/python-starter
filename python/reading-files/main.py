file_path = "/Users/heyjamal/Downloads/python/reading-files/my_file.txt"

# with open(file_path) as file:
#     contents = file.read()
#     print(contents)

# with open(file_path, 'a') as file:
#     file.write('\nHello world!')


with open("new_text.txt", "w") as file:
    file.write("\nHello world!")

# import os

# Print the current working directory
# print("Current Working Directory:", os.getcwd())
