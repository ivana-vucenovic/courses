from django.urls import path
from .import views

urlpatterns = [
    path('', views.index),
    path('new_course', views.new_course),
    path('courses/<int:id>', views.comments),
    path('courses/<int:id>/comment', views.create_comment),
    path('courses/<int:id>/delete', views.delete)
]
