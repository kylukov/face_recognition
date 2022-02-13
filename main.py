import vk_api
import wget

vk_session = vk_api.VkApi('+79258371444', 'Nagornaya1')
vk_session.auth()

vk = vk_session.get_api()


def get_user_city(user_id):
    user = vk_session.method('users.get', {'user_ids': {user_id}, "fields": 'city'})
    return str(user)[str(user).find("city"):]


def get_user_photo(user_id):
    """Downloading avatar photo from vk user"""
    photo = vk_session.method('users.get', {'user_ids': {user_id}, "fields": 'photo_400_orig'})
    users_photo = photo[0]['photo_400_orig']
    wget.download(users_photo)


def get_username(user_id):
    """Get first and second name of user"""
    user = vk_session.method("users.get", {"user_ids": {user_id}})
    fullname = user[0]['first_name'] +  ' ' + user[0]['last_name']
    return fullname


def get_friend(user_id):
    """Get friends ids list"""
    friends = vk_session.method('friends.get', {"user_id": user_id})
    users = open("BabyFile.txt", "w")
    for friend in friends['items']:
        user_info = vk_session.method('users.get', {'user_ids': friend})
        users.write(f"{user_info[0]['id']}\n")


def get_info():
    city = 'Дубна'
    userid = '269944728'
    if str(get_user_city(userid)).find(city) != 0:
        print(f"Пользователь: {get_username(userid)} ", f"Правда проживает в городе: {city}", "is", True)
    else:
        print(f"Пользователь: {get_username(userid)} ", f"Правда проживает в городе: {city}", "is", False)
    get_friend(userid)


def get_all_photos():
    f = open('BabyFile.txt', 'r')
    array = []
    for line in f:
        array.append(line[:-1])

    for i in range(len(array)):
        get_user_photo(str(array[i]))


def main():
    get_all_photos()



if __name__ == '__main__':
    main()
