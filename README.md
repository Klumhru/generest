generest
========

GeneREST - create rest clients from djangorestframework models

Generest introspects django rest framework routers and outputs a rest client in the desired language

## Installation:

In a virtualenv type:

'''
pip install -e git+git@github.com:Klumhru/generest.git
'''

Add 'generest' to you django installed apps

## Usage

Use the django manage.py command to generate rest clients

'''
./manage.py generest app1 [app2...] --lang=cs
'''
