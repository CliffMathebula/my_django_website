from django.db import models


class Post(models.Model):
    name = models.TextField()
    surname = models.TextField()
    id_number = models.IntegerField()
    email_address = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length = 50)
    user_id = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
