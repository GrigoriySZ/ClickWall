from django.db import models

class MoodPost(models.Model):
    author = models.CharField(
        max_length=50,
        default='Аноним',
        verbose_name='Имя автора',
        help_text='Введите имя автора'
    )
    text = models.TextField(
        max_length=280,
        verbose_name='Техт сообщения',
        help_text='Введите текст сообщения'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания поста'
    )
    def __str__(self):
        return f'{self.text[:30]}... ({self.author})' if len(self.text) > 30 else f'{self.text} ({self.author})'