import sys
import PyPDF2

inputs = sys.argv[1:]


def pdf_merger(arg):
    merger = PyPDF2.PdfFileMerger()
    for i in arg:
        merger.append(i)
    merger.write('super.pdf')


pdf_merger(inputs)
