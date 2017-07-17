{% if user.is_authenticated %}
urlpatterns = patterns('',
    :
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    :
)
{% endif %}
