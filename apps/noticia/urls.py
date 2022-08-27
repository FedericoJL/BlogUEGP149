from django.urls import path
from .views import AllNews, BlogListView, BlogDetailView, AddNoticia, CategoryPost, DeleteCategory, DeleteNoticia, EditarNoticia, AboutUs, AddCategory, search_view, UpdateCategory


urlpatterns = [
      
      path('buscar/', search_view, name='buscar'),
      path('delete_noticia/<int:pk>', DeleteNoticia.as_view(), name= 'delete_noticia'),
      path('editar/<int:pk>', EditarNoticia.as_view(), name='editar'),
      path('delete_category/<int:pk>', DeleteCategory.as_view(), name= 'delete_category'),
      path('edit_category/<int:pk>', UpdateCategory.as_view(), name= 'edit_category'),
      path('add_category/', AddCategory.as_view(), name= 'add_category'),
      path('administrar/', AddNoticia.as_view(), name= 'postear'),
      path('nosotros/', AboutUs.as_view(), name='nosotros'),
      path('categoria/<int:pk>', CategoryPost.as_view(), name='category'),
      path('noticias/', AllNews.as_view(), name='blog_noticias'),
      path('<int:pk>', BlogDetailView.as_view(), name='blog_detail'),
      path('', BlogListView.as_view(), name='last_x_posts'),
      
]

  