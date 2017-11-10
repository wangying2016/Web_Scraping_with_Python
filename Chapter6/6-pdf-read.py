from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import process_pdf
from pdfminer.converter  import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


pdfFile = open('CEF 使用说明中文版.pdf', 'rb')
outputString = readPDF(pdfFile)
print(outputString)
with open('CEF 使用说明中文版.txt', 'w+', encoding='utf8') as f:
    f.write(outputString)
pdfFile.close()
