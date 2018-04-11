import hashlib
import random

from django.shortcuts import render

from .models import myUsers, loginTokens



def hashPasswordFunction(request, raw_password):

	encoded_password = (raw_password).encode('utf-8')
	h = hashlib.md5()
	h.update(encoded_password)
	hashed_password = h.hexdigest()

	return (hashed_password)

# generate login token

def generateLoginTokenFunction(request, userSlug):

	generateLoginTokenLoop = True

	while generateLoginTokenLoop == True:

		generateLoginTokenFrom = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		login_token_length = 26
		theLoginToken = ""

		for i in range(login_token_length):
			next_index = random.randrange(len(generateLoginTokenFrom))
			theLoginToken = theLoginToken + generateLoginTokenFrom[next_index]

		checkLoginToken = loginTokens.objects.filter(loginToken=theLoginToken).count()
		if checkLoginToken == 0:
			generateLoginTokenLoop = False
			break
		else:
			generateLoginTokenLoop = True

	theUserInstance = myUsers.objects.get(slug=userSlug)

	loginTokens.objects.filter(user=theUserInstance, active=True).update(active=False)
	loginTokens.objects.create(loginToken=theLoginToken, user=theUserInstance)
	myUsers.objects.filter(slug=userSlug).update(currentToken=theLoginToken)	

	return (theLoginToken)