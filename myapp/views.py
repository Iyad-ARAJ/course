from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def all_courses(request):    #To View all Courses 
    context = {'all_courses' : courses()}
    return render(request, 'allcourses.html',context)


def add_course(request):
    if request.method == 'POST':
        errors = Course.objects.basic_validator(request.POST) #To Check Validation
        if len(errors) > 0:
            for error in errors.values():
                messages.error(request,error)
            return redirect('/')    
        create_course(request.POST)              # To create new course
        return redirect('/')

def remove_course(request, id):  #dnaskljdn daskdnas
    if request.method == 'POST':
        removecourse(id)
        return redirect('/')  
    else:                    #If it's not POST request , Go To Confirmation Message
        course = course_id(id)
        return render(request, 'delete_course.html', {'course': course})

def view_comments(request,id): #To view all comments 
    context = {'course': course_id(id),
               'allcomments' : allcomments(id)}
    return render(request, 'comments.html', context)

def add_comment(request, id): # To create a comment and redirct it  to comments.html
    course =  course_id(id)    
    if request.method == 'POST':
        create_comment(request.POST,id)
    return redirect(f'/courses/comment/{course.id}')



