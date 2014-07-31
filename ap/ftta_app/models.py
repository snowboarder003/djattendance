from django.db import models

from accounts import Applicant, Elder
from localities import Locality

from datetime import datetime

""" FTTA_APP models.py

This module catalogs all pertinent data associated with the FTTA application 
and contains most of the data that will be used by the other modules contained
in Djattendance.

Data Models:
    - Application: all the data associated to the applicant.
    - EmailTemplates: email template content
    - EmailProgress: data related to the progress of an application
"""

class Application(models.Model):
    """ An application can be either fulltime application, or short term application.
    Every applicant may have at most application of one type.
    """

    # each user should only have one of each profile
    person_applying = models.OneToOneField(Applicant)

    # each user has a sending locality and possibly another locality
    sent_by = models.OneToOneField(Locality)
    other_sender = models.OneToOneField(Locality)

    class Meta:
        abstract = True


class EmailTemplates(models.Model):
    #
    code = models.CharField(max_length=3)
    name = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    attachment = models.FilePathField(path="/ap", recursive=True)


class EmailProgress(models.Model):

    # elders recommendation
    elders_rec_submission = models.BooleanField()

    # Acknowledgement to Applicant
    ack_email = models.BooleanField()
        
    # Reminder to Applicant for Elder's Recommendation  
    elders_reminder = models.BooleanField()
    
    # Acceptance to Applicant
    accept_email = models.BooleanField()

    # Trainee Acceptance to Elders    
    elder_email = models.BooleanField()
    
    # Provisional Acceptance to Applicant    
    provisional_email = models.BooleanField()

    # Mentor Instructions    
    mentor_email = models.BooleanField()

    # Not finished Bible reading requirement reminder
    bible_requirement_email = models.BooleanField()

    # each set of email checks is mapped to one application
    application_progress = models.OneToOneField(Application)


class Recommendation():

    # the content of the recommendation
    description = models.TextField(blank=True, null=True)

    # date the recommendation is submitted
    recommendation_date_time = models.DateTimeField(default=datetime.now)

    # many recommendations are all mapped to one elder
    elder_recommending = models.ForeignKey(Elder)

    # each recommendation is mapped to one application
    applicant_recommended = models.OneToOneField(Application)

    def getContent(self):
        return self.description

    #connect with elder's information    
    def __unicode__(self):
        return u"the recommendation by %s" % elder_recommending



class HealthPackage(models.Model):

    # many health packages are mapped to many medical officers
    fully_approved = models.BooleanField()
    in_fellowship = models.BooleanField()
    need_tb = models.BooleanField()
    description = models.TextField(blank=True, null=False)

    # each package is mapped to one application
    medical_status_of_application = models.OneToOneField(Application)


class InternationalPackage(models.Model):
    # international forms helpers have access to the status of this set of forms (one for each application) 
    overall_visa = models.BooleanField(default=False)
    i_twenty = models.BooleanField(default=False)
    financial_statement = models.BooleanField(default=False)
    affidavit_support = models.BooleanField(default=False)
    supporting_docs = models.BooleanField(default=False)
    academic_qualification = models.BooleanField(default=False)
    proof_of_english = models.BooleanField(default=False)
    processing_fee = models.BooleanField(default=False)
    comments = models.TextField(blank=True, null=False)

    # each package is mapped to one application while an app may not have international package
    international_forms_application = models.ForeignKey(Application)


class Approval(models.Model):
    # 
    ay_approval = models.BooleanField()
    dh_approval = models.BooleanField()
    overall_approval = models.BooleanField()
    comments = models.TextField(blank=True, null=False)

    # each package is mapped to one application
    application_approval = models.OneToOneField(Application)


class FTApplication(Application):
    
    def __unicode__(self):
        return self.personApplying.account.get_full_name()


