def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    profile.update(user_info)
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)