# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import hashlib
import random

from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from django.db.models import Q
from .serializer import *
from .models import myUsers
from .functions import *


# Create your views here.

def home(request):
	template_name = 'index.html'

	context = {

	}

	return render(request, template_name, context)

class booksListClass(ListAPIView):
	serializer_class = booksListSerializer

	def get_queryset(self, *arg, **kwargs):

		queryset = AddBook.objects.all()

		return queryset





class bookDetailsClass(ListAPIView):
	serializer_class = booksListSerializer

	def get_queryset(self, *arg, **kwargs):

		bookSlug = self.request.GET.get('bookSlug', None)

		checkBook = AddBook.objects.filter(slug=bookSlug).count()
		if checkBook == 0:
			queryset = AddBook.objects.all()[:0]
		else:
			queryset = AddBook.objects.all().filter(slug=bookSlug)

		return queryset




class userRegistrationClass(APIView):

	permission_classes = []

	def get(self, request, *args, **kwargs):

		Today 		= datetime.now().date()
		currentTime = datetime.now().time()

		fname = request.GET.get('fname', None)
		mname = request.GET.get('mname', None)
		lname = request.GET.get('lname', None)
		email = request.GET.get('email', None)
		registrationNumber = request.GET.get('registrationNumber', None)
		departmentSlug     = request.GET.get('departmentSlug', None)
		password 		   = request.GET.get('password', None)
		confirmPassword    = request.GET.get('confirmPassword', None)

		if password != confirmPassword:
			return Response([{"result": "0", "success": "", "error": "The passwords don't match. Please check your password and try again!"}])
		else:
			hashedPassword = hashPasswordFunction(request, password)

			checkDepartment = Depatment.objects.filter(slug=departmentSlug).count()
			if checkDepartment == 0:
				return Response([{"result": "0", "success": "", "error": "Sorry, we couldn't find the department you requested. Please check the department and try again!"}])
			else:
				theDepartmentInstance = Depatment.objects.get(slug=departmentSlug)

				checkUser = myUsers.objects.filter(password=hashedPassword).filter(Q(email=email)|Q(registrationNumber=registrationNumber)).count()
				if checkUser != 0:
					return Response([{"result": "1", "success": "You are already registered, please login to proceed!", "error": ""}])
				else:
					myUsers.objects.create(fname=fname, mname=mname, lname=lname, email=email, registrationNumber=registrationNumber, password=hashedPassword, department=theDepartmentInstance)

					return Response([{"result": "1", "success": "Registration successful! Please login to use the system.", "error": ""}])




class departmentsListClass(ListAPIView):
	serializer_class = departmentSerializer

	def get_queryset(self, *arg, **kwargs):

		queryset = Depatment.objects.all()

		return queryset




class genderListClass(ListAPIView):
	serializer_class = genderSerializer

	def get_queryset(self, *arg, **kwargs):

		queryset = Gender.objects.all()

		return queryset




# GET USER DETAILS AND DISPLAY IN THE PROFILE PAGE
class userProfileClass(ListAPIView):

	serializer_class = userProfileSerializer

	def get_queryset(self, *arg, **kwargs):

		userSlug 		= self.request.GET.get('userSlug', None)

		checkUser = myUsers.objects.filter(slug=userSlug).count()
		if checkUser == 0:
			queryset = myUsers.objects.all()[:0]
		else:
			queryset = myUsers.objects.all().filter(slug=userSlug)

		return queryset




