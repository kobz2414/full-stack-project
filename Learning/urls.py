from django.contrib import admin
from django.urls import path
from myApp import views as indexPage
from movies import views as movieViews
from courses.views import CoursesView, CreateCourseView, UpdateCourseView, StudentApiView
from courses.models import Course
from django.urls import reverse_lazy

urlpatterns = [
    path('admin/', admin.site.urls, name = "index"),
    path('', indexPage.My_name),
    path('helloAgain/', indexPage.index, name = "helloAgain"),
    path('movies/', movieViews.list, name = "movieList"),
    path('movies/detail/<int:movie_id>', movieViews.detail, name = "movieList_details"),
    path('movies/createMovie', movieViews.createMovie, name = "createMovie"),
    path('movies/updateMovie/<int:movie_id>', movieViews.updateMovie, name="updateMovie"),
    path('courses/list/', CoursesView.as_view(), name = "coursesList"),
    path('courses/create/', CreateCourseView.as_view(), name = "createCourse"),
    path('courses/<int:course_id>/students', StudentApiView.as_view(), name = "student_list"),
    path('courses/update/<slug:pk>/', UpdateCourseView.as_view(model = Course, success_url = reverse_lazy("coursesList")), name = "updateCourse"),
]