from django.contrib import admin
from .models import (
    HeroSection, Service, Collection, Arrival, AcademySection, GalleryItem,
    AboutHeroSection, AboutStory, AboutMissionVision, AboutValue, AboutReason, AboutCTA,
    AcademyHero, AcademyIntroduction, AcademyCourse, AcademyBenefit, AcademyTestimonial, AcademyCTA
)

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    list_filter = ['is_active']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']

@admin.register(Arrival)
class ArrivalAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']

@admin.register(AcademySection)
class AcademySectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(AboutHeroSection)
class AboutHeroSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(AboutStory)
class AboutStoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(AboutMissionVision)
class AboutMissionVisionAdmin(admin.ModelAdmin):
    list_display = ['mission_title', 'vision_title', 'is_active']

@admin.register(AboutValue)
class AboutValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(AboutReason)
class AboutReasonAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(AcademyHero)
class AcademyHeroAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(AcademyIntroduction)
class AcademyIntroductionAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']

@admin.register(AcademyCourse)
class AcademyCourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'level', 'price', 'order']
    list_editable = ['order']
    list_filter = ['level']

@admin.register(AcademyBenefit)
class AcademyBenefitAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']
    list_editable = ['order']

@admin.register(AcademyTestimonial)
class AcademyTestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'order']
    list_editable = ['order']

@admin.register(AcademyCTA)
class AcademyCTAAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
