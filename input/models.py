from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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

    project_ID = models.CharField(primary_key=True, max_length=5)
    project_Phase = models.CharField(max_length=50, choices=Project_Phase_Type)
    source_of_Funding = models.CharField(max_length=50, choices=Source_of_Funding_Type)
    funding_Received = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    year_Funding_Received = models.PositiveIntegerField(validators=[MinValueValidator(1900), MaxValueValidator(9999)])
    project_Status_Update = models.TextField()
    links_Report_Studies = models.URLField(max_length=250)
    links_Images = models.FileField(upload_to='linkImages/')
    input_POC_Last_Name = models.CharField(max_length=100)
    input_POC_First_Name = models.CharField(max_length=100)
    input_POC_Email = models.EmailField(max_length=254)
    input_Date = models.DateField(auto_now_add=True)
