from django.conf.urls import url, include

from .views import *
app_name="main_app"

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^books_list/$', booksListClass.as_view(), name="bookListName"),
    url(r'^book_details/$', bookDetailsClass.as_view(), name="bookDetailsName"),
    url(r'^search_a_book/$', searchABbookClass.as_view(), name="searchABookName"),
    url(r'^borrow_book/$', borrow_bookClass.as_view(), name="borrowBookName"),
    url(r'^departments_list/$', departmentsListClass.as_view(), name="departmentsListName"),
    url(r'^gender_list/$', genderListClass.as_view(), name="genderListName"),
    url(r'^user_login/$', userLoginClass.as_view(), name="userLoginName"),
    url(r'^feedback/$', feedbackClass.as_view(), name="feedbackName"),
    url(r'^user_profile/$', userProfileClass.as_view(), name="userProfileName"),
    url(r'^user_registration/$', userRegistrationClass.as_view(), name="userRegistrationName"),
    # url(r'^user_registration/$', userRegistrationClass.as_view(), name="userRegistrationName"),
    url(r'^notifications/$', notificationsClass.as_view(), name="notificationName"),

]
