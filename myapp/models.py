from django.db import models

class CourseManager(models.Manager):
    def basic_validator(self,postData):
        errors = {}
        if len(postData['name']) < 5:
            errors['name'] = 'The name must be at least 5 char'

        if len(postData['description']) < 15 :
            errors['description'] = 'description must be at least 15 char'
        return errors
    
class Description(models.Model):
     content = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     
class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



def create_course(post): #Create new cource
    description_instance = Description.objects.create(content = post['description']) # Create an instance of Desc
    course = Course.objects.create(name = post['name'],description = description_instance)
    return course


def courses():
    courses = Course.objects.all()
    return courses

def removecourse(id):
    remove_course = Course.objects.get(id = id)
    remove_course.delete()

def course_id(id):
    course_id = Course.objects.get(id = id)
    return course_id

def allcomments(id):
    course = course_id(id)
    return course.comments.all()

def create_comment(post,id):
    course = course_id(id)
    comment_content = post['comment']
    comment = Comment.objects.create(course=course, content=comment_content)
    return comment





