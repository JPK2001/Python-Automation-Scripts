import PyPDF2
import os

def merge_pdfs(input_dir, output_file):
    # Get list of PDF files in the input directory
    pdf_files = [file for file in os.listdir(input_dir) if file.endswith('.pdf')]
    pdf_files.sort()  # Sort files to merge them in order

    # Create PDF writer object
    pdf_writer = PyPDF2.PdfFileWriter()

    # Iterate over each PDF file and append to the writer
    for pdf_file in pdf_files:
        with open(os.path.join(input_dir, pdf_file), 'rb') as file:
            pdf_reader = PyPDF2.PdfFileReader(file)
            # Iterate over each page and add it to the writer
            for page_num in range(pdf_reader.numPages):
                page = pdf_reader.getPage(page_num)
                pdf_writer.addPage(page)

    # Write the merged PDF to the output file
    with open(output_file, 'wb') as out_file:
        pdf_writer.write(out_file)

    print(f'Merged PDF saved to {output_file}')

input_directory = 'input_directory_path'  # Directory containing PDF files to merge
output_file = 'merged_output.pdf'  # Output file path for merged PDF
merge_pdfs(input_directory, output_file)
