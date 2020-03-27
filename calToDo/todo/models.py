from django.db import models
from django.urls import reverse
import django.utils.timezone as timezone

# Create your models here.
class Thing(models.Model) :
    title = models.CharField(max_length = 100)  #任务名
    name = models.CharField(max_length = 50, blank = True)  #姓名
    date_time = models.DateTimeField(default = timezone.now)  #日期
    status = models.TextField(blank = True, null = True)  #进度

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']

    def get_absolute_url1(self):
    	return reverse("thing-id1", kwargs={"id": self.id})
    
    def get_absolute_url2(self):
        return reverse("thing-id2", kwargs={"id": self.id})