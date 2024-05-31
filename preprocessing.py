import os
import shutil
import pandas as pd
import numpy as np
# 일단 판다스 데이터 프레임을 어떻게 저장해야하나면

# os.mkdir('./image_all')
# os.mkdir('./data')
post_data = open('./data/post.csv','w')
# 이미지 이름이 필요하고 해시태그들이 필요한데
# 이미지 이름 해시태그 하나 pk post_id 이미지 이름이 왜래키면 되지않을까
# post_data.write('pk,post_id,like_count,comment_count,hashtag,username')
# post_data.close()
#
# hashtag = open('./data/hashtag.csv','w')
# hashtag.write('pk,post_id, hashtag')
# hashtag.close()
#
# user = open('./data/user.csv','w')
# user.write('username,follower_count, following_count')
# user.close()
#
# image = open('./data/image.csv','w')
# image.write('pk,post_id,filename')
# exit()
# # 해시태그 저장은 미루고 해시태그에 따라
# post = pd.read_csv('./data/post_data.csv',encoding='utf-8')
# hashtag = pd.read_csv('./data/hashtag.csv', encoding='utf-8')
#
# result = pd.merge(left=post, right=hashtag, how='inner', on=['pk','post_id'])

# 그리고 반목문을 돌려야됨
os.mkdir('./dataset')
# for filename in os.listdir('./image_all'):
#     print(filename)
#     row = result[result['image_name'] == filename]
#     if not row.empty:
#         print("")
#         # 해시태그를 봐야되는거임
#         a = row['hashtag']
#         if not os.path.exists(f'./dataset/{a}'):
#             os.mkdir(f'./dataset/{a}')
#         shutil.copy(f'./image_all/{filename}',f'./dataset/{a}/{filename}')


