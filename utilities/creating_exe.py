import os, sys , datetime, binascii
from hashlib import pbkdf2_hmac


myEndtime = datetime.datetime(2020, 5, 1, 0, 0).timestamp()
myStartime = datetime.datetime(2020, 4, 1, 0, 0).timestamp()

# with open('mytunelic.txt', 'wb') as licfile:
#     dk = pbkdf2_hmac(bytes(str(myStartime)))
#     licence_time_key = binascii.hexlify(dk)
#     licfile.write(licence_time_key)

def executable_creator():
    command = 'pyinstaller -D '
    addata = '--add-data="exe/ffmpeg.exe;exe" --add-data="exe/ffplay.exe;exe"\
                                --add-data="exe/ffprobe.exe;exe"  \
                                --add-data="resources/gif/music1.gif;gif" --icon resources/icons/cuffie.ico'
    program = ' .\mytunefy.py'

    fullcommand = command + addata + program
    os.system(fullcommand)

def key_creator(address):
    mymac = address.lower()
    mycormac = mymac.replace('-', ':')
    mac_address = bytes(mycormac, 'utf8')
    dk = pbkdf2_hmac('sha256', mac_address, b'salt', 100000)
    key_bin = binascii.hexlify(dk)

    return key_bin, mycormac