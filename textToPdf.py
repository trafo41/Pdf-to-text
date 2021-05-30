from fpdf import FPDF
import os, shutil

# pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
# pdf.add_page()
# pdf.set_font('Arial', size = 12)
# pdf.set_doc_option(opt =  'latin-1' )

def text_tp_pdf(file_name, file_path, font, s):
    
    pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')
    pdf.add_page()
    pdf.set_font(font , style = '', size = s)

    f = open(file_path, "r")

    for i in f:
        pdf.multi_cell(190, 6, txt = i, align = 'J')             # here 5 is the height of the cell, you can decrease or increase it according to your need
    
    output_name = str(file_name.split('.')[0]) + ".pdf"
    pdf.output(output_name)
    shutil.move(os.path.join(os.getcwd(), output_name), directory)



directory = input("enter the directory path of file: ")
font = input(" Please enter the desired font  : ")
size = int(input(" Please enter the desired size of text  : "))

files = os.listdir(directory)

for i in files:
    # if os.path.isfile(directory+"\\"+i) == True:
    
    if i.endswith("txt"):
        if os.path.isfile(directory+"\\"+i.split('.')[0] + '.pdf'):                                      
            pass
        else:
            file_path = os.path.join(directory, i)
            text_tp_pdf(i, file_path, font, size)
            print(' Task completed')



