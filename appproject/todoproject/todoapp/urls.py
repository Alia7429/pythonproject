from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    # path('detail/', views.detail, name='detail')
    path('delete/<int:taskid>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('viewhome/',views.listview.as_view(),name='viewhome'),
    path('viewdetail/<int:pk>/', views.detailview.as_view(), name='viewdetail'),
    path('viewupdate/<int:pk>/',views.updateview.as_view(),name='viewupdate'),
    path('viewdelete/<int:pk>/',views.deleteview.as_view(),name='viewdelete'),
]
