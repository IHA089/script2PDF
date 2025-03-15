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

        print(f"[*] JavaScript successfully injected into: {output_file}")
    except Exception as e:
        print(f"[!] Error occurred: {e}")

def check_file_present(file_path):
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
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

    output_file = f"js_injected_{pdf_file.split('/')[-1]}"

    print(f"[*] Injecting JavaScript into PDF...")
    print(f"[*] PDF File: {pdf_file}")
    print(f"[*] JavaScript File: {js_file}")
    print(f"[*] Output File: {output_file}")
    sys.exit()
    inject_js_into_pdf(pdf_file, js_file, output_file)

if __name__ == "__main__":
    main()
