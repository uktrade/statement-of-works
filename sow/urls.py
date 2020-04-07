from django.urls import path
from sow import views


urlpatterns = [
    path('costcentrecode/', views.CostCentreCodeList.as_view()),
    path('costcentrecode/<int:pk>', views.CostCentreCodeDetail.as_view()),
    path('deliverable/', views.DeliverableList.as_view()),
    path('deliverable/<int:pk>', views.DeliverableDetail.as_view()),
    path('role/', views.RoleList.as_view()),
    path('role/<int:pk>', views.RoleDetail.as_view()),
    
]
