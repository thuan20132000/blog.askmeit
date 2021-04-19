
from .models import ReadingTopic, ReadingPost
from faker import Faker
from reading.helper import log_message
import random
import concurrent
import time


fake = Faker()


def gen_topics():
    topic_list = [
        {
            "name": "Điện",
            "slug": "dien-dien-tu",
        },
        {
            "name": "Khoá",
            "slug": "khoa",
        },
        {
            "name": "Giao hàng",
            "slug": "giao-hang",
        },
        {
            "name": "Y tế",
            "slug": "y-te",
        },
        {
            "name": "Nội thất",
            "slug": "noi-that",
        },
        {
            "name": "Xây dựng",
            "slug": "xay-dung",
        },
    ]

    try:

        for c in topic_list:
            topic = ReadingTopic()
            topic.name = c.get('name')
            topic.slug = c.get('slug')
            topic.save()
            
        message = f'Success: gen_category'
        log_message(message)

    except Exception as e:
        message = f'Error: {e}'
        print(message)
        log_message(message)



def gen_readingpost(number):
    try:
        topic = ReadingTopic.objects.all()
        # random_items = random.sample(cat,6)
        for i in range(number):
            post = ReadingPost()
            post.title = fake.name()
            post.slug = fake.slug()
            post.content = fake.paragraph(nb_sentences=5)
            post.reading_topic = random.choice(topic)
            post.save()
        message = f'Success: gen_field'
        log_message(message)
    except Exception as e:
        message = f'Error: {e}'
        print(message)
        log_message(message)
