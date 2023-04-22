import xlwt
from django.http import HttpResponse
from main.models import *


def export_data(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="tanalanlar_hasabaty.xls"'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Users Data')

    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Ulag Belgisi','Geçen Wagty','Sürüji ID','Geçen Kamerasy',]

    for cols in range(len(columns)):
        ws.write(row_num,cols,columns[cols],font_style)

    font_style=xlwt.XFStyle()

    recs = Recognised.objects.all().order_by('-time').values_list('nomer','time','car_id','camera_id')

    for row in recs:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response


def export_data_cam1(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="merkez_hasabat.xls"'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Users Data')

    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Ulag Belgisi','Geçen Wagty','Sürüji ID']

    for cols in range(len(columns)):
        ws.write(row_num,cols,columns[cols],font_style)

    font_style=xlwt.XFStyle()

    recs = Recognised.objects.all().order_by('-time').values_list('nomer','time','car_id').filter(camera_id="1")

    for row in recs:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response


def export_data_cam2(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="ashgabat_hasabat.xls"'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Users Data')

    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Ulag Belgisi','Geçen Wagty','Sürüji ID']

    for cols in range(len(columns)):
        ws.write(row_num,cols,columns[cols],font_style)

    font_style=xlwt.XFStyle()

    recs = Recognised.objects.all().order_by('-time').values_list('nomer','time','car_id').filter(camera_id="2")

    for row in recs:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response

def export_data_sanly(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="sanly_hasabat.xls"'

    wb=xlwt.Workbook(encoding='utf-8')
    ws=wb.add_sheet('Users Data')

    row_num=0
    font_style=xlwt.XFStyle()
    font_style.font.bold=True

    columns=['Ulag Belgisi','Geçen Wagty','Sürüji ID']

    for cols in range(len(columns)):
        ws.write(row_num,cols,columns[cols],font_style)

    font_style=xlwt.XFStyle()

    recs = Recognised.objects.all().order_by('-time').values_list('nomer','time','car_id').filter(camera_id="3")

    for row in recs:
        row_num +=1
        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]),font_style)
    wb.save(response)
    return response
