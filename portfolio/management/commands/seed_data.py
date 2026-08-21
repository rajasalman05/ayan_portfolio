from django.core.management.base import BaseCommand
from portfolio.models import Profile, SkillCategory, Skill, Education, Project, Certificate


class Command(BaseCommand):
    help = "Seed the database with Muhammad Ayan Abbasi's initial portfolio content."

    def handle(self, *args, **options):
        profile, _ = Profile.objects.get_or_create(
            id=1,
            defaults=dict(
                full_name="Muhammad Ayan Abbasi",
                role_titles="Python Developer, Django Developer, AI Enthusiast, Data Science Learner",
                tagline="Intermediate Computer Science student turning code into working software and data into clear answers.",
                about=(
                    "I'm Muhammad Ayan Abbasi, an Intermediate Computer Science student with a strong "
                    "interest in Python and Django web development. Alongside programming, I'm exploring "
                    "AI and data science, learning how to clean, analyze, and visualize data to draw "
                    "meaningful conclusions.\n\n"
                    "I'm also comfortable with everyday productivity tools — Microsoft Word, Excel, and "
                    "PowerPoint — which I use for documentation, data sheets, and presentations. I enjoy "
                    "building small, practical projects that combine backend logic with clean design, and "
                    "I'm always looking to learn something new."
                ),
                email="ayanabbasi@example.com",
                phone="+92 3XX XXXXXXX",
                location="Pakistan",
                years_learning=2,
                projects_completed=3,
            ),
        )

        categories = {
            "Programming": ("🐍", [("Python", 85), ("C++", 55), ("SQL", 60)]),
            "Web Development": ("🌐", [("Django", 80), ("HTML & CSS", 75), ("REST APIs", 55)]),
            "AI & Data Science": ("📊", [("Pandas & NumPy", 65), ("Data Visualization", 60), ("scikit-learn basics", 45)]),
            "Productivity Tools": ("🗂️", [("Microsoft Word", 90), ("Microsoft Excel", 85), ("Microsoft PowerPoint", 88)]),
        }
        for order, (cat_name, (icon, skills)) in enumerate(categories.items()):
            cat, _ = SkillCategory.objects.get_or_create(name=cat_name, defaults={"icon": icon, "order": order})
            for s_order, (skill_name, prof) in enumerate(skills):
                Skill.objects.get_or_create(
                    category=cat, name=skill_name,
                    defaults={"proficiency": prof, "order": s_order},
                )

        education_rows = [
            dict(degree="Intermediate (Computer Science)", institute="Add college name in admin panel",
                 year="In progress", description="Studying core CS subjects with a focus on programming fundamentals.",
                 order=0),
            dict(degree="Matriculation (Science)", institute="Add school name in admin panel",
                 year="Completed", description="Built a foundation in mathematics and computer studies.",
                 order=1),
        ]
        for row in education_rows:
            Education.objects.get_or_create(degree=row["degree"], institute=row["institute"], defaults=row)

        projects = [
            dict(title="Django Portfolio Website", summary="This very website — a dynamic, admin-driven portfolio.",
                 description="A fully dynamic personal portfolio built with Django, where every section (skills, "
                              "projects, education) is managed through the Django admin panel instead of hard-coded HTML.",
                 tech_stack="Python, Django, SQLite, HTML, CSS, JavaScript", order=0),
            dict(title="Student Data Analysis Tool", summary="A small tool to analyze and visualize student marks using Python.",
                 description="Reads spreadsheet data, calculates grade statistics, and generates simple charts using "
                              "pandas and matplotlib — bridging classroom Excel work with real data science.",
                 tech_stack="Python, Pandas, Matplotlib, Excel", order=1),
            dict(title="Automated Report Generator", summary="Generates formatted Word/PDF reports from raw data automatically.",
                 description="A Python script that takes raw data and produces clean, formatted Word documents and "
                              "PDF reports automatically, saving hours of manual formatting work.",
                 tech_stack="Python, python-docx, Automation", order=2),
        ]
        for row in projects:
            Project.objects.get_or_create(title=row["title"], defaults=row)

        certs = [
            dict(title="Python for Everybody", issuer="Add certificate details in admin", year="", order=0),
            dict(title="Introduction to Data Science", issuer="Add certificate details in admin", year="", order=1),
        ]
        for row in certs:
            Certificate.objects.get_or_create(title=row["title"], defaults=row)

        self.stdout.write(self.style.SUCCESS("Seed data loaded successfully."))
