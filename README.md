<p>
for preparing you pc to setup the project run this command in your terminal:</p>
<h2>
  pip install django-browser-reload  </h2>

<p>
 and put this commands in the 'head' part of the html file:</p>
<h2>
{% load django_browser_reload %}
{% django_browser_reload_script %}
</h2>

<p>
this makes kind of HOT Reload or LIVE preview in the django and updates the htm in the browser while the file is being edited.</p>



# NOTES

-the limitations should be proccesed in every mini app due to the api provider's limits.
