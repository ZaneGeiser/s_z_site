Hardware/Server Requirements:
*Project Server Requiremnts can be found in requirements.txt and can be installed
to local server with pipenv (reccomended)
"pipenv install requirements.txt"

Launch Web Application form Command Line with
"python manage.py runserver" #manage.py is the django start folder for this web app.
You will then be able to see the web app in browser at http://localhost:8000/
The Project is also running on Heroku at https://s-z-site.herokuapp.com
    In order to push up the live version use "git push heroku main"
    If heroku disconnected from git make sure logged into CLI "heroku login"
    Also to add Heroku app as a Git remote "heroku git:remote -a s-z-site"


Project Status:
NEXTSTEP: Add rich text feature to the blog content. Decide between Markdown, wagtail.io, and CKEditor's rich text field.

Thursday 17 Feb 2022
Project is live and running on Heroku.
profile pics are resized before AWS upload becasue I thought the AWS Lambda function was too hard (for now atleast.)

Wednesday 16 Feb 2022
Happy Birthday

Monday 6 December 2021
Made it to 1:08:40 on video 13 for deploying a linux server with linode. getting a 403 Forbidden.
I will need to check the git file from corey to check spelling on all steps to see where I went wrong.
Will be a very frustrating debug I suspect.
Also, I need to remove the DJANGO_PRIVATE_KEY in setting from git hub somehow. add to .Bash_profile then clean the existing repo.

Sunday 5 December 2021
Completed Part 11. Added Pagination and Pagination navigation to blog pages and user filterd blog views.
https://www.youtube.com/watch?v=acOktTcTVEQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=12

Friday 3 December 2021
Completed Part 10. Added User authenticated ability to create, update, delete, and Detail View their posts. Next Step:
https://www.youtube.com/watch?v=acOktTcTVEQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=11

Wednesday 1 December 2021
Completed Part 9 and git commits. Users can now update profile img, name, and email. Next Step:
https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=10

Friday 27 August 2021
I made it to the end of Video 6 and have a working user creation form.
https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3