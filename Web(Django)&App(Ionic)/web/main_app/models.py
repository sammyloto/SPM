# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.utils.timezone import now
from django.db.models.signals import pre_save
from django.utils.text import slugify

import random


class BorrowBook(models.Model):
	borrower 		= models.ForeignKey('myUsers', on_delete=models.CASCADE)
	borrowedBook 	= models.ForeignKey('AddBook', on_delete=models.CASCADE, verbose_name="Book borrowed")
	bookNeededFromDate	= models.DateField(blank=True, null=True, verbose_name="book needed on")
	bookNeededFromTime	= models.TimeField(auto_now_add=True, verbose_name="book needed at")
	granted 		= models.BooleanField(default=False)
	returned 		= models.BooleanField(default=False)
	orderedOnDate 	= models.DateField(auto_now_add=True, verbose_name="Ordered on date")
	orderedOnTime 	= models.TimeField(auto_now_add=True, verbose_name="Ordered on time")
	borrowedOnDate 	= models.DateField(blank=True, null=True, verbose_name="Borrowed on date")
	borrowedOnTime 	= models.TimeField(blank=True, null=True, verbose_name="Borrowed on time")
	returned_date 	= models.DateField(null=True, blank=True, verbose_name="Returned date")
	returned_time 	= models.TimeField(blank=True, null=True, verbose_name="Returned time")
	slug 			= models.SlugField(null=True, blank=True, unique=True)

	def __str__(self):
		return self.slug

	generateSlugFrom = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	slug_length = 26
	theSlug = ""

	for i in range(slug_length):
		next_index = random.randrange(len(generateSlugFrom))
		theSlug = theSlug + generateSlugFrom[next_index]

def create_BorrowBook_slug(instance, new_slug=None):
	slug = slugify(instance.theSlug)
	if new_slug is not None:
		slug = new_slug
	ourQuery = BorrowBook.objects.filter(slug=slug).order_by('id')
	exists = ourQuery.exists()
	if exists:
		new_slug = '%s-%s' %(slug, ourQuery.first().id)
		return create_BorrowBook_slug(instance, new_slug=new_slug)
	return slug

