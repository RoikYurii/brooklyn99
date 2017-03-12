from django.db import models

class New(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    data_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.title