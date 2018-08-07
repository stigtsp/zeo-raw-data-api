# Imports
from ZeoRawData.BaseLink import BaseLink
from ZeoRawData.Parser import Parser

# Initialize
link = BaseLink("/dev/tty.usbserial-FTHBZZ4L")
parser = Parser()

# Add the Parser to the BaseLink's callback
link.addCallback(parser.update)

# Add your callback functions

def linkCallbackDebug(timestamp, timestamp_subsec, version, data):
    print("timestamp {0}, subsec {1}, version {2}, data {3}\n".format(timestamp, timestamp_subsec, version, data))

#link.addCallback(linkCallbackDebug)

def foo(a):
    print(a)


parser.addEventCallback(foo)
parser.addSliceCallback(foo)

# Start link
link.start()
while 1:
    pass

