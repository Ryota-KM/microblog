from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Blog
from .forms import BlogForm


class BlogListView(ListView):
    model = Blog
    context_object_name = "blogs"


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"


class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    # 必須 (BlogFormで定義済みの為、不要)
    # fields = ["content"]
    success_url = reverse_lazy("index")
    template_name = "blog/blog_create_form.html"

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "失敗しました")
        return super().form_invalid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    # (BlogFormで定義済みの為、不要)
    # fields = ["content"]
    template_name = "blog/blog_update_form.html"

    def get_success_url(self):
        blog_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": blog_pk})
        return url

    def form_valid(self, form):
        messages.success(self.request, "更新しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新に失敗しました")
        return super().form_invalid(form)


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)
