from django.contrib import admin
from .models import Profile, SkillCategory, Skill, Education, Project, Certificate, ContactMessage


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "location")

    def has_add_permission(self, request):
        # Keep this a singleton so the site always has exactly one active profile.
        return Profile.objects.count() == 0


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "icon", "order")
    inlines = [SkillInline]


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "proficiency", "order")
    list_filter = ("category",)
    list_editable = ("proficiency", "order")


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institute", "year", "order")
    list_editable = ("order",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "featured", "order")
    list_editable = ("featured", "order")
    list_filter = ("featured",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("title", "issuer", "year", "order")
    list_editable = ("order",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at", "is_read")
    list_filter = ("is_read",)
    readonly_fields = ("name", "email", "subject", "message", "created_at")
