import time
import uuid
import urllib.request
from instagrapi import Client
from multiprocessing.dummy import Pool as ThreadPool
from functools import partial



def crawler(hashtag_word, cl):
    time.sleep(3)

    hashtag_medias_top = cl.hashtag_medias_top_v1(name=hashtag_word, amount=1000, tab_key='top')

    for i in range(0, len(hashtag_medias_top)):
        time.sleep(3)

        text = hashtag_medias_top[i].dict()

        pk = text['pk']
        post_id = text['id']

        username = text['user']['username']

        comment_count = text['comment_count']

        like_count = text['like_count']

        image_list = []
        for j in range(0, len(text['resources'])):
            image_list.append(str(text['resources'][j]['thumbnail_url']))

        for k, data in enumerate(image_list):
            filename = uuid.uuid4()
            filename: str = str(filename)

            urllib.request.urlretrieve(data, f'./image_all/{filename}.jpg')

        time.sleep(3)

        user = cl.user_info_by_username(username)
        user_data = user.dict()
        follower_count = user_data['follower_count']
        following_count = user_data['following_count']




