# Indian Document Privacy Guard

Indian Document Privacy Guard is a local-first Streamlit application that detects and redacts sensitive information in college and scholarship documents. It combines regular expressions with spaCy Named Entity Recognition (NER) to identify personal data before a document is shared.

## Features

- Upload and process TXT, CSV, PDF, JSON, DOCX, and XLSX files.
- Detect names, emails, Indian mobile numbers, PAN numbers, UPI IDs, student IDs, registration numbers, URLs, IP addresses, and selected financial identifiers.
- Validate Aadhaar-like numbers with a Verhoeff checksum to reduce false positives.
- Choose which categories should be redacted.
- Mask information using full, partial, or placeholder redaction.
- Show entity counts and a Low, Medium, or High privacy-risk score.
- Download redacted outputs and privacy-safe reports that do not include the original sensitive values.

## How it works

```text
Document upload or pasted text
        -> text extraction and preprocessing
        -> regex + spaCy NER detection
        -> duplicate cleanup and risk scoring
        -> selected-entity redaction
        -> redacted document and safe report
```

Regex handles structured Indian identifiers such as PAN and phone numbers. spaCy NER helps identify person names in ordinary text. This hybrid approach is suitable for an NLP mini-project because it demonstrates both rule-based and language-based processing.

## Quick start (Windows PowerShell)

```powershell
git clone https://github.com/YOUR_USERNAME/indian-document-privacy-guard.git
cd indian-document-privacy-guard

python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m spacy download en_core_web_sm
.\.venv\Scripts\python.exe -m streamlit run app\gui_app.py
```

Open http://localhost:8501 in your browser.

## Demo data

Use the fictional files in `samples/` to test the application. Never commit or upload real admission forms, scholarship applications, identity documents, or exported files containing personal data.

## Project structure

```text
app/
  gui_app.py                 Streamlit interface
  pii_service.py             Detection, risk, and redaction orchestration
  modules/
    data_ingestion.py        File validation and text extraction
    ner_engine.py            Regex, Aadhaar validation, and spaCy NER
    redaction_engine.py      Redaction and safe export logic
samples/                     Fictional local test documents
tests/                       Regression tests for Indian PII rules
```

## Current limitations

- A scanned or image-only PDF has no extractable text and requires OCR before detection.
- Free-form postal addresses and regional languages need dedicated models or rules for reliable detection.
- The privacy-risk score is a transparent academic demo score, not legal or compliance advice.

## Tech stack

- Python
- Streamlit
- spaCy
- Microsoft Presidio
- PyMuPDF
- python-docx, pandas, and openpyxl

## Academic concepts demonstrated

- Text extraction and preprocessing
- Tokenization
- Named Entity Recognition
- Regular expressions
- Hybrid NLP pipelines
- Privacy-preserving document redaction

## License

MIT. See [LICENSE](LICENSE).
