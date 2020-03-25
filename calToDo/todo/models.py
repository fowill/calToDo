from django.db import models
from django.urls import reverse

# Create your models here.
class Thing(models.Model) :
    title = models.CharField(max_length = 100)  #事项题目
    category = models.CharField(max_length = 50, blank = True)  #事项标签
    date_time = models.DateTimeField(auto_now_add = True)  #事项日期
    content = models.TextField(blank = True, null = True)  #事项说明正文

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

    def get_absolute_url(self):
    	return reverse("article-detail", kwargs={"id": self.id})
