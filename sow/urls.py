from django.urls import path
from sow import views


urlpatterns = [
    path('roles/', views.RoleList.as_view()),
    path('roles/<int:pk>', views.RoleDetail.as_view)
]
