# Muhammad Ayan Abbasi — Portfolio Website (Django)

A dynamic, admin-driven portfolio website. All content (skills, projects,
education, certificates, contact info, CV file) is stored in the database
and can be edited from the Django admin panel — no code editing needed to
update it.

## What's included
- Full Django project, ready to run (`db.sqlite3` already has sample data loaded)
- Admin panel to manage every section of the site
- A working contact form that saves messages into the database
- A starter CV (`media/cv/Muhammad_Ayan_Abbasi_CV.pdf`) already attached and downloadable from the site
- A dark, terminal-inspired custom design (not a template)

## How to run it

1. Install Python 3.10+ if you don't already have it.
2. Open a terminal in this folder and install the requirements:
   ```
   pip install -r requirements.txt
   ```
3. Start the site:
   ```
   python manage.py runserver
   ```
4. Open your browser at: http://127.0.0.1:8000/

## Admin panel (to edit content)

- URL: http://127.0.0.1:8000/admin/
- Username: `admin`
- Password: `Ayan@12345`

**Please change this password immediately** — go to Admin → Users → admin →
"this form" (change password link).

From the admin panel you can:
- Edit the **Profile** (name, tagline, about text, email, phone, social links, CV upload, profile photo)
- Add/edit **Skill categories** and **Skills** (with a 0–100 proficiency slider that becomes the animated bar)
- Add/edit **Education** entries (shown as a timeline)
- Add/edit **Projects** (title, description, tech tags, image, live/source links)
- Add/edit **Certificates**
- Read **Contact messages** sent through the website's contact form

## Updating the CV

Go to Admin → Profile → upload a new file in the "Cv file" field. The
"Download CV" button on the site will automatically point to the new file.
A starter CV template is already generated for you — replace it with the
real one whenever it's ready (`generate_cv.py` shows how it was built with
reportlab, in case you want to regenerate it from a script).

## Before putting this online (deployment)

This is currently set up for local development (`DEBUG = True`, SQLite
database). Before deploying to a live server:
1. Set `DEBUG = False` in `ayan_portfolio/settings.py`
2. Set a new, secret `SECRET_KEY`
3. Set `ALLOWED_HOSTS` to your real domain
4. Run `python manage.py collectstatic`
5. Use a production database (PostgreSQL/MySQL) and a real web server (e.g. gunicorn + nginx)

## Project structure

```
ayan_portfolio/        Django project settings
portfolio/              The main app (models, admin, views, templates data)
templates/portfolio/    HTML templates
static/portfolio/       CSS and JavaScript
media/                  Uploaded files (CV, photos, project images)
generate_cv.py          Script used to generate the starter CV PDF
requirements.txt        Python packages needed
```
