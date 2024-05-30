from instagrapi import Client
from multiprocessing.dummy import Pool as ThreadPool
from crawler import crawler
from functools import partial

hashtag_list = ['일상','학생','직장인','여행']
hashtags = [
    "love", "instagood", "fashion", "photooftheday", "photography", "art", "beautiful", "art", "nature",
    "picoftheday", "happy", "follow", "travel", "cute", "style", "instadaily", "tbt", "followme", "summer",
    "beauty", "fitness", "like4like", "food", "instalike", "photo", "selfie", "friends", "music", "smile", "family",
    "life", "fun", "girl", "likeforlikes", "motivation", "lifestyle", "likeforlike", "sunset", "amazing", "nofilter",
    "instamood", "sun", "follow4follow", "inspiration", "followforfollow", "instapic", "bestofheday", "cool",
    "swag", "night", "happybirthday"
]

settings = {

    'user-agent': ''
}
cl = Client()
cl.login(

)
partial_crawler = partial(crawler, cl=cl)

pool = ThreadPool(processes=4)
result = pool.map(partial_crawler, hashtag_list)
pool.close()
pool.join()