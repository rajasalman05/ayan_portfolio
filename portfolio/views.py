import json

from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Profile, SkillCategory, Education, Project, Certificate, ContactMessage


def index(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, "Thanks! Your message has been sent - Ayan will get back to you soon.")
        else:
            messages.error(request, "Please fill in your name, email, and message.")
        return redirect("index" if not request.GET.get("next") else request.GET.get("next"))

    profile = Profile.objects.first()
    context = {
        "profile": profile,
        "roles_json": json.dumps(profile.role_list()) if profile else "[]",
        "skill_categories": SkillCategory.objects.prefetch_related("skills"),
        "education": Education.objects.all(),
        "projects": Project.objects.filter(featured=True),
        "certificates": Certificate.objects.all(),
    }
    return render(request, "portfolio/index.html", context)
