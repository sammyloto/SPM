from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class booksListSerializer(ModelSerializer):
	
	class Meta:
		model  = AddBook
		fields = [
			"title",
			"author",
			"pub_date",
			"image",
			"publisher",
			"page_number",
			"description",
			"timestamp",
			"updated",
			"slug",
		]


class departmentSerializer(ModelSerializer):
	
	class Meta:
		model  = Depatment
		fields = [
			"name",
			"addedOnDateTime",
			"slug",
		]



class genderSerializer(ModelSerializer):
	
	class Meta:
		model  = Gender
		fields = [
			"name",
			"addedOnDateTime",
			"slug",
		]



class myUserSerializer(ModelSerializer):
	
	class Meta:
		model  = Depatment
		fields = [
			"fname",
			"mname",
			"lname",
			"email",
			"profileImage",
			"dob",
			"registrationNumber",
			"department",
			"registeredOnDateTime",
			"slug",
		]



class userProfileSerializer(ModelSerializer):

	departmentName = serializers.CharField(source='department.name', read_only=True)
	genderName 	   = serializers.CharField(source='gender.name', read_only=True)

	class Meta:
		model  = myUsers
		fields = [
			"fname",
			"mname",
			"lname",
			"email",
			"departmentName",
 			"profileImage",
			"genderName",
			"registrationNumber",
			"slug"
		]



class notificationsListSerializer(ModelSerializer):

	borrowerName = serializers.CharField(source='borrower.fname', read_only=True)
	borrowedBooTitle = serializers.CharField(source='borrowedBook.title', read_only=True)
	borrowedBookImage = serializers.CharField(source='borrowedBook.image', read_only=True)
	borrowedBookAuthor = serializers.CharField(source='borrowedBook.author', read_only=True)
	
	class Meta:
		model  = BorrowBook
		fields = [
			"borrowerName",
			"borrowedBooTitle",
			"borrowedBookImage",
			"borrowedBookAuthor",
			"bookNeededFromDate",
			"returned_date",
			"slug",
		]
