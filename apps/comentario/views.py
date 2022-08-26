from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.comentario.forms import CommentForm
from .models import Comentario
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.

class AddComment(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = CommentForm
    template_name = "comentario/add_comment.html"
    #success_url = reverse_lazy('blog_detail') 
    def form_valid(self, form):
        form.instance.noticia_id = self.kwargs["pk"]
        return super().form_valid(form)

    

'''class ReplyComment(LoginRequiredMixin, CreateView):
    model = Comentario
    form_class = CommentForm
    template_name = "comentario/reply_comment.html"

    def form_valid(self, form):
        form.instance.noticia_id = self.kwargs["pk"]
        return super().form_valid(form)

    success_url = reverse_lazy('blog_list') '''


class UpdateComment(LoginRequiredMixin, UpdateView):
    model = Comentario
    form_class = CommentForm
    template_name = "comentario/update_comment.html"
    #success_url = reverse_lazy('blog_list')

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        return Comentario.objects.filter(usuario=self.request.user)


class DeleteComment(LoginRequiredMixin, DeleteView):
    model = Comentario
    template_name = "comentario/delete_comment.html"
    success_url = reverse_lazy('last_x_posts')

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.model.objects.all()
        return Comentario.objects.filter(usuario=self.request.user)
   