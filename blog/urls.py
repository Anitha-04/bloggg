from django.urls import path
from.import views
app_name='blog'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('', views.register, name='register'),
    path('insertblog/', views.insertblog, name='insertblog'),
    path('blog1/',views.blog1,name='blog1'),
    path('blog2/<int:pk>', views.blog2, name='blog2'),

]