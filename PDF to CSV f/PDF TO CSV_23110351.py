import fitz 
import re
import csv

def read_pdf(pdf_file):
    text = ""
    with fitz.open(pdf_file) as doc:
        for page in doc:
            text += page.get_text()
    return text

def to_csv(pattern, text, csv_file, header):
    data = re.findall(pattern, text, re.MULTILINE)
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(header)
        writer.writerows(data)
    print("Conversion done")

party_pdf_file = "EB_Redemption_Details_PDF.pdf"
party_csv_file = "EB_Redemption_Details_CSV.csv"
party_file_header = ['Sr No', 'Date of Encashment', 'Name of the Political Party', 'Account no. of Political Party',
                     'Prefix', 'Bond Number', 'Denominations', 'Pay Branch Code', 'Pay Teller']
party_row_pattern = r'(\d+)\s+(\d+/\w+/\d+)\s+(.+?)\s+(\*{7}\d+)\s+(\w+)\s+(\d+)\s+([\d,]+)\s+(\d+)\s+(\d+)'

text = read_pdf(party_pdf_file)
to_csv(party_row_pattern, text, party_csv_file, party_file_header)

purchaser_pdf_file = "EB_Purchase_Details_PDF.pdf"
purchaser_csv_file = "EB_Purchase_Details_CSV.csv"
purchaser_file_header = ['Sr No', 'Reference No (URN)', 'Journal Date', 'Date of Purchase', 'Date of Expiry',
                         'Name of the Purchaser', 'Prefix', 'Bond Number', 'Denominations', 'Issue Branch Code',
                         'Issue Teller', 'Status']
purchaser_row_pattern = r'(\d+)\s+(\S+)\s+(\d+/\w+/\d+)\s+(\d+/\w+/\d+)\s+(.+?)\s+(.+?)\s+([A-Z]+)\s+(\d+)\s+([\d,]+)\s+(\S+)\s+(\d+)\s+(\w+)'

text = read_pdf(purchaser_pdf_file)
to_csv(purchaser_row_pattern, text, purchaser_csv_file, purchaser_file_header)
