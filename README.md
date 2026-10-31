# PDF Cutter ✂️

A lightweight Python tool that extracts specific page ranges from a PDF and saves them under a custom file name.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📌 Features

- **Custom page ranges:** single pages, ranges (`1-5`), or a mix (`1, 3, 7-10`).
- **Custom output name:** save the extracted PDF under any name you choose.
- **Fast and lightweight:** handles large documents with minimal dependencies.
- **No quality loss:** pages are copied as-is, so layout, formatting, and images are preserved.

---

## 🚀 Getting Started

### Prerequisites

Python 3.x. Check your version with:

```bash
python --version
```

### Installation

```bash
git clone https://github.com/rajbhowmik-code/Pdf-cutter.git
cd Pdf-cutter
pip install -r requirements.txt
```

---

## 🛠️ Usage

```bash
python main.py
```

Then follow the prompts:

1. Enter the path to your PDF.
2. Enter the pages to extract, e.g. `1-5` or `1, 3, 7-10`.
3. Enter the name for the output file.

**Example**

| Input file   | Pages       | Output file    |
|--------------|-------------|----------------|
| `book.pdf`   | `1, 3, 7-10`| `chapters.pdf` |

---

## 📁 Project Structure

```
Pdf-cutter/
├── main.py            # Core script for cutting PDFs
├── requirements.txt   # Project dependencies
├── README.md          # Project documentation
└── .gitignore         # Files ignored by Git
```

---

## 🤝 Contributing

Issues and pull requests are welcome.

## 📄 License

Distributed under the MIT License. See `LICENSE` for details.

## 👤 Author

**Raj Bhowmik Sany**: [GitHub](https://github.com/rajbhowmik-code)
