from django.db import models


class Profile(models.Model):
    """Singleton-style profile - one row holds all hero/about content, editable from admin."""
    full_name = models.CharField(max_length=120, default="Muhammad Ayan Abbasi")
    role_titles = models.CharField(
        max_length=255,
        default="Python Developer, Django Developer, AI & Data Science Enthusiast",
        help_text="Comma-separated roles shown in the animated terminal typing effect.",
    )
    tagline = models.CharField(max_length=255, blank=True,
        default="Intermediate Computer Science student building things with code and data.")
    about = models.TextField(blank=True)
    profile_photo = models.ImageField(upload_to="profile/", blank=True, null=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=120, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    whatsapp_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    cv_file = models.FileField(upload_to="cv/", blank=True, null=True,
        help_text="Upload the CV PDF here to power the Download CV button.")
    years_learning = models.PositiveIntegerField(default=2)
    projects_completed = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Profile (site owner)"
        verbose_name_plural = "Profile (site owner)"

    def __str__(self):
        return self.full_name

    def role_list(self):
        return [r.strip() for r in self.role_titles.split(",") if r.strip()]


class SkillCategory(models.Model):
    name = models.CharField(max_length=80)
    icon = models.CharField(max_length=10, blank=True, help_text="Emoji or short glyph, e.g. snake")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]
        verbose_name_plural = "Skill categories"

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField(max_length=80)
    proficiency = models.PositiveIntegerField(default=70, help_text="0-100")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"


class Education(models.Model):
    degree = models.CharField(max_length=200, help_text="e.g. Intermediate (Computer Science)")
    institute = models.CharField(max_length=200)
    year = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=255, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]
        verbose_name_plural = "Education"

    def __str__(self):
        return f"{self.degree} - {self.institute}"


class Project(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tech_stack = models.CharField(max_length=255, help_text="Comma-separated, e.g. Django, Python, SQLite")
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    project_url = models.URLField(blank=True)
    repo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "-id"]

    def __str__(self):
        return self.title

    def tech_list(self):
        return [t.strip() for t in self.tech_stack.split(",") if t.strip()]


class Certificate(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=150, blank=True)
    year = models.CharField(max_length=20, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.name} - {self.subject or 'No subject'}"
