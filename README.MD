# ***DevLobby*** Web application
 - A social network for developers.
 - Build with Django/python.
 - Django learning project.
 
 # Function
 - Login / Register (OAuth and integrate fb/google )
 - Create blog posts
 - Post status update
 - Message each other
 - Notification
 - Search function
 
 # URLs for registration module
 - admin/
 - tweetSearch/
 - accounts/ login/ [name='login']
 - accounts/ logout/ [name='logout']
 - accounts/ password_change/ [name='password_change']
 - accounts/ password_change/done/ [name='password_change_done']
 - accounts/ password_reset/ [name='password_reset']
 - accounts/ password_reset/done/ [name='password_reset_done']
 - accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
 - accounts/ reset/done/ [name='password_reset_complete']
 
Migrate DB:
 - docker-compose -f docker-compose.yml run web python manage.py migrate/makemigrations
 
Run DEV:
 - docker-compose -f docker-compose.yml up
 - docker-compose -f docker-compose.yml up --build
 
 Run PROD:
 - docker-compose -f docker-compose.prod.yml up