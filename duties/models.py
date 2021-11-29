from django.db import models
from django.urls import reverse
from django.conf import settings


class Team(models.Model):
    date = models.DateField()
    duty = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.date

class Event(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField("시작시간")
    title = models.CharField("이벤트 이름", max_length=50)

    class Meta:
        verbose_name = "이벤트 데이터"
        verbose_name_plural = "이벤트 데이터"

    def __str__(self):
        return self.title

    @property
    def get_html_url(self):
        url = reverse('duties:edit', args=(self.id,)) # 다시 URL로 돌아감
        return f'<a href="{url}"> {self.title} </a>'
"""
Django ORM 용

{
    1: 
        [['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],
         ['', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N', 'O', 'D', 'E', 'N'],]
    
}
"""