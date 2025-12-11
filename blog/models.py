from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.utils.crypto import get_random_string


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True, blank=True, max_length=170)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    cover_image = models.ImageField(upload_to="posts/", blank=True, null=True)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._generate_unique_slug()
        super().save(*args, **kwargs)

    def _generate_unique_slug(self):
        base_slug = slugify(self.title) or "post"
        slug = base_slug
        counter = 1
        while Post.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            counter += 1
            slug = f"{base_slug}-{counter}"
        # If somehow the slug is still empty, append a random string to avoid collisions
        if not slug:
            slug = f"post-{get_random_string(6)}"
        return slug

    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"slug": self.slug})
