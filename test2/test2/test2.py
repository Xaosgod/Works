import bs4 as bs
import urllib.request
import re
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
import numpy as np
import json2
import xml.etree.ElementTree as ET
import sys
import pickle
import requests




with open("D:/work/3.txt","r") as f:
 x=[]
 x = list(f.read())
 print (x)