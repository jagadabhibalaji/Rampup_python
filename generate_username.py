import random
import string

users = set()

length = 8
characters = string.ascii_letters + string.digits
def generate_unique_username():
    while len(users) < 10:
        # username = ''.join(random.choice(characters) for i in range(length))
        username_chars = [random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in
                          range(length)]
        username = ''.join(username_chars)

        if username not in users:
            users.add(username)
            yield username

obj=generate_unique_username()
for i in obj:
    print("unique username :",i)
