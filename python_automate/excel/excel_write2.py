from openpyxl import Workbook

wb = Workbook()
ws = wb.create_sheet('sheet_test3')

ws.append(['Number', 'Name'])

for i in range(10):
    ws.append([i, str(i) +' data'])

wb.save('result2.xlsx')