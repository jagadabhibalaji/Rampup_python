user_info = {
    'username': 'Balaji',
    'email': 'google@gmail.com',
    'location': 'Bangalore',
    'age': 23
}
print(f"Original user information :{user_info}")
new = {
    'email': 'balaji@gmail.com',
    'age': 25
}
user_info.update(new)
print(f"Updated user information :{user_info}")






# def update_user_profile(user_profile, new_data):
#     user_profile.update(new_data)
#
# user_profile = {
#     'username': 'johndoe',
#     'email': 'johndoe@example.com',
#     'age': 30
# }
#
# new_data = {
#     'email': 'john.doe@example.com',
#     'location': 'New York'
# }
#
# update_user_profile(user_profile, new_data)
#
# print(user_profile)
