from openpyxl import Workbook
import datetime
import os


#create workbook
workbook = Workbook()
active_worksheet = workbook.active
active_worksheet['A1'] ="FUCK"
active_worksheet['B1'] = datetime.datetime.now()
workbook.save("test_workbook.xlsx")
print(os.listdir('.'))
