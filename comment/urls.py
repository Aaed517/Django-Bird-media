from django.urls import path

from comment import views
app_name = 'Comment'

urlpatterns = [
        path('index', views.index, name='index'),
        path('commentadd', views.commentadd , name='commentadd'),
        path('commentlike', views.commentlike, name='commentlike'),
        path('recomment', views.recomment, name='recomment'),
        path('subcommentadd', views.subcommentadd, name='subcommentadd'),
        path('subcommentlist/<int:id>', views.subcommentlist, name='subcommentlist'),
        path('get_likes_count/<int:id>', views.get_likes_count, name='get_likes_count'),
        path('profile', views.profile, name='profile')
]
