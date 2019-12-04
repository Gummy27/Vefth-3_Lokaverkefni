{% extends 'interface.html' %}

{% block content %}
<h1>Skilaboð:</h1>
<main>
    <div class="accounts">
        <ol>
        {% for messege in messeges %}
            <ul>
                <p>{{ usernames[messege['poster']-1] }}</p>
            </ul>
        {% endfor %}
        </ol>
        <ol>
        {% for messege in messeges %}
            <ul>
                <p>{{ messege['messege'] }}</p>
            </ul>
        {% endfor %}
        </ol>
        {% if changes %}
            <ol>
            {% for messege in messeges %}
                <ul>
                    <a href="/signedIn/change/{{messege['id']}}"><p>Breyta</p></a>
                </ul>
            {% endfor %}
            </ol>
            <ol>
            {% for messege in messeges %}
                <ul>
                    <a href="/signedIn/delete/{{messege['id']}}"><p>Eyða</p></a>
                </ul>
            {% endfor %}
            </ol>
        {% endif %}
    </div>
</main>
{% endblock %}