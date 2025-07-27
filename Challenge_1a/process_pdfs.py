import json
from pathlib import Path
import fitz  # PyMuPDF
import re

# Keywords that are always considered headings
CUSTOM_KEYWORDS = [
    "Revision History", "Table of Contents", "Acknowledgements", "References",
    "Appendix", "Summary", "Background", "Milestones", "Evaluation", "Business Plan",
    "Proposal", "Terms of Reference", "Membership", "Chair", "Meetings", "Financial and Administrative Policies"
]

HEADING_MIN_LENGTH = 4  # Ignore headings shorter than this (except numbered)

# Detect heading level using multiple signals
def detect_heading_level(text, span, prev_fontsize=None):
    # Numbered pattern (e.g., 1., 2.1, 3.2.1)
    numbered = re.match(r'^(\d+\.)+\s', text)
    if numbered:
        num_dots = text.count('.')
        if num_dots == 1:
            return 'H1'
        elif num_dots == 2:
            return 'H2'
        else:
            return 'H3'
    # Custom keywords
    for kw in CUSTOM_KEYWORDS:
        if kw.lower() in text.lower():
            return 'H1'
    # Font size logic (relative to previous font size)
    if prev_fontsize and span['size'] > prev_fontsize:
        return 'H1'
    # Bold or large font
    if span.get('flags', 0) & 2 or span['size'] >= 16:
        return 'H1'
    elif span['size'] >= 14:
        return 'H2'
    elif span['size'] >= 12:
        return 'H3'
    return None

def clean_outline(outline):
    cleaned = []
    last = None
    for item in outline:
        # Merge fragments if close together
        if last and item['page'] == last['page'] and item['level'] == last['level']:
            last['text'] += ' ' + item['text']
        else:
            if last:
                cleaned.append(last)
            last = item.copy()
    if last:
        cleaned.append(last)
    # Filter: keep only valid headings
    filtered = [
        o for o in cleaned
        if (len(o['text']) >= HEADING_MIN_LENGTH or re.match(r'^(\d+\.)+\s', o['text']))
    ]
    # Remove duplicates
    seen = set()
    result = []
    for o in filtered:
        key = (o['level'], o['text'], o['page'])
        if key not in seen:
            seen.add(key)
            result.append(o)
    return result

def extract_pdf_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    toc = doc.get_toc(simple=True)  # [level, title, page]
    for item in toc:
        level, text, page = item
        outline.append({
            "level": f"H{level}",
            "text": text,
            "page": page
        })
    # Try to get the title from metadata or first page
    title = doc.metadata.get("title", "")
    if not title and doc.page_count > 0:
        # Fallback: largest text on first page
        first_page = doc[0]
        blocks = first_page.get_text("dict")["blocks"]
        max_fontsize = 0
        title_candidate = ""
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if span["size"] > max_fontsize and text:
                            max_fontsize = span["size"]
                            title_candidate = text
        title = title_candidate
    return title, outline

def extract_outline_by_signals(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = ""
    max_fontsize = 0
    title_candidate = ""
    prev_fontsize = None
    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if not text:
                            continue
                        if page_num == 1 and span["size"] > max_fontsize:
                            max_fontsize = span["size"]
                            title_candidate = text
                        level = detect_heading_level(text, span, prev_fontsize)
                        prev_fontsize = span["size"]
                        if level:
                            outline.append({
                                "level": level,
                                "text": text,
                                "page": page_num
                            })
    title = title_candidate
    return title, outline

def process_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    for pdf_file in input_dir.glob("*.pdf"):
        title, outline = extract_pdf_outline(pdf_file)
        # If no outline/bookmarks, fallback to multi-signal heuristic
        if not outline:
            title, outline = extract_outline_by_signals(pdf_file)
        outline = clean_outline(outline)
        output = {"title": title, "outline": outline}
        with open(output_dir / f"{pdf_file.stem}.json", "w") as f:
            json.dump(output, f, indent=2)
        print(f"Processed {pdf_file.name} -> {pdf_file.stem}.json")

if __name__ == "__main__":
    print("Starting processing pdfs")
    process_pdfs()
    print("Completed processing pdfs")