from django.urls import path
from .views import AllNews, BlogListView, BlogDetailView, AddNoticia, AboutUs



urlpatterns = [
      path('postear/', AddNoticia.as_view()),
      path('nosotros/', AboutUs.as_view(), name='nosotros'),
      path('noticias/', AllNews.as_view(), name='blog_noticias'),
      path('<slug:slug>', BlogDetailView.as_view(), name='blog_detail'),
      path('', BlogListView.as_view(), name='blog_list'),
]

  