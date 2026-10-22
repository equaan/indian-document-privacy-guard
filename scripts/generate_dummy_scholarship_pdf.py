"""Create a fictional, text-based scholarship application for parser demos."""

from pathlib import Path

import fitz


OUTPUT = Path(__file__).resolve().parents[1] / "samples" / "dummy_scholarship_application.pdf"


def add_page(document: fitz.Document, title: str, lines: list[str]) -> None:
    page = document.new_page()
    page.insert_text((54, 56), "ABC EDUCATION TRUST", fontsize=18, fontname="hebo")
    page.insert_text((54, 82), title, fontsize=13, fontname="hebo")
    page.draw_line((54, 94), (541, 94), color=(0.2, 0.2, 0.2))
    y = 124
    for line in lines:
        page.insert_text((64, y), line, fontsize=11, fontname="helv")
        y += 25
    page.insert_text((54, 780), "Demo data only - created for Indian Document Privacy Guard testing.", fontsize=8)


def main() -> None:
    document = fitz.open()
    add_page(document, "MERIT SCHOLARSHIP APPLICATION - 2026", [
        "Application Number: SCH-2026-0087",
        "Applicant Name: Priya Nair",
        "Student ID: ECE-2026-078",
        "Course: B.Tech Electronics and Communication Engineering",
        "Institution: ABC Engineering College",
        "Academic Year: 2026-27",
    ])
    add_page(document, "APPLICANT CONTACT AND ID DETAILS", [
        "Email Address: priya.nair@example.com",
        "Mobile Number: 9123456789",
        "PAN Number: BCDPN4321K",
        "UPI ID: priya@okaxis",
        "Communication Address: 12 Demo Road, Pune, Maharashtra",
    ])
    add_page(document, "DECLARATION", [
        "I confirm that this application uses fictional data for a privacy-redaction demo.",
        "Applicant Name: Priya Nair",
        "Date: 22 October 2026",
        "Signature: Priya Nair",
    ])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    document.save(OUTPUT)
    document.close()
    print(f"Created: {OUTPUT}")


if __name__ == "__main__":
    main()