def presave_BorrowBook(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_BorrowBook_slug(instance)
pre_save.connect(presave_BorrowBook, sender=BorrowBook)





class Depatment(models.Model):
	name 				= models.CharField(max_length=50)
	addedOnDateTime 	= models.DateTimeField(auto_now_add=True, verbose_name="Added on")
	slug 				= models.SlugField(null=True, blank=True, unique=False)

	def __str__(self):
		return self.name

def create_Depatment_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	ourQuery = Depatment.objects.filter(slug=slug).order_by('id')
	exists = ourQuery.exists()
	if exists:
		new_slug = '%s-%s' %(slug, ourQuery.first().id)
		return create_Depatment_slug(instance, new_slug=new_slug)
	return slug

def presave_Depatment(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_Depatment_slug(instance)
pre_save.connect(presave_Depatment, sender=Depatment)




# Gender list
class Gender(models.Model):
	name 				= models.CharField(max_length=50)
	addedOnDateTime 	= models.DateTimeField(auto_now_add=True, verbose_name="Time Stamp")
	slug 				= models.SlugField(null=True, blank=True, unique=True)

	def __str__(self):
		return self.name

def create_Gender_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	ourQuery = Gender.objects.filter(slug=slug).order_by('id')
	exists = ourQuery.exists()
	if exists:
		new_slug = '%s-%s' %(slug, ourQuery.first().id)
		return create_Gender_slug(instance, new_slug=new_slug)
	return slug

def presave_Depatment(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_Gender_slug(instance)
pre_save.connect(presave_Depatment, sender=Gender)






# Create your models here.
class AddBook(models.Model):
	title 		= models.CharField(max_length=50, blank=False)
	author 		= models.CharField(max_length=75, blank=False)
	pub_date 	= models.DateField(("Date"), default=datetime.now())
	image 		= models.FileField(null=True, blank=True)
	publisher 	= models.CharField(max_length=50, blank=False)
	page_number = models.IntegerField(default=0)
	description = models.TextField(blank=False)
	timestamp 	= models.DateTimeField(auto_now_add=True, verbose_name="Time stamp")
	updated 	= models.DateTimeField(auto_now=True, verbose_name="Updated time")
	slug 		= models.SlugField(null=True, blank=True, unique=True)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ['-timestamp', '-updated']

def create_addBook_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	ourQuery = AddBook.objects.filter(slug=slug).order_by('id')
	exists = ourQuery.exists()
	if exists:
		new_slug = '%s-%s' %(slug, ourQuery.first().id)
		return create_addBook_slug(instance, new_slug=new_slug)
	return slug

def presave_addBook(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_addBook_slug(instance)
pre_save.connect(presave_addBook, sender=AddBook)





# users list
class myUsers(models.Model):
	fname 	= models.CharField(max_length=50)
	mname 	= models.CharField(max_length=75, null=True, blank=True)
	lname 	= models.CharField(max_length=75)
	email 	= models.EmailField()
	slug 	= models.SlugField(null=True, blank=True, unique=True)
	dob 	= models.DateField(null=True, blank=True)
	currentToken 	= models.CharField(max_length=30)
	profileImage 	= models.FileField(null=True, blank=True)
	gender 			= models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True)
	department		= models.ForeignKey(Depatment, on_delete=models.CASCADE)
	password 		= models.CharField(max_length=100)
	registeredOnDateTime 	= models.DateTimeField(auto_now_add=True, verbose_name="Registered on")
	registrationNumber 		= models.CharField(max_length=20, unique=True, verbose_name="Reg Number")

	def __str__(self):
		return self.fname

def create_myUsers_slug(instance, new_slug=None):
	slug = slugify(instance.fname)
	if new_slug is not None:
		slug = new_slug
	ourQuery = myUsers.objects.filter(slug=slug).order_by('id')
	exists = ourQuery.exists()
	if exists:
		new_slug = '%s-%s' %(slug, ourQuery.first().id)
		return create_myUsers_slug(instance, new_slug=new_slug)
	return slug

def presave_myUsers(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_myUsers_slug(instance)
pre_save.connect(presave_myUsers, sender=myUsers)

	




# login tokens
class loginTokens(models.Model):
	loginToken 		= models.CharField(max_length=50)
	user 			= models.ForeignKey(myUsers, on_delete=models.CASCADE)
	active 			= models.BooleanField(default=True)
	createOnDate	= models.DateField(auto_now_add=True)
	createAtTime 	= models.TimeField(auto_now_add=True)
	slug 			= models.SlugField(null=True, blank=True, unique=True)
	deactivatedOnDate = models.DateField(auto_now_add=True, verbose_name="Deactivated on date")
	deactivatedAtTime = models.TimeField(blank=True, null=True, verbose_name="Deactivated at time")

	def __str__(self):
		return self.loginToken

def create_loginTokens_slug(instance, new_slug=None):
	slug = slugify(instance.loginToken)
	if new_slug is not None:
		slug = new_slug
	ourQuery = loginTokens.objects.filter(slug=slug).order_by('id')
	exists = ourQuery.exists()
	if exists:
		new_slug = '%s-%s' %(slug, ourQuery.first().id)
		return create_loginTokens_slug(instance, new_slug=new_slug)
	return slug

def presave_loginTokens(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_loginTokens_slug(instance)
pre_save.connect(presave_loginTokens, sender=loginTokens)


		


# Create your models here.
class Feedback(models.Model):
	name 		= models.CharField(max_length=50, blank=False)
	email 		= models.EmailField(max_length=75, blank=False)
	comment 	= models.TextField(blank=False)
	timestamp 	= models.DateTimeField(auto_now_add=True, verbose_name="Time stamp")
	updated 	= models.DateTimeField(auto_now=True, verbose_name="Updated time")
	slug 		= models.SlugField(null=True, blank=True, unique=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-timestamp', '-updated']

def create_Feedback_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	ourQuery = Feedback.objects.filter(slug=slug).order_by('id')
	exists = ourQuery.exists()
	if exists:
		new_slug = '%s-%s' %(slug, ourQuery.first().id)
		return create_Feedback_slug(instance, new_slug=new_slug)
	return slug

def presave_Feedback(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_Feedback_slug(instance)
pre_save.connect(presave_Feedback, sender=Feedback)
