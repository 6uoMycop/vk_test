import vk_api


def handler():
    code = input('Verification code ')
    return code, True


def auth_me(login, password):
    vk_session = vk_api.VkApi(login, password, auth_handler=handler)
    vk_session.auth()
    return vk_session.get_api()


# vvv EDIT THIS vvv

log_, pass_ = 'login_string', 'password_string'

# Here photos info should be placed
# example:
# https://vk.com/username?z=photo123456_8765432%2Falbum0987_0%2Frev
#                                 ^oid    ^item
items = [8765432, 0000, 0000000]  #
oid = 123456  # owner id

# ^^^ EDIT THIS ^^^

vk = auth_me(log_, pass_)

friends = vk.friends.get(user_id=13668833)
print(friends)

for it in items:
    all_likes = vk.likes.getList(type='photo', owner_id=oid, item_id=it, friends_only=0, count=1000)
    not_friends_likes = list(set(all_likes['items']) - set(friends['items']))
    # print(all_likes)
    # print(not_friends_likes)
    for like_id in not_friends_likes:  # get links for easy check
        print('https://vk.com/id' + str(like_id))
    print()
    print('--------------------------')
    print()
