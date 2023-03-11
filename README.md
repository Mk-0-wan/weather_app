how to connect tailwind with django
create a folder where you will store all the static files
go to settings and make a new STATICFILES_DIRS = [
	#you will provide the full path to that directory you have created
	BASE_DIR /"static"
]
BASE_DIR are not dependent on the local machine paths but universal to any other machines who will be trying out your project

STATIC_ROOT = BASE_DIR.parent / "local-cdn"/"static"

when in debug mode wanna make sure your using the original static
urls-> settings
from django.conf import settings


if settings.DEBUG:
	from djnago.conf.urls.static import static
	all these stuff in the try djnago -- or in the django documentation
	urlspatterns += static(settings.STATIC_URLS, document_root=settings.STATIC_ROOT)

to be able to have and input.css and output.css the same way with tailwind in order for them to be able to merge

static file for css
templates/weather/base.html for html files
templates/head/css.html or js.html files containing the links between the css and html files
href = {% static 'custom/custom.css' %} the file path where the css files are contained
go back to the base.html and add a tag which includes the css files with the href


