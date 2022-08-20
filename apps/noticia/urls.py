from django.urls import path
from .views import AllNews, BlogListView, BlogDetailView, AddNoticia, EditarNoticia, AboutUs



urlpatterns = [

      path('editar/<int:pk>', EditarNoticia.as_view(), name='editar'),
      path('administrar/', AddNoticia.as_view(), name= 'postear'),
      path('nosotros/', AboutUs.as_view(), name='nosotros'),
      path('noticias/', AllNews.as_view(), name='blog_noticias'),
      path('<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
      path('', BlogListView.as_view(), name='blog_list'),
      
]

  