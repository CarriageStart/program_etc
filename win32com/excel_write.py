import win32com.client as client


EXCEL = client.Dispatch("Excel.Application")
EXCEL.Visible = True

def main():
    wb = excel.Workbooks.Add("Test.xlsx")
    wb2 = excel.Workbooks.Add()
    ws = wb.Worksheets.Add("Test_sheet")
    ws2 = wb2.Worksheets.Add()


if __name__=="__main__":
    main()


