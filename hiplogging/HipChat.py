import requests
import json
import six

def jsonify(obj):
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, set):
        return list(obj)
    else:
        raise TypeError("Can't JSONify objects of type %s" % type(obj).__name__)

class HipChatRoom(object):
    def __init__(self, token, endpoint='https://api.hipchat.com', room=None):
        self.token = token
        self.endpoint = endpoint
        self.room = room
        self.url = self.endpoint + '/v2/room/' + room

    def notification(self, message, color=None, notify=False, format=None, sender=None):
        """
        Send a message to a room.
        """
        if not format:
            format = 'html'
        from_label = ""

        message_length = len(message)
        part_number = 0
        message_part = message[10000 * part_number :10000 * (part_number + 1)]
        while message_length > 0:
            data = {'message': message_part, 'notify': notify, 'message_format': format}
            if color:
                data['color'] = color
            if sender:
                data['from'] = sender[:64]
            self.__make_request(url=self.url + '/notification', data=data)
            part_number += 1
            message_length -= 10000




    def __make_request(self, url, data):
        headers = {'Authorization':'Bearer %s' % self.token,
                   'Content-Type':'application/json'}
        if not isinstance(data, six.string_types):
            data = json.dumps(data, default=jsonify)

        r = requests.post(url=url, data=data, headers=headers)
        print(r.text)
