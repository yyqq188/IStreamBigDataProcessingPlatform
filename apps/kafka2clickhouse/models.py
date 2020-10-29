from django.db import models

# Create your models here.

class BaseInfo(models.Model):
    #这里要提前建立
    app_name = models.CharField(primary_key=True,max_length=200,null=False,blank=False,verbose_name="应用名称")
    kafka_cluster = models.CharField(max_length=50,verbose_name="Kafka/MQ集群",choices=(('kafkacluster1','集群1'),('kafkacluster2','集群2')),default='kafkacluster1')
    kafka_topic = models.CharField(max_length=100,verbose_name="数据Topic")
    clickhouse_cluster = models.CharField(max_length=50,verbose_name="Clickhouse集群",choices=(('clickhousecluster1','集群1'),('clickhousecluster2','集群2')),default='clickhousecluster1')
    clickhouse_database = models.CharField(max_length=50,verbose_name="Clickhouse库名",choices=(('clickhousedb1','库1'),('clickhousedb2','库2')),default='clickhousedb1')
    clickhouse_tablename = models.CharField(max_length=50,verbose_name="Clickhouse表名",null=False)
    class Meta:
        verbose_name = "基本信息"
        verbose_name_plural = verbose_name
        db_table = "Kafka2CH基本信息表"

class ClickhouseTableInfo(models.Model):
    order_index = models.CharField(max_length=100,verbose_name="排序索引")
    simple_field = models.CharField(max_length=100,verbose_name="抽样字段")
    query_size = models.CharField(max_length=100,choices=(("DEFAULT","默认"),("OTHER","其他")),default="DEFAULT",verbose_name="查询粒度")
    #TODO 分区粒度
    partition_size = models.CharField(max_length=100,choices=(("DEFAULT","默认"),("OTHER","其他")),default="DEFAULT",verbose_name="分区粒度")
    #TODO 分区字段
    partition_field = models.CharField(max_length=100,choices=(("DEFAULT","默认"),("OTHER","其他")),default="DEFAULT",verbose_name="分区字段")
    #TODO 数据保留时间
    hold_time = models.CharField(max_length=100,verbose_name="数据保留时间")
    #TopicSchema 默认从kafka topic中自动抽取
    # topic_schema = models.CharField()

    #关联应用名称 为了获得kafka的表数据
    app_name = models.CharField(max_length=200,null=False,blank=False,verbose_name="关联应用名称")

    class Meta:
        verbose_name = "CH建表参数"
        verbose_name_plural = verbose_name
        db_table = "CH建表参数表"

class Kafka2CHMatch(models.Model):
    app_name = models.CharField(primary_key=True,max_length=200, verbose_name="kafka字段")
    kafka_cluster = models.CharField(max_length=100, verbose_name="kafka字段类型")
    ch_type = models.CharField(max_length=100, verbose_name="CH消费类型")
    ch_property = models.CharField(max_length=100, verbose_name="CH属性")
    ch_expression = models.CharField(max_length=100, verbose_name="CH表达式")
    ch_field_name = models.CharField(max_length=100, verbose_name="CH字段名")

    class Meta:
        verbose_name = "Schema展示"
        verbose_name_plural = verbose_name
        db_table = "Schema展示表"


class JobInfo(models.Model):
    #这里要提前建立
    configID= models.CharField(primary_key=True,max_length=200,null=False,blank=False,verbose_name="配置ID")
    app_name = models.CharField(max_length=50,default='应用名称')
    change_time = models.DateField(max_length=100,verbose_name="更新时间")
    kafka_cluster = models.CharField(max_length=50, verbose_name="Kafka/MQ集群")
    kafka_topic = models.CharField(max_length=100, verbose_name="Topic")
    clickhouse_cluster = models.CharField(max_length=50,verbose_name="Clickhouse集群")
    clickhouse_database = models.CharField(max_length=50,verbose_name="Clickhouse库名")
    clickhouse_tablename = models.CharField(max_length=50,verbose_name="Clickhouse表名",null=False)
    state = models.CharField(max_length=50,verbose_name="状态")
    class Meta:
        verbose_name = "任务导入"
        verbose_name_plural = verbose_name
        db_table = "Kafka2CH任务导入表"
