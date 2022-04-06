# 筋トレツイートbot
from config import settings
import tweepy
import random


def tweet():
    # 初期設定
    client = tweepy.Client(
        consumer_key=settings.API_KEY,
        consumer_secret=settings.API_SECRET,
        access_token=settings.ACCESS_TOKEN,
        access_token_secret=settings.ACCESS_TOKEN_SECRET
    )

    # トレーニング決定
    rand_menu = random.randrange(
        0, len(settings.TRAINING)
        )


    # 筋トレメニュー決定
    training_menu = settings.TRAINING[rand_menu]

    # ツイート内容
    if training_menu == '休み':
        message = f'今日のトレーニングは{training_menu}です!'

    elif training_menu == '自転車':
        message = f'今日は{training_menu}でトレーニングしましょう!'

    elif training_menu == 'プランク':
        message = f'今日は{training_menu}を1分3セットしましょう!'

    else:
        # トレーニング回数とセット数決定
        rand_num = random.randrange(
            0, len(settings.NUM)
        )
        rand_set = random.randrange(
            1 , 3
        )
        message = f'今日は{training_menu}を{settings.NUM[rand_num]}回を{rand_set}セットしましょう!'

    # ツイート
    client.create_tweet(text=message)
