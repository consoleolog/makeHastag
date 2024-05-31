import time
import uuid
import urllib.request
from instagrapi import Client
from multiprocessing.dummy import Pool as ThreadPool
def crawler(hashtag_word):
    cl = Client()
    # cl.set_proxy('http://127.0.0.1')
    cl.login(
'
    )
    time.sleep(3)

    hashtag_medias_top = cl.hashtag_medias_v1(name=hashtag_word, amount=1000, tab_key='top')

    for i in range(0, len(hashtag_medias_top)):
        time.sleep(3)

        text = hashtag_medias_top[i].dict()

        pk = text['pk']
        post_id = text['id']

        username = text['user']['username']

        comment_count = text['comment_count']

        like_count = text['like_count']
        post = open('./data/post.csv','a',encoding='utf-8')
        post.write(f'\n{str(pk)},{str(post_id)},{str(like_count)},{str(comment_count)},{str(hashtag_word)},{str(username)}')
        post.close()


        image_list = []
        for j in range(0, len(text['resources'])):
            image_list.append(str(text['resources'][j]['thumbnail_url']))

        for k, data in enumerate(image_list):
            filename = uuid.uuid4()
            filename: str = str(filename)
            image = open('./data/image.csv','a')
            image.write(f'\n{str(pk)},{str(post_id)},{filename}')
            urllib.request.urlretrieve(data, f'./image_all/{filename}.jpg')
            image.close()
        time.sleep(3)
        user_csv = open('./data/user.csv','a')
        user = cl.user_info_by_username(username)
        user_data = user.dict()
        follower_count = user_data['follower_count']
        following_count = user_data['following_count']
        user_csv.write(f'\n{str(username)},{str(follower_count)},{str(following_count)}')
        user_csv.close()

hashtags = [
    "love", "instagood", "fashion", "photooftheday", "photography", "art", "beautiful", "art", "nature",
    "picoftheday", "happy", "follow", "travel", "cute", "style", "instadaily", "tbt", "followme", "summer",
    "beauty", "fitness", "like4like", "food", "instalike", "photo", "selfie", "friends", "music", "smile", "family",
    "life", "fun", "girl", "likeforlikes", "motivation", "lifestyle", "likeforlike", "sunset", "amazing", "nofilter",
    "instamood", "sun", "follow4follow", "inspiration", "followforfollow", "instapic", "bestofheday", "cool",
    "swag", "night", "photograhy", "smallbusiness", "business", "entrepreneur", "socialmedia", "digitalmarketing",
    "sales",
    "tech", "leadership", "innovation", "networking", "SEO", "contentmarketing", "marketingstrategy", "businesstips",
    "startups",
    "productivity", "strategy", "b2b", "consulting", "workplace", "professionaldevelopment", "leadgeneration",
    "b2bmarketing", "sass",
    "thoughtleadership"
]
hashtag_list = list(set(hashtags))

pool = ThreadPool(processes=4)
result = pool.map(crawler, hashtag_list)
pool.close()
pool.join()