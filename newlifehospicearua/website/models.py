from django.db import models

# Logo
class SiteLogo(models.Model):
    logo = models.ImageField(upload_to='logos/')
    alt_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return "Site Logo"

# Hero / Carousel images
class HeroImage(models.Model):
    image = models.ImageField(upload_to='hero/')
    caption = models.TextField(blank=True)

    def __str__(self):
        return self.caption[:20]
    
class WhyNelihaSection(models.Model):
    title = models.CharField(max_length=200, default="WHY NELIHA")
    description = models.TextField(blank=True, null=True)
    background_image = models.ImageField(upload_to="why_neliha/", blank=True, null=True)

    class Meta:
        verbose_name = "Why NELIHA Section"
        verbose_name_plural = "Why NELIHA Section"

    def __str__(self):
        return self.title

# Programs / Services
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    button_text = models.CharField(max_length=50, default='More...')

    def __str__(self):
        return self.title
class MembershipSection(models.Model):
    title = models.CharField(max_length=200, default="Become a Member")
    description = models.TextField(blank=True, null=True)
    button_text = models.CharField(max_length=50, default="Join Now")
    button_link = models.URLField(blank=True, null=True, help_text="URL to membership form or contact page")
    background_image = models.ImageField(upload_to="membership/", blank=True, null=True)

    class Meta:
        verbose_name = "Membership Section"
        verbose_name_plural = "Membership Section"

    def __str__(self):
        return self.title

# Partners
class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/')

    def __str__(self):
        return self.name

# Footer / Contact
class FooterContent(models.Model):
    address = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=50, blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
