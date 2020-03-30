from django.db import models
import django.utils.timezone as timezone

# Create your models here.
class Comment(models.Model) :
    name = models.CharField(max_length = 50, blank = True)  #姓名
    date_time = models.DateTimeField(default = timezone.now)  #日期
    text = models.TextField(blank = True, null = True)  #正文

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.text

    class Meta:  #按时间下降排序
        ordering = ['-date_time']
