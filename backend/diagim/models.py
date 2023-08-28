from django.db import models
from utils.models import CoreModel

# Create your models here.
class Diagim(CoreModel):
    status = models.CharField(null=False, max_length=64, verbose_name="状态", help_text="状态")
    pid = models.CharField(null=False, max_length=32, verbose_name="病人ID", help_text="病人ID")
    name = models.CharField(null=False, max_length=64, verbose_name="姓名", help_text="姓名")
    age = models.CharField(null=False, max_length=32, verbose_name="年龄", help_text="年龄")
    sex = models.CharField(null=False, max_length=32, verbose_name="性别", help_text="性别")
    inspection_type = models.CharField(null=False, max_length=32, verbose_name="检查类型", help_text="检查类型")
    inspection_content = models.CharField(null=False, max_length=64, verbose_name="检查内容", help_text="检查内容")
    is_request_form = models.CharField(max_length=64, verbose_name="是否申请单", help_text="申请单")
    quantity_of_charts = models.CharField(max_length=64, verbose_name="图量", help_text="图量")
    inspection_time = models.CharField(max_length=64, verbose_name="检查时间", help_text="检查时间")
    inventory_time = models.CharField(max_length=64, verbose_name="入库时间", help_text="入库时间")
    hospital_name = models.CharField(max_length=64, verbose_name="医院名称", help_text="医院名称")
    
    class Meta:
        db_table = "Diagim"
        verbose_name = '影像诊断'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
