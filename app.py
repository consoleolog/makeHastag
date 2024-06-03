from instagrapi import Client
from multiprocessing.dummy import Pool as ThreadPool
from crawler import crawler
from functools import partial

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
    "thoughtleadership", "japan"
]
hashtag_list = list(set(hashtags))

cl = Client()

cl.login(

)

partial_crawler = partial(crawler, cl=cl)

for word in hashtag_list:
    crawler(word, cl=cl)


# except:
#     print("failed")
