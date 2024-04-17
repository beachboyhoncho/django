from django.urls import path
from .import views

urlpatterns = [
    #path('',views.index,name="index"),
    path('about/',views.about,name="about"),
    path('',views.login_user,name="login"),
    path('logout/',views.logout_user,name="logout"),
    path('signup/',views.signup,name="signup"),
    path('add/',views.add,name="add"),
    path('book/<int:pk>',views.book,name="book"),
    path('delete/<int:pk>',views.delete_book,name="delete"),
    path('update/<int:pk>', views.update_record, name='update'),
    
]
