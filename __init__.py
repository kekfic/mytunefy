__version__ = "0.2.0"
user_key_list = {
    "FFazio": b'73cea9c6624304ebea7b57ef2c932662a02bcfce3890d4c8a67acfbb7580a98d',
    "PVallone:": b'c426a8c3078a190c7329609836cb921650cf205abfb58e532e205e33df880ebf',
    "faust": b'16c059e15b5dd7ed5102cb98632ea3dd1007a0cf803d2b9c8cd68bfe086c5bb0',
    "CPeluso": b'a6acc3e5ce29b4e11a00252d3390bb7f925083f2c94602c9d5f6786d7a936f1e',
    "FZaino": b'a63ceb426ebd2785f8878fabcfcacce094b72f125abd7f67ef6f92782475ca2a',
    "FZaino2": b'b45013395627f9521020605cb7064310ade5788679616c471d1c0a3a9533ade2'
}

personal_key = b'6f97f66b280c5451958a6733caf0f9c80c2ca4ce8e682ddb114c7877f8bf5d67'


user_list = [personal_key, user_key_list["faust"], user_key_list["FFazio"],\
                                user_key_list["PVallone:"],user_key_list["CPeluso"] ,user_key_list["faust"],\
                                            user_key_list["FZaino"], user_key_list["FZaino2"]]

import  datetime
""" I am using the __init__.py file in the wrong way
    Sometimes it happens...
    # Todo ---- Modify here
"""
#
myEndtime = datetime.datetime(2020, 5, 1, 0, 0).timestamp()
