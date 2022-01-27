from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    """тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        """возвращает строковое представление модели"""
        return self.text


class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
 
    def __str__(self):
        """Return a string representation of the model."""
        text_str = self.text
        if len(self.text) > 50:
            text_str = text_str[:50] + "..."

        return text_str
