import PyPDF2
 
def read_pdf(file_path,callback):
    try:
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            print(f"Processing {file_path} with {num_pages} pages.")

            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    print(f"--- Page {page_num + 1} ---")
                    print(text)
                    callback(text,"")
                else:
                    print(f"Page {page_num + 1} is empty or contains non-text content.")
        return True
    except Exception as e:
        print(f"Error reading {file_path}: {str(e)}")
        return False



def move_file(file_path):
    """Move File to archive folder"""
    return_val = True
    try:
        print(f"moving file {file_path}")
    except Exception as e:
        return_val = False

    return return_val
        

