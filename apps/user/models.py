from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.
class UserProfile(AbstractUser):

    nick_name = models.CharField(max_length=50,verbose_name="昵称",default="")
    birthday = models.DateField(verbose_name="生日",null=True,blank=True)
    gender = models.CharField(verbose_name="性别",max_length=10,choices=(("male","男"),("female","女")),default="female")
    address = models.CharField(verbose_name="地址",max_length=11,null=True,blank=True)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username



