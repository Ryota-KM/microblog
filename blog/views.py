from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Blog
from .forms import BlogForm


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # 必須 (BlogFormで定義済みの為、不要)
    # fields = ["content"]
    success_url = reverse_lazy("index")


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    # (BlogFormで定義済みの為、不要)
    # fields = ["content"]

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": blog_pk})
        return url


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("index")
