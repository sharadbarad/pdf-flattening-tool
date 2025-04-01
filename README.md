# PDF Flattening Tool

A Python-based tool that converts PDFs into flattened versions by processing each page as an image. This tool is particularly useful when you need to:
- Creating PDFs that prevent direct copying of content
- Remove interactive elements from PDFs
- Create a universally compatible version of a PDF
- Ensure consistent rendering across different PDF viewers
- Preserve the visual appearance of complex PDFs

---

## Features

- 🔄 Converts PDFs to images and back to PDF format
- 🔐 Supports password-protected PDFs
- 🎨 Maintains visual fidelity of the original document
- 📐 Customizable DPI settings (72-600 DPI)
- 🖼️ Preserves image quality during conversion

---

## Requirements

- Python 3.6 or higher
- PyMuPDF (fitz)
- Pillow (PIL)

## How It Works

1. The tool reads the input PDF file page by page
2. Each page is converted to a high-quality image at the specified DPI
3. These images are then combined into a new PDF file
4. The result is a flattened PDF where each page is essentially an image

---

## Use Cases

- Creating PDFs that prevent direct copying of content
- Removing interactive elements for compatibility
- Ensuring consistent appearance across different PDF viewers
- Creating web-friendly versions of complex PDFs

---

**🤝 Any issues or errors? Please raise them now.**

