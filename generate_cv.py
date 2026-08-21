"""One-off script to generate Muhammad Ayan Abbasi's CV as a clean PDF."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.enums import TA_LEFT

INK = colors.HexColor("#0a0f1c")
BLUE = colors.HexColor("#2255c4")
MUTED = colors.HexColor("#55617a")
LINE = colors.HexColor("#dbe1ec")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=24, textColor=INK, leading=28),
    "role": ParagraphStyle("role", fontName="Helvetica", fontSize=12, textColor=BLUE, spaceAfter=4),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9.5, textColor=MUTED),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12.5, textColor=INK, spaceBefore=14, spaceAfter=6),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=10, textColor=INK, leading=14.5, alignment=TA_LEFT),
    "item_title": ParagraphStyle("item_title", fontName="Helvetica-Bold", fontSize=10.5, textColor=INK, leading=13),
    "item_sub": ParagraphStyle("item_sub", fontName="Helvetica-Oblique", fontSize=9.5, textColor=MUTED, leading=12),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=10, textColor=INK, leading=14, leftIndent=10),
}

doc = SimpleDocTemplate(
    "media/cv/Muhammad_Ayan_Abbasi_CV.pdf",
    pagesize=A4,
    leftMargin=22 * mm, rightMargin=22 * mm, topMargin=18 * mm, bottomMargin=18 * mm,
)

story = []

story.append(Paragraph("Muhammad Ayan Abbasi", styles["name"]))
story.append(Paragraph("Python &amp; Django Developer&nbsp;&nbsp;|&nbsp;&nbsp;AI &amp; Data Science Enthusiast", styles["role"]))
story.append(Paragraph(
    "ayanabbasi@example.com&nbsp;&nbsp;·&nbsp;&nbsp;+92 3XX XXXXXXX&nbsp;&nbsp;·&nbsp;&nbsp;Pakistan&nbsp;&nbsp;·&nbsp;&nbsp;github.com/ayanabbasi&nbsp;&nbsp;·&nbsp;&nbsp;linkedin.com/in/ayanabbasi",
    styles["contact"]))
story.append(Spacer(1, 8))
story.append(HRFlowable(width="100%", thickness=1, color=LINE))

story.append(Paragraph("PROFILE SUMMARY", styles["h2"]))
story.append(Paragraph(
    "Intermediate Computer Science student with a strong interest in Python and Django web development, "
    "and a growing focus on AI and data science. Comfortable analyzing and presenting data using Microsoft "
    "Word, Excel, and PowerPoint. Eager to apply classroom learning to real, practical projects and to keep "
    "building a solid foundation in software development and data-driven problem solving.",
    styles["body"]))

story.append(Paragraph("EDUCATION", styles["h2"]))
edu_rows = [
    ("Intermediate (Computer Science)", "In progress", "Studying core computer science subjects, including programming fundamentals, mathematics, and computer studies."),
    ("Matriculation (Science)", "Completed", "Built a strong foundation in mathematics and computer studies."),
]
for title, period, desc in edu_rows:
    story.append(Paragraph(title, styles["item_title"]))
    story.append(Paragraph(period, styles["item_sub"]))
    story.append(Paragraph(desc, styles["body"]))
    story.append(Spacer(1, 6))

story.append(Paragraph("TECHNICAL SKILLS", styles["h2"]))
skills_table_data = [
    ["Programming", "Python, C++ (basics), SQL"],
    ["Web Development", "Django, HTML &amp; CSS, REST APIs (basics)"],
    ["AI &amp; Data Science", "Pandas, NumPy, data visualization, scikit-learn basics"],
    ["Productivity Tools", "Microsoft Word, Microsoft Excel, Microsoft PowerPoint"],
]
skills_table_data = [[Paragraph(a, styles["item_title"]), Paragraph(b, styles["body"])] for a, b in skills_table_data]
t = Table(skills_table_data, colWidths=[45 * mm, 115 * mm])
t.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("TOPPADDING", (0, 0), (-1, -1), 2),
]))
story.append(t)

story.append(Paragraph("PROJECTS", styles["h2"]))
projects = [
    ("Django Portfolio Website", "Python, Django, SQLite",
     "Built a fully dynamic personal portfolio website where all content — skills, projects, education — is managed through the Django admin panel."),
    ("Student Data Analysis Tool", "Python, Pandas, Matplotlib",
     "Developed a tool to analyze student marks from spreadsheet data and generate summary charts."),
    ("Automated Report Generator", "Python, python-docx",
     "Wrote a script that automatically formats raw data into clean Word/PDF reports, reducing manual formatting time."),
]
for title, stack, desc in projects:
    story.append(Paragraph(f"{title}  <font color='#55617a' size=9>— {stack}</font>", styles["item_title"]))
    story.append(Paragraph(desc, styles["body"]))
    story.append(Spacer(1, 6))

story.append(Paragraph("CERTIFICATES", styles["h2"]))
for c in ["Python for Everybody (in progress / completed — update with real issuer)",
          "Introduction to Data Science (update with real issuer)"]:
    story.append(Paragraph(f"•  {c}", styles["bullet"]))

story.append(Paragraph("LANGUAGES", styles["h2"]))
story.append(Paragraph("Urdu (native), English (fluent)", styles["body"]))

doc.build(story)
print("CV generated.")
