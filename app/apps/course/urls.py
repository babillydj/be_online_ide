from django.urls import path, include
from . import views


app_name = 'runner'
urlpatterns = [
    path('api/v1/course/', include(
        ([
            path('list/', views.CourseList.as_view(), name='run_code'),
            path('detail/<int:pk>', views.CourseDetail.as_view(), name='run_code2'),
        ], 'course_api_v1')
    ))
]
