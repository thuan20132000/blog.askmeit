
from firebase_admin import messaging
from firebase_admin import credentials
import firebase_admin
import local_config


cred = credentials.Certificate(local_config.PATH_WORK_DIR+'/fcm_key.json')


class Notification:

    firebase_admin.initialize_app(cred)

    def send_to_topic(self, topic, title, body,vocabulary_id,vocabulary):
        # [START send_to_topic]
        # The topic name can be optionally prefixed with "/topics/".

        # See documentation on defining a message payload.
        message = messaging.Message(
            data={
                "ID": vocabulary_id,
                "name": "thinking",
                "word_type": "adjective"
            },
            notification=messaging.Notification(
                title=title,
                body=body
            ),
            topic=topic,
        )

        # Send a message to the devices subscribed to the provided topic.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
        # [END send_to_topic]


    def send_daily_vocabulary(self,vocabulary,vocabulary_type,vocabulary_id,body=None):
        # [START send_to_topic]
        # The topic name can be optionally prefixed with "/topics/".

        # See documentation on defining a message payload.
        message = messaging.Message(
            data={
                "ID": vocabulary_id,
                "name": vocabulary,
                "word_type": vocabulary_type
            },
            notification=messaging.Notification(
                title=vocabulary,
                body=body
            ),
            topic='daily_vocabulary',
        )

        # Send a message to the devices subscribed to the provided topic.
        response = messaging.send(message)
        # Response is a message ID string.
        print('Successfully sent message:', response)
        # [END send_to_topic]


    def send_practice(self,title,body):
        message = messaging.Message(
            notification=messaging.Notification(title=title,body=body),
            topic='practice'
        )

        response = messaging.send(message)
        print('Successfully sent message:', response)
