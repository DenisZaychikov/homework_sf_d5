from django.contrib import admin
from django.urls import path
from p_library import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('book_increment/', views.book_increment),
    path('book_decrement/', views.book_decrement),
    path('pb_houses_books/', views.pb_houses_books, name='pb_houses_books'),
    path('friends_list/', views.friends_list, name='friends_list'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('friend_info/<int:id>', views.friend_info, name='friend_info'),
]