class FTAppPersonalInfo(models.Model):
    # one AppPersonalInfo is mapped to oneFApplication
    SUFFIXES = (
        ('J', 'Jr.'),
        ('R', 'Sr.'),
        ('T', 'III'),
        ('F', 'IV')
    )

    TWIN = (
        ('Y', 'Yes'),
        ('N', 'No'),
        ('T', 'Not yet sure')
    )

    TEAM = (
        ('C', 'Campus'),
        ('Y', 'Young People'),
        ('H', 'Children'),
        ('M', 'Community')
    )

    LANG = (
        ('GO', 'Greek I'),
        ('GT`', 'Greek II'),
        ('CH', 'Character')
    )

    suffix = models.CharField(max_length=3, choices= SUFFIXES)
    maiden_name = models.CharField(max_length=35)
    terms_completed = models.CharField(max_length=12)
    homephone = models.CharField(max_length=15)
    homephone_inter = models.CharField(max_length=15)
    cellphone_inter = models.CharField(max_length=15)
    us_citizen = models.BooleanField()
    citizenship = models.CharField(max_length=36)
    skype_acct = models.CharField(max_length=32)
    twitter_acct = models.CharField(max_length=15)
    bring_auto = models.BooleanField()
    plan_for_two_years = models.CharField(max_length=12, choices=TWIN)
    plan_not_two_years_exp = models.TextField(blank=True, null=False)
    english_ability_difficulty = models.BooleanField()
    other_languages_fluent = models.TextField(blank=True, null=False)
    supported_financially_by = models.CharField(max_length=15)
    gospel_team_pref_one = models.CharField(max_length=12,choices=TEAM)
    gospel_team_pref_two = models.CharField(max_length=12,choices=TEAM)
    greek_or_character = models.CharField(max_length=9, choices=LANG)
    other_pertinent_info = models.TextField(blank=True, null=False)
    consecration_agreement = models.BooleanField()

    # each dataset is mapped to an application
    personalOwnerApp = models.OneToOneField(FTApplication)


class FamilyInfo(models.Model):
    # one familyinfo is mapped to oneFTApplication
    MARITAL = (
        ('G', 'Single'),
        ('R', 'Married'),
        ('E', 'Engaged'),
        ('D', 'Divorced/Separated')
    )

    ATTITUDE = (
        ('A', 'Agree'),
        ('B', 'Disagree'),
        ('T', 'Also burdened to be full-time'),
    )

    marital_status = models.CharField(max_length=18, choices=MARITAL)
    spouse_name = models.CharField(max_length=70)
    marriage_date = models.DateField(auto_now=False, auto_now_add=False)
    spouse_occupation = models.CharField(max_length=70)
    spouse_age = models.IntegerField()
    spouse_attitude = models.CharField(max_length=29, choices=ATTITUDE)
    spouse_attend = models.BooleanField()
    spouse_plan = models.TextField(blank=True, null=False)
    dependents = models.IntegerField()

    # each package is mapped to one applicationlication (one type)
    family_info = models.OneToOneField(FTApplication)


class Skill(models.Model):
    # one skill is mapped to oneFTApplication
    av = models.BooleanField()
    auto_repair = models.BooleanField()
    carpentry = models.BooleanField()
    computer_database = models.BooleanField()
    computer_hardware = models.BooleanField()
    computer_networking = models.BooleanField()
    computer_programming = models.BooleanField()
    eletrical = models.BooleanField()
    facility_maint = models.BooleanField()
    floor_covering = models.BooleanField()
    gardening = models.BooleanField()
    graphic_design = models.BooleanField()
    landscaping = models.BooleanField()
    med_training = models.BooleanField()
    photo = models.BooleanField()
    picture_framing = models.BooleanField()
    plumbing = models.BooleanField()
    prof_writing = models.BooleanField()
    security_safety = models.BooleanField()
    sewing = models.BooleanField()
    web_programming = models.BooleanField()
    other = models.TextField(blank=True, null=False)

    # each skill package is mapped to one application (one type)
    skill_list = models.OneToOneField(FTApplication)

class WorkExperience(models.Model):
    # one workexperience is mapped to oneFTApplication
    occupation = models.CharField(max_length=50)

    # each workpackage is mapped to one application (one type)
    work_info = models.OneToOneField(FTApplication)

class Testimony(models.Model):
    # one testimony is mapped to oneFTApplication
    content = models.TextField(blank=True, null=False)

    # each testimony is mapped to one application (one type)
    testimony = models.OneToOneField(FTApplication)

class Education(models.Model):
    # one education is mapped to oneFTApplication

    DEGREEBACH = (
        ('B', 'Bachelor'),
        ('A', 'Associate'),
        ('X', 'None')
    )

    DEGREEGRAD = (
        ('M', 'Master'),
        ('P', 'Ph.D'),
        ('O', 'Other')
    )

    bachelor_degree = models.BooleanField()
    bachelor_univ = models.CharField(max_length=82)
    bachelor_country = models.CharField(max_length=36)
    major = models.CharField(max_length=50)
    degree_type = models.CharField(max_length=9, choices=DEGREEBACH)
    grad_date = models.DateField(auto_now=False, auto_now_add=False)
    grad_univ = models.CharField(max_length=82)
    grad_country = models.CharField(max_length=36)
    grad_major = models.CharField(max_length=50)
    grad_type = models.CharField(max_length=6, choices=DEGREEGRAD)

    # each education package is mapped to one application (one type)
    education_info = models.OneToOneField(FTApplication)

