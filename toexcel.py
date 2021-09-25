import urllib.request
import xlwt
from ast import literal_eval
import urllib.request

wb = xlwt.Workbook()
ws = wb.add_sheet('face')
row_num = 0
columns = ['id','width','height','color','hash','url','userid','username']
for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num])
with open('face.txt', 'r') as people:
    for person in people:
        pers = literal_eval(person)
        for i in range(len(pers['results'])):
            row_num += 1
            id = pers['results'][i]['id']
            width = pers['results'][i]['width']
            height = pers['results'][i]['height']
            color = pers['results'][i]['color']
            url = pers['results'][i]['urls']['full']
            hash = pers['results'][i]['blur_hash']
            user_id = pers['results'][i]['user']['id']
            username = pers['results'][i]['user']['username']
            ls = [id,width,height,color,hash,url,user_id,username]
            imgURL = f"{url}"
            # urllib.request.urlretrieve(imgURL,f"./face/{id}.png")

            for col_num in range(len(ls)):
                ws.write(row_num, col_num, ls[col_num])
            wb.save('face.xls')


