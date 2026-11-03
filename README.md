# Python Automation for Office Tasks

**Official companion resources for the book by Luis García**  
*15 Practical Projects to Save Time with Files, Excel, PDFs and Everyday Workflows*

Welcome! This repository contains the sample files, Python scripts, and practice resources used in the book. The examples are designed for beginners and use fictional data.

## What's included

- **15 Python projects** with editable source code.
- **Practice data** for spreadsheets, PDFs, CSV files, and folders.
- **Exercises** described in the book, which you can complete by modifying the scripts.
- A **sample-data generator** to restore the original practice files.

## Download the files

1. Click the green **Code** button at the top of this repository.
2. Select **Download ZIP**.
3. Extract the ZIP file on your computer.
4. Open the extracted folder in Visual Studio Code or another code editor.

You do not need a GitHub account to download the public files.

## Requirements

- Python 3 installed on your computer (preferably a current supported release).
- A terminal or Visual Studio Code.
- Internet access to install the packages once.

The scripts use these additional packages: `openpyxl`, `pypdf`, `reportlab`, and `python-docx`. Their compatible versions are listed in [`requirements.txt`](requirements.txt).

## Quick start

Open a terminal in the downloaded project folder (the same folder containing `requirements.txt`).

**Windows:**

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python build_samples.py
.venv\Scripts\python projects/p01_organize_files.py
```

**macOS / Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build_samples.py
.venv/bin/python projects/p01_organize_files.py
```

The first project creates organized sample files. Check the generated `output/` folder to see the results.

**Important:** `build_samples.py` recreates demonstration inputs. If you edited those files, save your changes before running the generator again.

## The 15 projects

| # | Topic | Python file |
|---|---|---|
| 1 | Organize files by type | [`p01_organize_files.py`](projects/p01_organize_files.py) |
| 2 | Batch-rename files | [`p02_batch_rename.py`](projects/p02_batch_rename.py) |
| 3 | Find duplicate files | [`p03_find_duplicates.py`](projects/p03_find_duplicates.py) |
| 4 | Clean Excel data | [`p04_clean_excel.py`](projects/p04_clean_excel.py) |
| 5 | Merge Excel workbooks | [`p05_merge_workbooks.py`](projects/p05_merge_workbooks.py) |
| 6 | Create Excel reports | [`p06_excel_report.py`](projects/p06_excel_report.py) |
| 7 | Convert CSV to Excel | [`p07_csv_to_excel.py`](projects/p07_csv_to_excel.py) |
| 8 | Merge PDFs | [`p08_merge_pdfs.py`](projects/p08_merge_pdfs.py) |
| 9 | Extract text from PDFs | [`p09_extract_pdf_text.py`](projects/p09_extract_pdf_text.py) |
| 10 | Generate PDF reports | [`p10_generate_pdf_report.py`](projects/p10_generate_pdf_report.py) |
| 11 | Draft automated emails | [`p11_email_draft.py`](projects/p11_email_draft.py) |
| 12 | Prepare emails with attachments | [`p12_email_attachment.py`](projects/p12_email_attachment.py) |
| 13 | Generate Word letters | [`p13_word_letters.py`](projects/p13_word_letters.py) |
| 14 | Prepare a script for scheduling | [`p14_scheduled_task.py`](projects/p14_scheduled_task.py) |
| 15 | Build an office automation toolkit | [`p15_office_toolkit.py`](projects/p15_office_toolkit.py) |

To run a different project, replace the script name in the last command. For example:

```bash
python projects/p08_merge_pdfs.py
```

Use the virtual environment's Python executable instead of `python` if you have not activated it.

## Additional starter scripts

- [`first_report.py`](first_report.py): introductory example from Chapter 1.
- [`task_summary.py`](task_summary.py): another beginner-level example.
- [`build_samples.py`](build_samples.py): creates fictional practice data.

## Safety and responsible use

- **Work with copies**, never your only copy of an important file.
- Do not use real customer, employee, or confidential information while practicing.
- Projects 11 and 12 save email drafts locally by default; they do **not** send messages unless you explicitly pass `--send` and configure SMTP settings. Never commit credentials or passwords.
- Project 14 logs a run. To automate repeated runs, you must separately configure your operating system's scheduler.
- The educational examples are provided **as is**. Review and test before adapting them to real business workflows.

## Troubleshooting

- **`python` is not recognized:** on Windows try `py`, or reinstall Python and enable its command-line integration.
- **`ModuleNotFoundError`:** install the dependencies using the same Python interpreter used to run the project.
- **File not found:** run commands from the repository's root folder, not from inside `projects/`.
- **Unexpected results:** regenerate fictional inputs using `build_samples.py` after saving any changes you want to keep.

## About the book

**Python Automation for Office Tasks** teaches practical Python by walking through real-world-style office scenarios, with step-by-step explanations, exercises, and examples.

This repository is supplementary material. It is not a free copy of the ebook.

© 2026 Luis García. Educational use of the example scripts is permitted with the book. Redistribution or resale of this companion package as a separate product is not authorized without permission.

