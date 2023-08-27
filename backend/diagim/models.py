from django.db import models
from utils.models import CoreModel

# Create your models here.
class Diagim(CoreModel):
    status = 
    id = models.CharField(null=False, max_length=32, verbose_name="病人ID", help_text="病人ID")
    name = models.CharField(null=False, max_length=64, verbose_name="姓名", help_text="姓名")
    age = models.CharField(null=False, max_length=32, verbose_name="年龄", help_text="年龄")
    sex = models.CharField(null=False, max_length=32, verbose_name="性别", help_text="性别")
    inspection_type = models.CharField(null=False, max_length=32, verbose_name="检查类型", help_text="检查类型")
    inspection_content = 
    is_request_form = 
    quantity_of_charts = 
    inspection_time = 
    inventory_time = 
    hospital_name = 
    
    class Meta:
        db_table = "Diagim"
        verbose_name = '影像诊断'
        verbose_name_plural = verbose_name
        ordering = ('-create_datetime',)
