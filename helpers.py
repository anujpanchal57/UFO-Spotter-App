import requests
from flask import redirect, render_template, request
from pymongo import MongoClient

client = MongoClient('mongodb+srv://anujpanchal57:heenaanuj53@dev-community-cluster.qazlv.mongodb.net/?retryWrites=true&w=majority')

def get_count(city, state):
   """Count the UFO sightings for that city and state"""


   city_count = list(client['ufos']['ufos'].aggregate([
       {
           '$match': {
               'city':  city
           }
       }, {
           '$match': {
               'state': state
           }
       }, {
           '$count': 'ufo_count'
       }
   ]))


   return city_count


def get_ufos(city, state):
   """Gets report of UFO sightings for that city and state"""


   recent_ufos = list(client['ufos']['ufos'].aggregate([
       {
           '$match': {
               'city': city
           }
       }, {
           '$match': {
               'state': state
           }
       }, {
           '$sort': {
               'datetime': -1
           }
       },
   ]))


   return recent_ufos