import PyPDF2
import sys

if len(sys.argv) != 2:
    print("Wrong amount of command line arguments given")
    print("Try: 'python Crop.py -input_file_name-")
    sys.exit(1)

in_file = open(str(sys.argv[1]), 'rb')
pdf_reader = PyPDF2.PdfFileReader(in_file)

out_file = open('edit-' + str(sys.argv[1]), 'wb')
pdf_writer = PyPDF2.PdfFileWriter()

for pagenum in range(pdf_reader.numPages):
    
    # get page from in file
    page = pdf_reader.getPage(pagenum)

    # print(page.mediaBox.getUpperLeft())
    # set top right corner
    page.cropBox.upperRight = (545, 753)
    
    # set lower left corner
    page.cropBox.lowerLeft = (67, 435)
    
    # rotate page
    page.rotateClockwise(90)

    # write to new pdf
    pdf_writer.addPage(page)

pdf_writer.write(out_file)

in_file.close()
out_file.close()