class Immunization(models.Model):
    # one immunization is mapped to oneFTApplication
    tdap = models.DateField(auto_now=False, auto_now_add=False)
    hep_A_one = models.DateField(auto_now=False, auto_now_add=False)
    hep_A_two = models.DateField(auto_now=False, auto_now_add=False)
    hep_B_one = models.DateField(auto_now=False, auto_now_add=False)
    hep_B_two = models.DateField(auto_now=False, auto_now_add=False)
    hep_B_three = models.DateField(auto_now=False, auto_now_add=False)
    tb_skin = models.DateField(auto_now=False, auto_now_add=False)
    tb_result = models.TextField(blank=True, null=False)
    chest_xray = models.DateField(auto_now=False, auto_now_add=False)
    xray_result = models.TextField(blank=True, null=False)
    mmr_one = models.DateField(auto_now=False, auto_now_add=False)
    mmr_two = models.DateField(auto_now=False, auto_now_add=False)
    tb_comments = models.TextField(blank=True, null=False)

    # each immunization package is mapped to one application (one type)
    immune_info = models.OneToOneField(FTApplication)

class History(models.Model):
    # one history is mapped to oneFTApplication
    date_saved = models.DateField(auto_now=False, auto_now_add=False)
    date_baptized = models.DateField(auto_now=False, auto_now_add=False)
    raised_in_church = models.BooleanField()
    came_to_church = models.DateField(auto_now=False, auto_now_add=False)
    first_locality = models.CharField(max_length=30)
    service_area = models.CharField(max_length=42)
    been_in_ftta = models.BooleanField()
    which_ftt = models.CharField(max_length=22)
    past_ftt = models.DateField(auto_now=False, auto_now_add=False)
    read_ot = models.BooleanField()
    read_nt = models.BooleanField()
    ever_criminal = models.BooleanField()
    consent = models.BooleanField()

    # each history package is mapped to one application (one type)
    history_info = models.OneToOneField(FTApplication)

