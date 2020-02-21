from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    parent        = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        full_path = [self.category_name]
        k = self.parent
        while k is not None:
            full_path.append(k.category_name)
            k = k.parent
        return ' -> '.join(full_path[::-1])

class Post(models.Model):
    category      = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title         = models.CharField(max_length=100)
    image         = models.ImageField(default='default.jpg', upload_to='post_pics')
    description   = models.TextField()
    pub_date      = models.DateTimeField(auto_now_add=True)
    author        = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    post          = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    title         = models.CharField(max_length=60)
    content       = models.CharField(max_length=500)
    pub_date      = models.DateTimeField(auto_now_add=True)