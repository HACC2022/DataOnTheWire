from django.db import models

# Create your models here.


class ProjectFactSheet(models.Model):
    o01 = "O-01"
    o02 = "O-02"
    o03 = "O-03"
    o06 = "O-06"
    o07 = "O-07"
    o38 = "O-38"
    o40 = "O-40"
    o08 = "O-08"
    o09 = "O-09"
    o11 = "O-11"
    o13 = "O-13"
    o16 = "O-16"
    o20 = "O-20"
    o30 = "O-30"
    o33 = "O-33"
    k14 = "K-14"
    k03 = "K-03"
    k05 = "K-05"
    k07 = "K-07"
    k08 = "K-08"
    k13 = "K-13"
    h01 = "H-01"
    h06 = "H-06"
    m06 = "M-06"

    Project_ID_Type = (
        (o01, "O-01"),
        (o02, "O-02"),
        (o03, "O-03"),
        (o06, "O-06"),
        (o07, "O-07"),
        (o38, "O-38"),
        (o40, "O-40"),
        (o08, "O-08"),
        (o09, "O-09"),
        (o11, "O-11"),
        (o13, "O-13"),
        (o16, "O-16"),
        (o20, "O-20"),
        (o30, "O-30"),
        (o33, "O-33"),
        (k14, "K-14"),
        (k03, "K-03"),
        (k05, "K-05"),
        (k07, "K-07"),
        (k08, "K-08"),
        (k13, "K-13"),
        (h01, "H-01"),
        (h06, "H-06"),
        (m06, "M-06"),
    )

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

    project_ID = models.CharField(max_length=5, choices=Project_ID_Type)
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