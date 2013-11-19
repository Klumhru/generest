#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
generest.management.commands.generest
"""
from __future__ import unicode_literals, print_function, absolute_import

from django.core.commands import BaseCommand


class Command(BaseCommand):

    def handle(*args, **options):
        print(args, options)
