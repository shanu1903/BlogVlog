from django.urls import path , include
from . import views
from .views import   PostDetailView ,PostCreateView ,PostUpdateView , PostDeleteView , UserPostListView


urlpatterns = [
    # path('',PostListView.as_view() , name = "home"),
    path('',views.home , name = 'home'),
    path('about/' , views.about, name = 'about'),
    path('post/<int:pk>' , PostDetailView.as_view() , name = 'post-detail'),
    path('post/new' , PostCreateView.as_view(template_name = 'blog/posts_form.html') , name = 'post-create'),
    path('post/<int:pk>/update' , PostUpdateView.as_view(),name = 'post-update'),
    path('post/<int:pk>/delete' , PostDeleteView.as_view() , name = 'post-delete'),
    path('user/<str:username>' , UserPostListView.as_view() , name = 'post-user' )

]

