from django.urls import path, re_path
from . import views

urlpatterns = [
    path('bhm', views.bhm, name='bhm'),
    path('csem', views.csem, name='csem'),
    path('erpm', views.erpm, name='erpm'),
    path('som', views.som, name='som'),
    path('view_notice/<int:id>', views.view_notice, name='view_notice'),
    path('delete_notice/<int:id>', views.delete_notice, name='delete_notice'),
    path('create_notice/<str:slug>', views.create_notice, name='create_notice'),
    path('redirect_me/<str:slug>', views.redirect_me, name='redirect_me'),




]