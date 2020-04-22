import json
import logging
import random
import requests
import string

config_file = 'config.json'
host = 'http://localhost:8000'
letters = string.ascii_lowercase
logging.basicConfig(filename="bot.log", level=logging.INFO, filemode="w")
file = open(config_file, 'r')
config = json.load(file)
user_count = config.get('number_of_users', 1)
max_posts_per_user = config.get('max_posts_per_user', 1)
max_likes_per_user = config.get('max_likes_per_user', 1)
users = []


def random_str(str_len):
    return ''.join(random.choice(letters) for i in range(str_len))


def create_header(login_data):
    access = login_data.get('access')
    return {'Authorization': f'Bearer {access}'}


def user_create_posts(login_data):
    headers = create_header(login_data)
    post_count = random.randrange(max_posts_per_user)
    for i in range(post_count):
        post_data = {'title': random_str(20),
                     'text': random_str(100)}
        response_post = requests.post(url=host + '/post/list/', data=post_data, headers=headers)
        if response_post.status_code == 201:
            logging.info(response_post.text)
        else:
            exit(0)


def main():
    for i in range(user_count):
        email = '%s@gmail.com' % random_str(10)
        password = random_str(6)
        user_data = {'email': email,
                     'first_name': random_str(10),
                     'last_name': random_str(10),
                     'password': password}
        # create user
        response_singup = requests.post(url=host + '/user/sing-up/', data=user_data)
        logging.info(response_singup.text)
        if response_singup.status_code == 201:
            user_login_data = {'email': email,
                               'password': password}
            # login user
            response_login = requests.post(url=host + '/user/login/', data=user_login_data)
            logging.info(response_login.text)
            if response_login.status_code == 200:
                login_data = response_login.json()
                users.append(login_data)
                # create posts
                user_create_posts(login_data)
            else:
                exit(0)
        else:
            exit(0)

    # start create likes
    for user in users:
        headers = create_header(user)
        # get all posts
        response_post = requests.get(url=host + '/post/list/', headers=headers)
        if response_post.status_code == 200:
            user_likes_count = random.randrange(max_likes_per_user)
            post_ids = [post.get('id') for post in response_post.json()]
            random_posts = random.sample(post_ids, user_likes_count)
            for post_id in random_posts:
                like_data = {'post': post_id}
                # create new like
                response_post_like = requests.post(url=host + '/post/like/', data=like_data, headers=headers)
                logging.info(response_post_like.text)
        else:
            exit(0)


if __name__ == "__main__":
    print('Start')
    logging.info('Start')
    main()
    logging.info('Successful')
    print('Successful')
