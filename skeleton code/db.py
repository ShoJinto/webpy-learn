#!/usr/bin/env python
# coding: utf-8

import config


def listing(**k):
    return config.db.select('items', **k)
