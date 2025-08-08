from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    comment = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.comment[:30]}..."