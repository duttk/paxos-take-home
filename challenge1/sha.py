"""This module exposes an API to convert a string to its SHA256 hash """

import hashlib
import hug
import falcon

MESSAGES = {}


@hug.get('/messages/{digest}')
def get_message(digest: str, response):
    """
    Return the message associated with the digest if exists else return 404
    """

    if digest not in MESSAGES:
        response.status = falcon.HTTP_404
        return {'err_msg': 'Message not found'}

    return {'message': MESSAGES.get(digest)}


@hug.post('/messages')
def post_message(message: str, response):
    """
    Return the SHA256 hash digest of the message, return 409 if it already exists
    """

    if message in MESSAGES.values():
        response.status = falcon.HTTP_409
        return {'err_msg': 'Message already exists'}

    encoded_message = message.encode('utf-8')
    digest = hashlib.sha256(encoded_message).hexdigest()
    MESSAGES[digest] = message

    return {'digest': digest}
