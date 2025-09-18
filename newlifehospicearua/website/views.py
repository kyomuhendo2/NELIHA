from django.shortcuts import render
from .models import SiteLogo, HeroImage, Service, Partner, FooterContent,MembershipSection, WhyNelihaSection

def home(request):
    context = {
        'logo' : SiteLogo.objects.first(),
        'hero_images' : HeroImage.objects.all(),
        'services' : Service.objects.all(),
        'partners' : Partner.objects.all(),
        'footer' : FooterContent.objects.all(),
        'membership': MembershipSection.objects.first(),
        'why_neliha':WhyNelihaSection.objects.first(),
    }
    return render(request, "website/index.html", context)
