from django.db import models

# Create your models here.

class Student():
    email_username
    phone_number
    first_name
    last_name
    account_id
    social_media_info

# What is this? Why?
# DOCE, one of our major goals is to make it a destination online 
# social learning platform.
#   - can we integrate with each of these platforms? Weather today or, tomorrow?
#   - are their opportunities to pull? 
#       are their opportunities to push data/information/learning-experiences?
#
# TIME-CAPSULE: 
# from https://en.wikipedia.org/wiki/Social_media, 23.11.2017 (DE-DATE)
#   Most popular services
#   This is a list of the leading social networks based on number of active user accounts as of August
#   2017.[51]
#       Facebook: 2,047,000,000 users
#       YouTube: 1,500,000,000 users
#       WhatsApp: 1,200,000,000 users
#       Facebook Messenger: 1,200,000,000 users
#       WeChat: 938,000,000 users
#       QQ: 861,000,000 users
#       Instagram: 700,000,000 users
#       QZone: 638,000,000 users
#       Tumblr: 357,000,000 users
#       Twitter: 328,000,000 users
#       Sina Weibo: 313,000,000 users
#       Baidu Tieba: 300,000,000 users
#       Skype: 300,000,000 users
#       Viber: 260,000,000 users
#       Snapchat: 255,000,000 users
#       Line: 214,000,000 users
#       Pinterest 175,000,000 users
#
class StudentSocialMedia():
    # Paying tribute, ala godfather, goodfellas... ;) Danke Tom!
    has_github
    github_id
    
    has_facebook
    facebook_id

    has_youtube
    youtube_id
    
    has_whatsapp
    whatsapp_id
    
    # Feels a little robotic to me too but... ja wohl!
    has_facebookmessenger
    facebookmessenger_id 
    
    # https://www.wechat.com/en/
    has_wechat
    wechat_id

    # http://www.qq.com/ (CN)
    has_qq
    qq_id

    has_instagram
    instagram_id

    # https://qzone.qq.com/
    has_qzone
    qzone_id

    # https://www.tumblr.com/
    has_tumblr
    tumblr_id

    has_twitter
    twitter_id

    # http://overseas.weibo.com/
    has_sinaweibo
    sinaweibo_id

    # https://tieba.baidu.com
    has_baidutieba
    baidutieba_id

    has_skype    
    skype_id

    viber

    snapchat

    line


    has_linkedin
    linkedin_id
    
    has_pintrest
    pintrest_id

    has_xing
    xing_id

# Online Learning Sites for this student. - This might help us integrate lessons from other systems or, push our material to those systems as well.
class StudentOnlineLearning():
    # udemy, code academy, etc

class Teacher():
    classes_tought
    classes_current

class Class():
    teachers
    lessons

class Lesson():
    lesson_date
    lesson_start_time
    lesson_end_time
    tought_by
    students_in_attendance


    #
    # These two prperties are complex and rich but, it helps track 
    # overall class-room productivity. As well as, what the student 
    # should have learned but, didnt, that can be delivered in fragments 
    # via online lesson-bursts or, lesson-sessions


    source_lesson_plan # The original intent to be delivered as teachable units in the lesson
    lesson_delivered # What was actually taught - delivered to the students.

class LessonPlan:
    learnable_artifacts

class LessonDelivered:
    learnable_artifacts

# Components within a lesson plan - an invidiual teaching goal. A single learnable item. 
class LearnableArtifact(): 


# Superclass for: 
#   Notebooks, 
#   Notebook Groups, 
#   Notebook-Artifacts (such as cells or external referential components), 
#   Notebook-Artifact-groups.
class JupityerArtifact():

class JupityerNotebook():


class JupityerNotbookGroup():


# Captures an artifact wihin a JPNB that we which to model for referential purposes
class JupiterNotebookArifact():


JupiterNotebookArifactGroup