class Healthinfo(models.Model):
    # one healthinfo is mapped to oneFTApplication

    FREQ = (
        ('L', 'Less than 3'),
        ('S', '3 or more'),
    )

    healthy = models.BooleanField()
    allergic_to_meds = models.BooleanField()
    allergies_to_meds = models.TextField(blank=True, null=False)
    taking_meds = models.BooleanField()
    allergic_to_food_salmon = models.BooleanField()
    allergic_to_food_tilapia = models.BooleanField()
    allergic_to_food_tuna = models.BooleanField()
    allergic_to_food_cod = models.BooleanField()
    allergic_to_food_gluten = models.BooleanField()
    allergic_to_food_gluten_exc = models.TextField(blank=True, null=False)
    allergic_to_food_others = models.TextField(blank=True, null=False)
    chronic_illness = models.BooleanField()
    physical_disability = models.BooleanField()
    back_discomfort = models.BooleanField()
    surgery = models.BooleanField()
    diagnosis_advice = models.BooleanField()
    illnesses_peptic_ulcer = models.BooleanField()
    illnesses_tbc = models.BooleanField()
    illnesses_hep = models.BooleanField()
    illnesses_heart_disease = models.BooleanField()
    illnesses_kidney_disease = models.BooleanField()
    illnesses_cancer = models.BooleanField()
    illnesses_high_bp = models.BooleanField()
    illnesses_asthma = models.BooleanField()
    illnesses_other = models.BooleanField()
    hospitalized_phys = models.BooleanField()
    phys_hospital_comm = models.TextField(blank=True, null=False)
    hospitalized_ment = models.BooleanField()
    mental_hospital_comm = models.TextField(blank=True, null=False)
    psych_care_advised = models.BooleanField()
    ever_thought_harm_self = models.BooleanField()
    diff_adjust = models.BooleanField()
    diff_sleep = models.BooleanField() 
    diff_back_to_sleep = models.BooleanField()
    anxiety_health_effect = models.BooleanField()
    anxiety_appetite_effect = models.BooleanField()
    anxiety_sleep_effect = models.BooleanField()
    anxiety_school_effect = models.BooleanField()
    anxiety_church_family_effect = models.BooleanField()
    panic_attack = models.BooleanField()
    unusual_fear = models.BooleanField()
    depressed = models.BooleanField()
    no_pleasure = models.BooleanField()
    no_concentration = models.BooleanField()
    diff_decision = models.BooleanField()
    too_energetic = models.BooleanField()
    too_tired = models.BooleanField()
    greater_appetite = models.BooleanField()
    sleeping_more = models.BooleanField()
    no_self_value_comp = models.BooleanField()
    angry_outburst = models.BooleanField()
    reckless_spending = models.BooleanField()
    trouble_others = models.BooleanField()
    phys_exam_recent = models.BooleanField()
    phys_exam_info = models.TextField(blank=True, null=False)
    chest_xray = models.BooleanField()
    chest_xray_info = models.TextField(blank=True, null=False)
    bad_cough = models.BooleanField()
    colds = models.CharField(max_length=11, choices=FREQ)
    days_school_lost = models.IntegerField()
    days_school_lost_last_year = models.IntegerField()
    recent_weight_change = models.BooleanField()
    satisfied_eating_pattern = models.BooleanField()
    weight_affect_self = models.BooleanField()
    secret_eating = models.BooleanField()
    eating_disorder_family = models.BooleanField()
    eating_disorder_self = models.BooleanField()
    computer_act = models.BooleanField()
    used_tobacco = models.BooleanField()
    used_tobacco_info = models.TextField(blank=True, null=False)
    used_alchohol = models.BooleanField()
    used_alchohol_info = models.TextField(blank=True, null=False)
    used_habit_drugs = models.BooleanField()
    used_habit_drugs_info = models.TextField(blank=True, null=False)
    last_alcohol = models.CharField(max_length=16)
    affect_training = models.BooleanField()
    extent_effect = models.TextField(blank=True, null=False)
    last_dentist = models.CharField(max_length=16)
    dental_work = models.BooleanField()
    spouse_attend = models.BooleanField()
    spouse_name = models.CharField(max_length=70)
    spouse_attending = models.BooleanField()
    height = models.CharField(max_length=25)
    weight = models.CharField(max_length=25)
    bp_measured_recent = models.BooleanField()
    bp_info = models.CharField(max_length=25)
    emerg_contact_name = models.CharField(max_length=70)
    emerg_contact_addr = models.CharField(max_length=70)
    emerg_contact_phone_one = models.CharField(max_length=15)
    emerg_contact_phone_two = models.CharField(max_length=15)
    emerg_email = models.EmailField(max_length=255)
    consent_insurance = models.BooleanField()
    insurance_type = models.TextField(blank=True, null=False)
    insurance_details = models.TextField(blank=True, null=False)

    # each health package is mapped to one application (one type)
    health_info = models.OneToOneField(FTApplication)

class STApplication(Application):
    
    def __unicode__(self):
        return self.personApplying.account.get_full_name()

class Choice(models.Model):
    # one choice is mapped to oneSTApplication

    arriving_by = models.CharField(max_length=8)
    gospel_team_pref = models.CharField(max_length=12)
    need_housing = models.BooleanField()
    good_physical = models.BooleanField()
    physical_comments = models.TextField(blank=True, null=True)
    have_disabilities = models.BooleanField()
    disabilities_comments = models.TextField(blank=True, null=True)

    # each choice package is mapped to one application (one type)
    choices_st_applicant = models.OneToOneField(STApplication)

class STAppPersonalInfo(models.Model):
    # one STAppPersonalInfo is mapped to oneSTApplication

    name = models.CharField(max_length=70)
    age = models.IntegerField()
    occupation = models.TextField(blank=True, null=False)
    arrival = models.DateField(auto_now=False, auto_now_add=False)
    arrival_time = models.TimeField(auto_now=False, auto_now_add=False)
    departure = models.DateField(auto_now=False, auto_now_add=False)
    departure_time = models.TimeField(auto_now=False, auto_now_add=False)
    saved = models.DateField(auto_now=False, auto_now_add=False)
    baptized = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=7)
    homephone = models.CharField(max_length=15)
    cellphone = models.CharField(max_length=15)

    # each package is mapped to one application
    personal_info_st_applicant = models.OneToOneField(STApplication)

class Agreement(models.Model):
    # one agreement is mapped to one STApplication

    transport = models.BooleanField()
    cease_time = models.BooleanField()
    automatic_less_than_a_week = models.BooleanField()
    room_board = models.BooleanField()
    no_hospitality_after = models.BooleanField()
    
    # each package is mapped to one application
    agreement_st_applicant = models.OneToOneField(STApplication)