from pypdf import PdfReader, PdfWriter

def extract_pages(input_pdf, output_pdf, start_page, end_page):
    reader = PdfReader(input_pdf)
    writer = PdfWriter()
    
    # Python indexing starts at 0, so subtract 1 from start_page
    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])
        
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"Successfully saved {output_pdf}!")

# Example usage for Rosen Discrete Math:
extract_pages("Discrete Mathematics and Its Applications - Kenneth Rosen (2012)s.pdf", "DM_Part_1.pdf", 1, 60)