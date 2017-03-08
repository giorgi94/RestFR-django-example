import random
import requests

from string import ascii_lowercase as al
from string import ascii_uppercase as uc
from string import digits as dg

def get_set():
	temp = [x for x in al + uc + dg]
	random.shuffle(temp)
	return temp

def generate_token():
	token = ''.join([random.choice(get_set()) for x in range(random.randint(30, 35))])
	return token

def unique_token(tk, tokens):
	if tk in tokens:
		tk = generate_token()
		return unique_token(tk, tokens)
	else:
		return tk
