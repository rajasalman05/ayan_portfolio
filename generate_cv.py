"""One-off script to generate Muhammad Ayan Abbasi's CV with Photo & Updated Details."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, Image
)
from reportlab.lib.enums import TA_LEFT, TA_RIGHT

# Palette
INK = colors.HexColor("#0a0f1c")
BLUE = colors.HexColor("#2255c4")
MUTED = colors.HexColor("#55617a")
LINE = colors.HexColor("#dbe1ec")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, textColor=INK, leading=26),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=11, textColor=BLUE, leading=14, spaceAfter=4),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9, textColor=MUTED, leading=13),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12, textColor=INK, spaceBefore=12, spaceAfter=6),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=14, alignment=TA_LEFT),
    "item_title": ParagraphStyle("item_title", fontName="Helvetica-Bold", fontSize=10, textColor=INK, leading=13),
    "item_sub": ParagraphStyle("item_sub", fontName="Helvetica-Oblique", fontSize=9, textColor=MUTED, leading=12),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.5, textColor=INK, leading=13, leftIndent=10),
}

# Directory create karna agar exist na kare
os.makedirs("media/cv", exist_ok=True)

doc = SimpleDocTemplate(
    "media/cv/Muhammad_Ayan_Abbasi_CV.pdf",
    pagesize=A4,
    leftMargin=18 * mm, rightMargin=18 * mm, topMargin=16 * mm, bottomMargin=16 * mm,
)

story = []

# --- HEADER WITH IMAGE ---
contact_text = (
    "<b>Email:</b> ayanabbasi1515@gmail.com &nbsp;·&nbsp; <b>Phone:</b> +92 325 2990965<br/>"
    "<b>Location:</b> Pakistan &nbsp;·&nbsp; <b>Portfolio:</b> ayanportfolio.site<br/>"
    "<b>GitHub:</b> github.com/ayanabbasi &nbsp;·&nbsp; <b>LinkedIn:</b> linkedin.com/in/ayanabbasi"
)

header_para = Paragraph(
    f"<font size=18><b>Muhammad Ayan Abbasi</b></font><br/><br/>"
    f"<font color='#2255c4'><b>Python &amp; Django Developer &nbsp;|&nbsp; AI &amp; Data Science Enthusiast</b></font><br/><br/>"
    f"{contact_text}",
    styles["contact"]
)

# Photo handling
image_path = "profile.jpg"
if os.path.exists(image_path):
    user_img = Image(image_path, width=28 * mm, height=34 * mm)
else:
    user_img = Paragraph("", styles["contact"])

header_table = Table([[header_para, user_img]], colWidths=[138 * mm, 36 * mm])
header_table.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("ALIGN", (1, 0), (1, 0), "RIGHT"),
]))

story.append(header_table)
story.append(Spacer(1, 6))
story.append(HRFlowable(width="100%", thickness=1, color=LINE))

# --- PROFILE SUMMARY ---
story.append(Paragraph("PROFILE SUMMARY", styles["h2"]))
story.append(Paragraph(
    "Intermediate Computer Science student with a strong interest in Python and Django web development, "
    "and a growing focus on AI and data science. Comfortable analyzing and presenting data using Microsoft "
    "Word, Excel, and PowerPoint. Eager to apply classroom learning to real, practical projects and to keep "
    "building a solid foundation in software development and data-driven problem solving.",
    styles["body"]))

# --- TECHNICAL SKILLS ---
story.append(Paragraph("TECHNICAL SKILLS", styles["h2"]))
skills_table_data = [
    ["Programming", "Python, C++ (basics), SQL"],
    ["Web Development", "Django, HTML &amp; CSS, REST APIs, Gunicorn, WhiteNoise"],
    ["AI &amp; Data Science", "Pandas, NumPy, Data Visualization (Matplotlib), Scikit-Learn basics"],
    ["Productivity &amp; Tools", "Git, GitHub, VS Code, MS Word, MS Excel, MS PowerPoint"],
]
skills_table_data = [[Paragraph(a, styles["item_title"]), Paragraph(b, styles["body"])] for a, b in skills_table_data]
t = Table(skills_table_data, colWidths=[42 * mm, 132 * mm])
t.setStyle(TableStyle([
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 1),
]))
story.append(t)

# --- PROJECTS ---
story.append(Paragraph("PROJECTS", styles["h2"]))
projects = [
    ("Django Portfolio Website", "Python, Django, PostgreSQL, Render",
     "Built a fully dynamic personal portfolio website deployed on a custom domain where all content (skills, projects, education) is managed live through the Django admin panel."),
    ("Student Data Analysis Tool", "Python, Pandas, Matplotlib",
     "Developed a tool to analyze student marks from spreadsheet data and generate automated summary performance charts."),
    ("Automated Report Generator", "Python, python-docx, ReportLab",
     "Wrote a script that automatically formats raw structured data into clean Word and PDF reports, reducing manual formatting time."),
]
for title, stack, desc in projects:
    story.append(Paragraph(f"{title}  <font color='#55617a' size=9>— {stack}</font>", styles["item_title"]))
    story.append(Paragraph(desc, styles["body"]))
    story.append(Spacer(1, 4))

# --- EDUCATION ---
story.append(Paragraph("EDUCATION", styles["h2"]))
edu_rows = [
    ("Intermediate (Computer Science)", "In progress", "Studying core computer science subjects, including programming fundamentals, mathematics, and computer studies."),
    ("Matriculation (Science)", "Completed", "Built a strong foundation in mathematics and computer studies."),
]
for title, period, desc in edu_rows:
    story.append(Paragraph(f"{title} <font color='#55617a' size=9>({period})</font>", styles["item_title"]))
    story.append(Paragraph(desc, styles["body"]))
    story.append(Spacer(1, 4))

# --- CERTIFICATES & LANGUAGES ---
story.append(Paragraph("CERTIFICATES", styles["h2"]))
for c in ["Python for Everybody Specialization — Coursera", "Introduction to Data Science — Cognitive Class / IBM"]:
    story.append(Paragraph(f"•  {c}", styles["bullet"]))

story.append(Paragraph("LANGUAGES", styles["h2"]))
story.append(Paragraph("Urdu (Native), English (Fluent)", styles["body"]))

# Build PDF
doc.build(story)
print("CV generated at: media/cv/Muhammad_Ayan_Abbasi_CV.pdf")