from django.urls import path

from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("signup", views.patientsignup, name="signup"),
    path("register", views.registerPatient, name="registerPatient"),
    path("loginUser", views.loginUser, name="loginUser"),
    path("logout", views.logout, name="logout"),
    path("patient_dashboard", views.patient_dashboard_display, name="patient_dashboard_display"),
    path("doctor_dashboard", views.doctor_dashboard_display, name="doctor_dashboard_display"),
    path("hcadmin_dashboard", views.hcadmin_dashboard_display, name="hcadmin_dashboard_display"),
    path("accounts_dashboard", views.accounts_dashboard_display, name="accounts_dashboard_display"),
    path("form", views.form, name="form"),
    path("form/formsubmit",views.submitForm,name="formsubmit"),
    path("hcadmin_dashboard/acceptFormByHC", views.acceptFormByHC, name="acceptFormByHC"),
    path("hcadmin_dashboard/rejectFormByHC", views.rejectFormByHC, name="rejectFormByHC"),
    path("doctor_dashboard/acceptByDoctor", views.acceptByDoctor, name="acceptByDoctor"),
    path("doctor_dashboard/rejectByDoctor", views.rejectByDoctor, name="rejectByDoctor"),
    path("accounts_dashboard/acceptByAccounts", views.acceptByAccounts, name="acceptByAccounts"),
    path("accounts_dashboard/rejectByAccounts", views.rejectByAccounts, name="rejectByAccounts"),
    path("hcadmin_dashboard/signup_admin", views.adminsignup, name="adminsignup"),
    path("hcadmin_dashboard/register_any_user", views.register_any_user, name="register_any_user"),
    path("hcadmin_dashboard/register_any_user", views.register_any_user, name="register_any_user"),
    path("patient_dashboard/patient_profile", views.patient_profile, name="patient_profile"),
    path("patient_dashboard/patient_profile/update_patient_profile", views.update_patient_profile, name="update_patient_profile"),
]
