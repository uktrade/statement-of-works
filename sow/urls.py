from django.urls import path
from sow import views


urlpatterns = [
    path('roles/', views.RoleList.as_view()),
    path('roles/<int:pk>', views.RoleDetail.as_view()),
    path('costcentrecode/', views.CostCentreCodeList.as_view()),
    path('costcentrecode/<int:pk>', views.CostCentreCodeDetail.as_view())
]
