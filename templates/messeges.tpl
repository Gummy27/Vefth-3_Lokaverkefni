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
        <ol>
        {% for messege in messeges %}
            <ul>
                <p>Breyta</p>
            </ul>
        {% endfor %}
        </ol>
        <ol>
        {% for messege in messeges %}
            <ul>
                <p>Eyða</p>
            </ul>
        {% endfor %}
        </ol>
    </div>
</main>
{% endblock %}