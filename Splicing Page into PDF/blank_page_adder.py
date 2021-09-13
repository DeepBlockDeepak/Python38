
import os, PyPDF2

#find the existing pdf that needs a blank page
base_doc = input("Enter filepath of the file needing an appending: ")

#find the location where the blank page needs to be inserted
pre_pivot = int(input("After which page would you like to insert a blank page: "))

#create the object for the existing pdf file, so that it can be used by PyPDF2
pdf_base_file = open(base_doc, 'rb')

#@BUG Figure out how to create a true Blank page pdf here in source code, so that
#       this script doesn't depend on one's existence prior to running
#       pdf_blank_page = open(os.path.join(os.path.dirname(base_doc), "Blankie.pdf"), 'wb')

#create the fresh blank PDF, which will be inserted into the existing pdf
pdf_blank_page = open(os.path.join(os.path.dirname(base_doc), "Blank.pdf"), 'rb')

#Reader objects are required so that the Writer Object can use them
base_file_reader = PyPDF2.PdfFileReader(pdf_base_file)
blank_page_reader = PyPDF2.PdfFileReader(pdf_blank_page)
pdfWriter = PyPDF2.PdfFileWriter()

#read each page of the existing PDF, up to the new page spot
for pageNum in range(pre_pivot):
    pageObj = base_file_reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

#read in the blank page
for pageNum in range(blank_page_reader.numPages):
    pageObj = blank_page_reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)

#read the rest of the existing PDF, after the insertion location
for pageNum in range(pre_pivot, base_file_reader.numPages):
    pageObj = base_file_reader.getPage(pageNum)
    pdfWriter.addPage(pageObj)


#create the new filename for the new pdf which has the blank page
new_file_name = base_doc[:(len(base_doc) - 4)] + "_with_blank.pdf"

#open the new PDF and copy the pdfWriter to it
pdfOutputFile = open(new_file_name, 'wb')
pdfWriter.write(pdfOutputFile)

pdfOutputFile.close()
pdf_base_file.close()
pdf_blank_page.close()

