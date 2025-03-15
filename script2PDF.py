#This tool is designed by IHA089
import sys, os
from PyPDF2 import PdfReader, PdfWriter

def inject_js_into_pdf(pdf_file, js_file, output_file):
    try:
        with open(js_file, 'r') as js_f:
            js_content = js_f.read()

        reader = PdfReader(pdf_file)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        writer.add_js(js_content)

        with open(output_file, "wb") as output_pdf:
            writer.write(output_pdf)

        print(f"[script2PDF] JavaScript successfully injected into: {output_file}")
    except Exception as e:
        print(f"[script2PDF!] Error occurred: {e}")

def check_file_present(file_path):
    if not os.path.isfile(file_path):
        print(f"[script2PDF!] Error: File '{file_path}' does not exist.")
        return False
    return True

def main():
    try:
        pdf_file = sys.argv[1]
    except IndexError:
        pdf_file = input("Enter pdf file path: ")
    if not check_file_present(pdf_file):
        return

    try:
        js_file = sys.argv[2]
    except IndexError:
        js_file = input("Enter js file path: ")
    if not check_file_present(js_file):
        return

    output_file = f"malicious_{pdf_file.split('/')[-1]}"

    print(f"[script2PDF] Injecting JavaScript into PDF...")
    print(f"[script2PDF] PDF File: {pdf_file}")
    print(f"[script2PDF] JavaScript File: {js_file}")
    print(f"[script2PDF] Output File: {output_file}")
    
    inject_js_into_pdf(pdf_file, js_file, output_file)

if __name__ == "__main__":
    main()
