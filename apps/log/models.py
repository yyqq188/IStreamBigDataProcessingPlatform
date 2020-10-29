from django.db import models

# Create your models here.

class FinkSQLLog(models.Model):
    object_id = models.CharField(primary_key=True,max_length=50,default="",verbose_name="主键")
    # name = models.CharField(max_length=20,null=True,blank=True,default="",verbose_name="用户名")
    # email= models.EmailField(verbose_name="邮箱")
    # address = models.CharField(max_length=100,verbose_name="联系地址")
    # message = models.CharField(max_length=500,verbose_name="留言信息")
    app_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="应用名称")
    gen_datetime = models.DateField(max_length=500,verbose_name="时间")
    log = models.CharField(max_length=10000, verbose_name="日志信息")

    class Meta:
        verbose_name = "FlinkSQL日志"
        verbose_name_plural = verbose_name
        db_table = "FlinkSQL日志表"
        # ordering = "-object_id"  #倒序


class ClickhouseSQLLog(models.Model):
    object_id = models.CharField(primary_key=True,max_length=50,default="",verbose_name="主键")
    app_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="应用名称")
    gen_datetime = models.DateField(max_length=500, verbose_name="时间")
    log = models.CharField(max_length=10000, verbose_name="日志信息")

    class Meta:
        verbose_name = "ClickhouseSQL日志"
        verbose_name_plural = verbose_name
        db_table = "ClickhouseSQL日志表"
        # ordering = "-object_id"  #倒序

class Kafka2CHLog(models.Model):
    object_id = models.CharField(primary_key=True,max_length=50,default="",verbose_name="主键")
    app_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="应用名称")
    gen_datetime = models.DateField(max_length=500, verbose_name="时间")
    log = models.CharField(max_length=10000, verbose_name="日志信息")
    class Meta:
        verbose_name = "Kafka2CH日志"
        verbose_name_plural = verbose_name
        db_table = "Kafka2CH日志表"
        # ordering = "-object_id"  #倒序

class Kafka2HbaseLog(models.Model):
    object_id = models.CharField(primary_key=True,max_length=50,default="",verbose_name="主键")
    app_name = models.CharField(max_length=200, null=True, blank=True, verbose_name="应用名称")
    gen_datetime = models.DateField(max_length=500, verbose_name="时间")
    log = models.CharField(max_length=10000, verbose_name="日志信息")

    class Meta:
        verbose_name = "Kafka2Hbase日志"
        verbose_name_plural = verbose_name
        db_table = "Kafka2Hbase日志表"
        # ordering = "-object_id"  #倒序
