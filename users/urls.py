"""Users app url config"""

from django.urls import path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from . import views


app_name = 'users'

urlpatterns = [
    path('create', view=views.CreateUserView.as_view(), name='create'),
    path('token', view=obtain_jwt_token, name='token'),
    path('token/refresh', view=refresh_jwt_token, name='refresh'),
    path('token/verify', view=verify_jwt_token, name='verify'),

    path('patients', view=views.PatientList.as_view(), name='patient_list'),
    path('patients/<int:pk>', view=views.PatientDetail.as_view(),
         name='patient_detail'),

    path('psychologists', view=views.PsychologistList.as_view(),
         name='psychologist_list'),
    path('psychologists/<int:pk>', view=views.PsychologistDetail.as_view(),
         name='psychologist_detail'),
]