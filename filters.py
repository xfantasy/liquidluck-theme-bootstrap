#!/usr/bin/env python


def categorist(key):
    from liquidluck.options import settings
    dct = settings.theme_variables.get('categories')
    if not isinstance(dct, dict):
        return ''
    if key not in dct:
        return ''
    return dct[key]
