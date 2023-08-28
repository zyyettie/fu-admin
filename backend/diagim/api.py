from typing import List
from ninja import Router, ModelSchema, Query, Field
from ninja.pagination import paginate

from diagim.models import Diagim
from utils.fu_crud import (
    ImportSchema,
    create,
    delete,
    export_data,
    import_data,
    retrieve,
    update,
)
from utils.fu_ninja import FuFilters, MyPagination

router = Router()


# 设置过滤字段
class Filters(FuFilters):
    #name: str = Field(None, alias="name")
    #code: str = Field(None, alias="code")
    #status: int = Field(None, alias="status")
    #id: str = Field(None, alias="demo_id")

    name: str = Field(None, alias="name")


# 设置请求接收字段
class DiagimSchemaIn(ModelSchema):
    class Config:
        model = Diagim
        model_fields = ['status', 'pid', 'name', 'age', 'sex']


# 设置响应字段
class DiagimSchemaOut(ModelSchema):
    class Config:
        model = Diagim
        model_fields = "__all__"


# 创建Diagim
@router.post("/diagim", response=DiagimSchemaOut)
def create_diagim(request, data: DiagimSchemaIn):
    diagim = create(request, data, Diagim)
    return diagim


# 删除Diagim
@router.delete("/diagim/{diagim_id}")
def delete_diagim(request, diagim_id: int):
    delete(diagim_id, Diagim)
    return {"success": True}


# 更新Diagim
@router.put("/diagim/{diagim_id}", response=DiagimSchemaOut)
def update_diagim(request, diagim_id: int, data: DiagimSchemaIn):
    diagim = update(request, diagim_id, data, Diagim)
    return diagim


# 获取Diagim
@router.get("/diagim", response=List[DiagimSchemaOut])
@paginate(MyPagination)
def list_diagim(request, filters: Filters = Query(...)):
    qs = retrieve(request, Diagim, filters)
    return qs


# 导入
@router.get("/diagim/all/export")
def export_diagim(request):
    title_dict = {
        'status': '状态',
        'pid': '病人ID',
        'name': '姓名',
        'age': '年龄',
    }
    return export_data(request, Diagim, DiagimSchemaOut, title_dict)


# 导出
@router.post("/diagim/all/import")
def import_diagim(request, data: ImportSchema):
    title_dict = {
        '状态': 'status',
        '病人ID': 'pid',
        '姓名': 'name',
        '年龄': 'age',
    }
    return import_data(request, Diagim, DiagimSchemaIn, data, title_dict)