class userLoginClass(APIView):

	permission_classes = []

	def get(self, request, *args, **kwargs):

		Today 		= datetime.now().date()
		currentTime = datetime.now().time()

		action 		= request.GET.get('action', None)
		sentToken 	= request.GET.get('sentToken', None)
		userSlug 	= request.GET.get('sentToken', None)
		username 	= request.GET.get('username', None)
		password 	= request.GET.get('password', None)

		hashedPassword = hashPasswordFunction(request, password)

		if action == 'login':
			
			checkUser = myUsers.objects.filter(password=hashedPassword).filter(Q(email=username)|Q(registrationNumber=username)).count()
			if checkUser == 0:
				return Response([{"result": "0", "success": "", "error": "Login error! Please check you credentials and try agian!"}])
			else:
				getUserData = myUsers.objects.all().filter(password=hashedPassword).filter(Q(email=username)|Q(registrationNumber=username))
				for userData in getUserData:
					userSlug = userData.slug

				theLoginToken = generateLoginTokenFunction(request, userSlug)

				return Response([{"result": "1", "success": "Login successful!", "error": "", "loginToken": theLoginToken, "userSlug": userSlug}])

		elif action == 'renewToken':
			checkUser = myUsers.objects.filter(slug=userSlug, currentToken=sentToken).count()
			if checkUser == 0:
				return Response([{"result": "0", "success": "", "error": "Token verification failed!"}])
			else:
				theLoginToken = generateLoginTokenFunction(request, userSlug)
				return Response([{"result": "1", "success": "Login successful!", "error": "", "loginToken": theLoginToken}])
		else:
			return Response([{"result": "0", "success": "", "error": "Unknown action!"}])
		





class borrow_bookClass(APIView):
	permission_classes = []

	def get(self, request, *args, **kwargs):

		Today 		= datetime.now().date()
		currentTime = datetime.now().time()

		bookSlug 	= request.GET.get('bookSlug', None)
		userSlug 	= request.GET.get('userSlug', None)
		borrowFromDate 	= request.GET.get('borrowFromDate', None)
		borrowFromTime 	= request.GET.get('borrowFromTime', None)
		borrowFromDate 	= datetime.strptime(borrowFromDate, "%Y-%m-%d").date()
		borrowFromTime 	= datetime.strptime(borrowFromTime, "%H:%M").time()

		returned_date 	= request.GET.get('returned_date', None) 
		returned_date 	= datetime.strptime(returned_date, "%Y-%m-%d").date()
		returned_time 	= request.GET.get('returned_time', None)
		returned_time 	= datetime.strptime(returned_time, "%H:%M").time()

	


		checkBook = AddBook.objects.filter(slug=bookSlug).count()
		if checkBook == 0:
			return Response([{"result": "0", "success": "", "error": "Sorry, we couldn't find the book!"}])
		else:
			theBookInstance = AddBook.objects.get(slug=bookSlug)

			checkUser = myUsers.objects.filter(slug=userSlug).count()
			if checkUser == 0:
				return Response([{"result": "0", "success": "", "error": "Sorry, we couldn't find your account!"}])
			else:
				theUserInstance = myUsers.objects.get(slug=userSlug)

				# check if requested date and time is greater than current time
				# check if book is available ie not borrowed or ordered

				BorrowBook.objects.create(borrower=theUserInstance, borrowedBook=theBookInstance, bookNeededFromDate=borrowFromDate, bookNeededFromTime=borrowFromTime, returned_date=returned_date, returned_time=returned_time)

				return Response([{"result": "1", "success": "Book successfuly ordered!", "error": ""}])




class searchABbookClass(ListAPIView):
	serializer_class = booksListSerializer

	def get_queryset(self, *arg, **kwargs):

		searchTerm = self.request.GET.get("searchTerm", None)

		queryset   = AddBook.objects.all().filter(Q(title__icontains=searchTerm)|Q(author__icontains=searchTerm)|Q(publisher__icontains=searchTerm))

		return queryset






class feedbackClass(APIView):
	permission_classes = []

	def get(self, request, *args, **kwargs):

		Today = datetime.now().date()
		currentTime = datetime.now().time()

		name 	= request.GET.get('name', None)
		email 	= request.GET.get('email', None)
		comment = request.GET.get('comment', None)

		if not name and not email and not comment:
			return Response([{"result": "0", "success": "", "error": "The fields are required"}])
		else:
			Feedback.objects.create(name=name, email=email, comment=comment)

			return Response([{"result": "1", "success": "Thanks for your feedback. We appreciate", "error": ""}])




class notificationsClass(ListAPIView):
	serializer_class = notificationsListSerializer

	def get_queryset(self, *arg, **kwargs):

		queryset = BorrowBook.objects.all()
		if not queryset:
			return Response([{"result": "0", "success": "", "error": "You have not borrowed a book yet"}])
		else:
			return queryset