import PyPDF2

with open('dummy.pdf', 'rb') as file:

    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter() #this allows us to write the object in memory
    writer.addPage(page)
    with open('tilt.pdf', 'wb') as new_file: #to update our dummy pdf to write and rotate
        writer.write(new_file)
