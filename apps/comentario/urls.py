from django.urls import path
from .views import AddComment, UpdateComment, DeleteComment

urlpatterns = [
      
      path('update_comment/<int:pk>', UpdateComment.as_view(), name='update_comment'),
      path('delete_comment/<int:pk>', DeleteComment.as_view(), name='delete_comment'),
      path('<int:pk>', AddComment.as_view(), name='add_comment'),

]
