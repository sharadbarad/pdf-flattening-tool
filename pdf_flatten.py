import fitz  # PyMuPDF
from PIL import Image
import io


def pdf_to_images(pdf_path, password="", dpi=300):
    """
    Converts each page of a PDF to an RGB image.

    Parameters:
        pdf_path (str): Path to the input PDF file.
        password (str, optional): Password to open the PDF file.
        dpi (int, optional): DPI for the output images.

    Returns:
        list: A list of PIL Image objects.
    """
    pdf_document = fitz.open(pdf_path)
    if password:
        if not pdf_document.authenticate(password):
            raise ValueError("Incorrect password for PDF file.")
    
    images = []
    for page_num in range(len(pdf_document)):
        try:
            page = pdf_document.load_page(page_num)
            zoom = dpi / 72  # Calculate zoom factor based on DPI
            mat = fitz.Matrix(zoom, zoom)
            pix = page.get_pixmap(matrix=mat, alpha=False)  # Ignore transparency
            img = Image.open(io.BytesIO(pix.tobytes())).convert('RGB')
            images.append(img)
        except Exception as e:
            print(f"Error rendering page {page_num + 1}: {e}")
    return images

def images_to_pdf(images, output_pdf_path, dpi=300):
    """
    Saves a list of images into a PDF file.

    Parameters:
        images (list): A list of PIL Image objects.
        output_pdf_path (str): Path to the output PDF file.
        dpi (int, optional): DPI for the output PDF.
    """
    if images:
        images[0].save(output_pdf_path, save_all=True, append_images=images[1:], resolution=dpi)
    else:
        print("No images to save.")


if __name__ == "__main__":
    # Get input from user
    input_pdf = input("Enter the input PDF file path: ")
    output_pdf = input("Enter the output PDF file path (default: output.pdf): ") or "output.pdf"
    password = input("Enter PDF password (press Enter if none): ")

    while True:
        try:
            dpi = int(input("Enter DPI (72-600, default 300): ") or "300")
            if 72 <= dpi <= 600:
                break
            print("DPI must be between 72 and 600")
        except ValueError:
            print("Please enter a valid number")

    try:
        print(f"Processing PDF with {dpi} DPI...")
        images = pdf_to_images(input_pdf, password=password, dpi=dpi)
        images_to_pdf(images, output_pdf, dpi=dpi)
        print(f"Successfully flattened PDF saved as: {output_pdf}")
    except Exception as e:
        print(f"An error occurred: {e}")