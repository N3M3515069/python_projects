import PyPDF2

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

# for looping the numbers of times as much as the super.pdf containes the numbers of pages
for i in range(template.getNumPages()):

    # to get the pages from the super.pdf
    pages = template.getPage(i)

    # merging each page of super.pdf with wtr.pdf
    pages.mergePage(watermark.getPage(0))

    output.addPage(pages)

    # to update our merged pdf and creating a new file
    with open('watermarked_output.pdf', 'wb') as file:
        output.write(file)
