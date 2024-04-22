import PyPDF2

def read_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)
        pdf_text = ''
        
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()
        
        return pdf_text

file_path = 'design thinking.pdf' # path to your pdf  file
pdf_contents = read_pdf(file_path)
print(pdf_contents)
