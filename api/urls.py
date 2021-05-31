from django.urls import path

from .db_views.job_opening_views import job_opening_insert, job_opening_list, job_opening_detail
from .db_views.all_users_views import all_users_insert, all_users_list, all_users_detail
from .db_views.challenges_views import challenges_insert, challenges_list, challenges_detail
from .db_views.user_company_views import user_company_insert, user_company_list, user_company_detail
from .db_views.suggested_courses_views import suggested_courses_insert, suggested_courses_list, suggested_courses_detail
from .db_views.company_views import company_insert, company_list, company_detail
from .db_views.job_opening_has_suggested_courses_views import job_opening_has_suggested_courses_insert, job_opening_has_suggested_courses_list, job_opening_has_suggested_courses_detail
from .db_views.user_general_views import user_general_insert, user_general_list, user_general_detail
from .db_views.user_general_applies_job_opening_views import user_general_applies_job_opening_insert, user_general_applies_job_opening_list, user_general_applies_job_opening_detail
from .db_views.experience_views import experience_insert, experience_list, experience_detail

urlpatterns = [

    # Job Opening

    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('job_opening/insert/', job_opening_insert, name="job_opening_insert"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    path('job_opening/get_or_delete/<str:id>/',
         job_opening_detail, name="job_opening_detail"),

    # The method is only GET for this one
    path('job_opening/list', job_opening_list, name="job_opening_list"),



    # All Users

    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('all_users/insert/', all_users_insert, name="all_users_insert"),

    # The method is only GET for this one
    path('all_users/list', all_users_list, name="all_users_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    path('all_users/get_or_delete/<str:id>/',
         all_users_detail, name="all_users_detail"),

    # Challenges
    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('challenges/insert/', challenges_insert, name="challenges_insert"),

    # The method is only GET for this one
    path('challenges/list', challenges_list, name="challenges_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    #id1 = job_opening_id, id2 = order_number
    path('challenges/get_or_delete/<str:id>/<str:id2>/',
         challenges_detail, name="challenges_detail"),

    # user_company
    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('user_company/insert/', user_company_insert, name="user_company_insert"),

    # The method is only GET for this one
    path('user_company/list', user_company_list, name="user_company_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    path('user_company/get_or_delete/<str:id>/', user_company_detail,
         name="user_company_detail"),

    # suggested_courses
    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('suggested_courses/insert/', suggested_courses_insert,
         name="suggested_courses_insert"),

    # The method is only GET for this one
    path('suggested_courses/list', suggested_courses_list,
         name="suggested_courses_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    path('suggested_courses/get_or_delete/<str:id>/', suggested_courses_detail,
         name="suggested_courses_detail"),


    # company
    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('company/insert/', company_insert,
         name="company_insert"),

    # The method is only GET for this one
    path('company/list', company_list,
         name="company_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    path('company/get_or_delete/<str:id>/', company_detail,
         name="company_detail"),

    # job_opening_has_suggested_courses
    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('job_opening_has_suggested_courses/insert/', job_opening_has_suggested_courses_insert,
         name="job_opening_has_suggested_courses_insert"),

    # The method is only GET for this one
    path('job_opening_has_suggested_courses/list', job_opening_has_suggested_courses_list,
         name="job_opening_has_suggested_courses_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    path('job_opening_has_suggested_courses/get_or_delete/<str:id>/<str:id2>/', job_opening_has_suggested_courses_detail,
         name="job_opening_has_suggested_courses_detail"),




    # user_general
    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('user_general/insert/', user_general_insert,
         name="user_general_insert"),

    # The method is only GET for this one
    path('user_general/list', user_general_list,
         name="user_general_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    path('user_general/get_or_delete/<str:id>/', user_general_detail,
         name="user_general_detail"),

    # user_general_applies_job_opening
    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('user_general_applies_job_opening/insert/', user_general_applies_job_opening_insert,
         name="user_general_applies_job_opening_insert"),

    # The method is only GET for this one
    path('user_general_applies_job_opening/list', user_general_applies_job_opening_list,
         name="user_general_applies_job_opening_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted
    #id1 = username, id2 = job_id
    path('user_general_applies_job_opening/get_or_delete/<str:id>/<str:id2>/', user_general_applies_job_opening_detail,
         name="user_general_applies_job_opening_detail"),


    # experience
    # For this one you can GET (open this subdomain in the browser) to find out the JSON needed to store data in database
    # To insert data, use the INSERT method and send the JSON in the correct format
    path('experience/insert/', experience_insert,
         name="experience_insert"),

    # The method is only GET for this one
    path('experience/list', experience_list,
         name="experience_list"),

    # If the method is GET, then data with primary key id will be retrieved
    # If the method is DELETE, then data with primary key id will be deleted

    #id1 = order_no, id2 = username
    path('experience/get_or_delete/<str:id>/<str:id2>/', experience_detail,
         name="experience_detail")



]
