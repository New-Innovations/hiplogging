Hiplogging
==========

With Hiplogging, you can keep using the standard python [logging](https://docs.python.org/2/library/logging.html) module, *and* have the important log messages in HipChat, where they might actually reach you :)


Installation
--------

Execute:

```bash
sudo python setup.py install
```

or, from pip
```bash
sudo pip install hiplogging
```


Example
--------

Here’s how you use this. In bash:
```bash
export HIPCHAT_ADMIN_TOKEN=”ABCDEF”
export HIPCHAT_ROOM=’HelloWorld’
```

You can an admin token from [this link](https://<YOUR_HIPCHAT_NAME>.hipchat.com/admin/api).

Then, in the sweet code:

```python
import os
import logging
import hiplogging

# Set up a standard logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

# Add the hipchat handler
# Get an admin token from: https://<YOUR_HIPCHAT_NAME>.hipchat.com/admin/api
handler = hiplogging.HipChatHandler(os.environ['HIPCHAT_ADMIN_TOKEN'],
                                   os.environ['HIPCHAT_ROOM'])
handler.setLevel(logging.DEBUG)
logger.addHandler(handler)

# Try it out: messages will be visible both in the console and on hipchat.
logger.debug('debug - we are approaching the anomaly')
logger.info('info - shields up, red alert!')
logger.warn('warn - shield down to 15%')
logger.fatal('fatal - what shields?')
```

## This is what you get
![This is what you get](example.png)

