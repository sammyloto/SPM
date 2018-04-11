# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import AddBook, Depatment, myUsers, Gender, BorrowBook, Feedback

# Register your models here.

class AddBookAdmin(admin.ModelAdmin):
	list_display 		= ['title', 'author', 'pub_date', 'publisher', 'timestamp']
	list_display_links  = ['title', 'author', 'publisher']
	list_filter 		= ['title', 'author', 'publisher']
	search_fields 		= ['title', 'author', 'publisher', 'pub_date', 'timestamp']
	list_per_page 		= 15
	class Meta:
		model = AddBook

admin.site.register(AddBook, AddBookAdmin)




class DepatmentAdmin(admin.ModelAdmin):
	list_display 	   = ['name', 'addedOnDateTime']
	list_display_links = ['name', 'addedOnDateTime']
	list_filter 	   = ['name']
	search_fields	   = ['name', 'addedOnDateTime']
	list_per_page 	   = 15
	class Meta:
		model = Depatment

admin.site.register(Depatment, DepatmentAdmin)




class BorrowBookAdmin(admin.ModelAdmin):
	list_display 		= ['borrower', 'borrowedBook']
	list_display_links 	= ['borrower']
	list_filter 		= ['borrower']
	search_fields 		= ['borrower', 'borrowedBook']
	list_per_page 		= 15
	class Meta:
		model = BorrowBook

admin.site.register(BorrowBook, BorrowBookAdmin)



class GenderAdmin(admin.ModelAdmin):
	list_display 		= ['name', 'addedOnDateTime']
	list_display_links 	= ['name']
	list_filter 		= ['name']
	search_fields 		= ['name', 'addedOnDateTime']
	list_per_page 		= 15
	class Meta:
		model = Gender

admin.site.register(Gender, GenderAdmin)



class myUsersAdmin(admin.ModelAdmin):
	list_display 		= ['registrationNumber', 'fname', 'lname', 'department']
	list_display_links 	= ['registrationNumber', 'fname', 'lname']
	list_filter = ['fname', 'mname', 'lname', 'email']
	search_fields = ['fname', 'mname', 'lname', 'email', 'department', 'registrationNumber']
	list_per_page =15
	class Meta:
		model = myUsers

admin.site.register(myUsers, myUsersAdmin)



class feedbackAdmin(admin.ModelAdmin):
	list_display = ['name', 'email']
	list_display_links = ['name']
	list_filter = ['name', 'email']
	search_fields = ['name', 'email', 'comment']
	list_per_page =15
	class Meta:
		model = Feedback

admin.site.register(Feedback, feedbackAdmin)
