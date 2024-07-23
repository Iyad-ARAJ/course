from django.urls import path
from . import views

urlpatterns = [ 
    path('',views.all_courses,name='index'),
    path('addcourse',views.add_course,name='add_course'),
    path('courses/destroy/<int:id>',views.remove_course,name='remove_course'),
    path('courses/comment/<int:id>',views.view_comments,name='viewcomments'),
    path('courses/addcomment/<int:id>',views.add_comment,name='comment'),
]