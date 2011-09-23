# -*- coding: utf8 -*-
from nose.tools import eq_

from packager.main import _slugify


def test_slugify():
    def check(string, expected):
        eq_(_slugify(string), expected)
    eq_(' Jack & Jill like numbers 1,2,3 and 4 and silly characters ?%.$!/_',
        'jack--jill-like-numbers-123-and-4-and-silly-characters-_')
    eq_(u"Un \xe9l\xe9phant \xe0 l'or\xe9e du bois",
        u'un-\xe9l\xe9phant-\xe0-lor\xe9e-du-bois')
    check('版本历史记录', 'addon')
    check('版本历史记录boop版', 'boop')
