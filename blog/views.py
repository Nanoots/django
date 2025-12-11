from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(published=True)
    template_name = "blog/post_list.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = self.queryset[:4]
        context["categories"] = [
            "All",
            "Commercial",
            "Design",
            "Nature",
            "People",
            "Photography",
            "Tech",
            "Travel",
            "Uncategorized",
        ]
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "excerpt", "content", "cover_image", "published"]
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("blog:post_list")

    def form_valid(self, form):
        # Ensure slug is regenerated on create if left blank
        form.instance.slug = ""
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", "excerpt", "content", "cover_image", "published"]
    template_name = "blog/post_form.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("blog:post_list")


class PostDeleteView(DeleteView):
    model = Post
    template_name = "blog/post_confirm_delete.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"
    success_url = reverse_lazy("blog:post_list")
