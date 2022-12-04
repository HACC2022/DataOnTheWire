from django.core.mail import send_mail
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
from django.db.models.signals import pre_save
from django.dispatch import receiver

from dataonthewire import settings
from users.models import User


class ProjectFactSheet(models.Model):
    prePlan = "Pre-Planning"
    plan = "Planning"
    des = "Design"
    planDes = "Plan/Design"
    comp = "Completed"
    eaDes = "EA/Design"
    constr = "Construction"
    desConstr = "Des/Constr"
    planDesConstr = "Plan/Des/Constr"

    Project_Phase_Type = (
        (prePlan, "Pre-Planning"),
        (plan, "Planning"),
        (des, "Design"),
        (planDes, "Plan/Design"),
        (comp, "Completed"),
        (planDes, "EA/Design"),
        (constr, "Construction"),
        (desConstr, "Des/Constr"),
        (planDesConstr, "Plan/Des/Constr"),
    )

    gf = "General Fund"
    sf = "Special Fund"
    gb = "GO Bonds"
    gbr = "GO Bonds Repaid"
    rb = "Revenue Bonds"
    fedi = "FED & Interstate"
    fedp = "FED & Primary"
    feds = "FED & Secondary"
    fedu = "FED & Urban"
    ofed = "Other FED Funds"
    fedrs = "FED Revenue Sharing"
    pc = "Private Contributions"
    cf = "County Funds"
    tf = "Trust Funds"
    it = "Interdept Transfer"
    rf = "Revolving Fund"
    of = "Other Funds"

    Source_of_Funding_Type = (
        (gf, "General Fund"),
        (sf, "Special Fund"),
        (gb, "GO Bonds"),
        (gbr, "GO Bonds Repaid"),
        (rb, "Revenue Bonds"),
        (fedi, "FED & Interstate"),
        (fedp, "FED & Primary"),
        (feds, "FED & Secondary"),
        (fedu, "FED & Urban"),
        (ofed, "Other FED Funds"),
        (fedrs, "FED Revenue Sharing"),
        (pc, "Private Contributions"),
        (cf, "County Funds"),
        (tf, "Trust Funds"),
        (it, "Interdept Transfer"),
        (rf, "Revolving Fund"),
        (of, "Other Funds"),
    )

    project_ID = models.CharField(primary_key=True, max_length=5)
    project_Phase = models.CharField(max_length=50, choices=Project_Phase_Type)
    source_of_Funding = models.CharField(max_length=50, choices=Source_of_Funding_Type)
    funding_Received = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    year_Funding_Received = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(9999)])
    project_Status_Update = models.TextField()
    links_Report_Studies = models.URLField(max_length=250)
    links_Images = models.FileField(upload_to='linkImages/', blank=True)
    input_POC_Last_Name = models.CharField(max_length=100)
    input_POC_First_Name = models.CharField(max_length=100)
    input_POC_Email = models.EmailField(max_length=254)
    input_Date = models.DateField(auto_now_add=True)
    approved_by_staff = models.BooleanField(default=False)
    rejected_by_staff = models.BooleanField(default=False)


@receiver(pre_save, sender=ProjectFactSheet, dispatch_uid='active')
def approved(sender, instance, **kwargs):
    if instance.approved_by_staff and ProjectFactSheet.objects.filter(pk=instance.pk, approved_by_staff=False).exists():
        subject = 'Sheet %s Approved' % instance.project_ID
        message = '%s your sheet has been approved' % instance.input_POC_First_Name
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [instance.input_POC_Email], fail_silently=False)
    if instance.rejected_by_staff and ProjectFactSheet.objects.filter(pk=instance.pk, rejected_by_staff=False).exists():
        subject = 'Sheet %s Rejected' % instance.project_ID
        message = '%s your sheet has been rejected, please review the information entered' % instance.input_POC_First_Name
        from_email = settings.EMAIL_HOST_USER
        send_mail(subject, message, from_email, [instance.input_POC_Email], fail_silently=False)
    if not instance.rejected_by_staff and ProjectFactSheet.objects.filter(pk=instance.pk, rejected_by_staff=True).exists():
        subject = 'Sheet %s updated' % instance.project_ID
        message = 'Sheet %s has been updated, please review the information and approve or reject' % instance.project_ID
        from_email = settings.EMAIL_HOST_USER
        # users = User.objects.get(is_staff=True)
        staff_mails = "bjarne.martens@icloud.com"
        send_mail(subject, message, from_email, [staff_mails], fail_silently=False)
