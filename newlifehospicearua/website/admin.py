from django.contrib import admin
from .models import MembershipSection
from .models import SiteLogo, HeroImage, Service, Partner, FooterContent, WhyNelihaSection

admin.site.register(SiteLogo)
admin.site.register(HeroImage)
admin.site.register(Service)
admin.site.register(Partner)
admin.site.register(FooterContent)

@admin.register(WhyNelihaSection)
class WhyNelihaSectionAdmin(admin.ModelAdmin):
    list_display = ("title",)

@admin.register(MembershipSection)
class MembershipSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "button_text", "button_link")