from django.contrib import admin

# Register your models here.

from .models import Kafka2CHMatch
from .models import ClickhouseTableInfo
from .models import BaseInfo
from .models import JobInfo

from django.contrib import admin

admin.AdminSite.site_header = '流数据处理平台'
admin.AdminSite.site_title = '流数据处理平台'



class BaseInfoAdmin(admin.ModelAdmin):

    list_display = ["app_name","kafka_cluster","kafka_topic","clickhouse_cluster","clickhouse_database","clickhouse_tablename"]
    search_fields = ["app_name","kafka_cluster","kafka_topic","clickhouse_cluster","clickhouse_database","clickhouse_tablename"]
    list_filter = ["app_name","kafka_cluster","kafka_topic","clickhouse_cluster","clickhouse_database","clickhouse_tablename"]

class ClickhouseTableInfoAdmin(admin.ModelAdmin):
    list_display = ["order_index","simple_field","query_size","partition_size","partition_field","hold_time","app_name"]
    search_fields = ["order_index","simple_field","query_size","partition_size","partition_field","hold_time","app_name"]
    list_filter = ["order_index","simple_field","query_size","partition_size","partition_field","hold_time","app_name"]

class Kafka2CHMatchAdmin(admin.ModelAdmin):



    list_display = ["app_name","kafka_cluster","kafka_cluster","ch_type","ch_property","ch_expression","ch_field_name"]
    search_fields = ["app_name","kafka_cluster","kafka_cluster","ch_type","ch_property","ch_expression","ch_field_name"]
    list_filter = ["app_name","kafka_cluster","kafka_cluster","ch_type","ch_property","ch_expression","ch_field_name"]


class JobInfoAdmin(admin.ModelAdmin):
    list_display = ["configID","app_name","change_time","kafka_cluster","kafka_topic","clickhouse_cluster","clickhouse_database","clickhouse_tablename","state"]
    list_filter = ["configID","app_name","change_time","kafka_cluster","kafka_topic","clickhouse_cluster","clickhouse_database","clickhouse_tablename","state"]



admin.site.register(Kafka2CHMatch,Kafka2CHMatchAdmin)
admin.site.register(ClickhouseTableInfo,ClickhouseTableInfoAdmin)
admin.site.register(BaseInfo,BaseInfoAdmin)
admin.site.register(JobInfo,JobInfoAdmin)
