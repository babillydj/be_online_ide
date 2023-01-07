from django.urls import path, include
from . import views


app_name = 'runner'
urlpatterns = [
    path('api/v1/runner/', include(
        ([
            path('run-code/', views.run_code, name='run_code'),
            path('run-code2/', views.run_code2, name='run_code2'),
            # path('run-code3/', views.run_code3, name='run_code3'),
        ], 'runner_api_v1')
    ))
]
