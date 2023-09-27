def create_post():
    title = input("Enter the title of the post: ")
    content = input("Enter the content of the post: ")
    filename = r"C:\Users\JagadabhiBalaji-3303\PycharmProjects\pythonProject\projects\Rajeswari tasks\{title}.txt"
    with open(filename, "w") as file:
        file.write(content)
    print(f"'{title}' created successfully!")
def read_post():
    title = input("Enter the title of the post you want to read: ")
    filename = r"C:\Users\JagadabhiBalaji-3303\PycharmProjects\pythonProject\projects\Rajeswari tasks\{title}.txt"
    try:
        with open(filename,"r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"'{title}' not found.")
def edit_post():
    title = input("Enter the title of the post you want to edit: ")
    filename = r"C:\Users\JagadabhiBalaji-3303\PycharmProjects\pythonProject\projects\Rajeswari tasks\{title}.txt"
    try:
        with open(filename, "r") as file:
            content = file.read()
        print(f"Current content of '{title}':")
        print(content)
        old_word = input("Enter the word you want to replace: ")
        new_word = input(f"Enter the new word to replace: ")
        new_content = content.replace(old_word, new_word)
        with open(filename, "w") as file:
            file.write(new_content)
        print(new_content)
    except FileNotFoundError:
        print(f"'{title}' does not exist!")
while True:
    print("1. Create a new blog post")
    print("2. Read a blog post")
    print("3. Edit a blog post")
    print("4. Quit")
    choice = input("Enter your choice in the above options: ")
    if choice == "1":
        create_post()
    elif choice == "2":
        read_post()
    elif choice == "3":
        edit_post()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
