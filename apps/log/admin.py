from django.contrib import admin

# Register your models here.

from .models import FinkSQLLog
from .models import ClickhouseSQLLog
from .models import Kafka2CHLog
from .models import Kafka2HbaseLog


class FinkSQLLogAdmin(admin.ModelAdmin):

    list_display = ["object_id","gen_datetime","log"]
    search_fields = ["object_id","gen_datetime","log"]
    list_filter = ["object_id","gen_datetime","log"]

class ClickhouseSQLLogAdmin(admin.ModelAdmin):

    list_display = ["object_id","gen_datetime","log"]
    search_fields = ["object_id","gen_datetime","log"]
    list_filter = ["object_id","gen_datetime","log"]


class Kafka2CHLogAdmin(admin.ModelAdmin):

    list_display = ["object_id","gen_datetime","log"]
    search_fields = ["object_id","gen_datetime","log"]
    list_filter = ["object_id","gen_datetime","log"]


class Kafka2HbaseLogAdmin(admin.ModelAdmin):

    list_display = ["object_id","gen_datetime","log"]
    search_fields = ["object_id","gen_datetime","log"]
    list_filter = ["object_id","gen_datetime","log"]





admin.site.register(FinkSQLLog,FinkSQLLogAdmin)
admin.site.register(ClickhouseSQLLog,ClickhouseSQLLogAdmin)
admin.site.register(Kafka2CHLog,Kafka2CHLogAdmin)
admin.site.register(Kafka2HbaseLog,Kafka2HbaseLogAdmin)
