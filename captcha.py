# encoding: utf-8

import random


def gen_4byte_captcha():
    """
    Generate 4 byte captcha
    """
    return ''.join(map(str, random.sample([0, 1, 2, 3, 5, 6, 7, 8, 9], 4)))


def gen_6byte_captcha():
    """
    Generate 6 byte captcha
    """
    return ''.join(map(str, random.sample([0, 1, 2, 3, 5, 6, 7, 8, 9], 6)))
