#!/usr/bin/env python2

from tornado import gen
from tornado.websocket import websocket_connect
from tornado.ioloop import IOLoop, PeriodicCallback
from singlemessagebot import SingleMessageBot
from json import loads
from sys import argv
import requests

hype = 2

def specifyHype():
    global hype
    hype = (hype + 1) * 3
    bot = SingleMessageBot("Hype level is now {}".format(hype))
    bot.start()

callback = PeriodicCallback(specifyHype, 86400000) # daily
callback.start()
IOLoop.instance().start()
