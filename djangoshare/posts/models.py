from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

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
    description   = models.CharField(max_length=1000)
    pub_date      = models.DateTimeField('date published')

    def __str__(self):
        return self.title

class Comment(models.Model):
    post          = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    title         = models.CharField(max_length=60)
    content       = models.CharField(max_length=500)
    pub_date      = models.DateTimeField('date published')