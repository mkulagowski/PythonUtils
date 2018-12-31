import PyPDF2
import sys

page_no = int(sys.argv[3])
with open(sys.argv[1], 'rb') as doc:
    with open(sys.argv[2], 'rb') as doc2:
        reader = PyPDF2.PdfFileReader(doc)
        swapPage = PyPDF2.PdfFileReader(doc2).getPage(0)
        writer = PyPDF2.PdfFileWriter()
        for i in range(reader.numPages):
            page = reader.getPage(i)
            if i == page_no:
                swapPage.mergePage(page)
                page = swapPage
            writer.addPage(page)
        with open('swapped_output.pdf', 'wb') as output_file:
            writer.write(output_file)
