import xlsxwriter
import csv
import stockpricer
from stockpricer import get_data,get_adjusted_close,get_volume


# Create a new Excel workbook and add a worksheet
def filewritersheet1():
    workbook = xlsxwriter.Workbook('stocks.xlsx')
    worksheet = workbook.add_worksheet()

    # Write the column headers
    headers = ['Ticker Symbol', 'Company Name', 'Exchange', 'Asset Type', 'IPO Date','Delisting Date', 'Status']
    worksheet.write_row('A1', headers)

    # Write the data for ULST
    with open('listing_status.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        row_num = 1
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                symbol = row[0]
                name = row[1]
                exchange = row[2]
                assetType = row[3]
                ipoDate = row[4]
                delistingDate = row[5]
                status = row[6]
                data = [symbol,name, exchange, assetType, ipoDate, delistingDate, status]
                worksheet.write_row(row_num,0, data)
                row_num += 1

'''
def filewritersheet2():
    workbook = xlsxwriter.Workbook('stocks.xlsx')
    worksheet_price = workbook.add_worksheet()
    headers_price = ['Symbol', 'Company Name', 'Adjusted Close', 'Volume']
    worksheet_price.write_row('A1', headers_price)
    with open('listing_status.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count_price = 0
        row_num_price = 1
        for row in csv_reader:
            if line_count_price == 0:
                line_count_price += 1
            else:
                symbol_price = row[0]
                name = row[1]
                data = [symbol_price,name,stockpricer.get_adjusted_close(symbol_price),stockpricer.get_volume(symbol_price)]
                worksheet_price.write_row(row_num_price,0, data)
                row_num_price += 1
    workbook.close()
    print("Function completed successfully!")

filewritersheet2()
'''