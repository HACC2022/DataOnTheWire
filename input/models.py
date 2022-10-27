from django.db import models

# Create your models here.


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

    project_ID = models.CharField(max_length=5)
    project_Phase = models.CharField(max_length=50, choices=Project_Phase_Type)
    source_of_Funding = models.CharField(max_length=50, choices=Source_of_Funding_Type)
    funding_Received = models.DecimalField(max_digits=12, decimal_places=2)
    year_Funding_Received = models.IntegerField()
    project_Status_Update = models.TextField()
    links_report_studies = models.URLField(max_length=250)
    links_images = models.FileField(upload_to='linkImages/')
    inputPOC_lastname = models.CharField(max_length=100)
    inputPOC_firstname = models.CharField(max_length=100)
    inputPOC_email = models.EmailField(max_length=254)
    inputDate = models.DateField(auto_now_add=True)