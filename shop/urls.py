from django.urls import path

from .views import index


urlpatterns = [
    path('',index, name = 'index'),
    path('<int:course_id>',views.single_course, name='single_course')

]