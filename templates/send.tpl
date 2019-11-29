{% extends 'interface.html' %}

{% block content %}
<form method="POST">
    <div>
        <textarea rows="4" cols="50" name="messege" required>
        </textarea>
    </div>
    <div>
        <input name="receiver" type=text required>
    </div>
    <div>
        <input type="submit" value="Submit">
    </div>
</form>
{% endblock %}