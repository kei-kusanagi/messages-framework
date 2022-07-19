Pues empecemos a explorar esta bonita opción de los mensajes en Django, y no me refiero a un messenger como tal, me refiero a los mensajes que nos aparecen en la pagina al hacer un login o borrar algo.

https://youtu.be/MhUfgeWFgos

https://docs.djangoproject.com/en/4.0/ref/contrib/messages/

Iniciamos un nuevo proyecto de Django llamado "core" y una nueva app llamada "exploredjangomessages"

vamos a "settings.py" y aparte de registrar nuestra app "core" y checamos que este ya instalado el framework de messages

![image](IMG%20README/Pasted%20image%2020220718155824.png)


Los mensajes tienen diferentes niveles

![image](IMG%20README/Pasted%20image%2020220718161529.png)

Aqui usaremos lo que son los de SUCCESS , pero como usarlos? a pues como se muestra acotinuacion:

![image](IMG%20README/Pasted%20image%2020220718161632.png)

Vamos a views.py y añadimos 
```
from django.contrib import messages

from django.shortcuts import render

  

def index(request):

    messages.add_message(request, messages.INFO, 'Hello world.')

    return render(request, 'coore/idnex.html')


```

creamos un archivo index.html en la carpeta core/templates/core/index.html
![image](IMG%20README/Pasted%20image%2020220718183235.png)

declaramos su path en urls.py
```
from django.contrib import admin

from django.urls import path

  

from core import views

  

urlpatterns = [

    path('', views.index, name='index'),

    path('admin/', admin.site.urls),

]
```

y corremos el servidor ``python manage.py runserver``

![image](IMG%20README/Pasted%20image%2020220718183348.png)

pareciera que no pasa nada y que no aparece el mensaje que acabamos de poner verdad, pues para que aparesca necesitamos desplegarlo

![image](IMG%20README/Pasted%20image%2020220718183531.png)

así que vamos a nuestra pagina infdex.html y ponemos lo siguiente

```
...

<body>

    <section class="section">

        <h1 class="title">Explore Django | Messages</h1>

  

        {% if messages %}

            {% for message in messages %}

                <div>{{ message }}</div>

            {% endfor %}

        {% endif %}

    </section>

</body>

...
```

![image](IMG%20README/Pasted%20image%2020220718183902.png)


aparece una ves porque volví a corer el servidor, pero si quitamos ese código que acabamos de poner y refrescamos 3 veces y lo volvemos  aponer 

![image](IMG%20README/Pasted%20image%2020220718184121.png)

ya que nos dará ese mensaje cada que detecte la entrada a esa pagina, ahora añadiremos un mensaje de SUCCESS, vamos a views.py y ponemos lo siguiente

```
from django.contrib import messages

from django.shortcuts import render

  

def index(request):

    messages.add_message(request, messages.INFO, 'Hello world.')

    messages.success(request, 'Profile details updated.')

    return render(request, 'core/index.html')
```

podemos usar ``{{ message.tags }}`` para que nos imprima que tipo de mensaje es

![image](README%20d%2%20IMG/Pa0image%2020220718184730.png]] ![imag)(IMG%20README/Pasted%20image%2020220718184740.png)

ahora le pondremos un poco de estilo, asi que abriremos una style arriba de este codigo, para que  cada mensaje tenga diferente color de fondo

```

    <title>Explore Django | Messages</title>

  

    <style>

        .info {

            padding: 10px;

            background: blue;

        }

  

        .success {

            padding: 10px;

            background: green;

        }

    </style>

</head>

<body>

    <section class="section">

        <h1 class="title">Explore Django | Messages</h1>

        {% if messages %}

            {% for message in messages %}

                <div class="{{ message.tags }}">{{ message }}</div>

            {% endfor %}

        {% endif %}

    </section>

</body>

</html>
```

esto nos da como resultado

![image](IMG%20README/Pasted%20image%2020220718185246.png)

Ahora añadiremos extra message tags
![image](IMG%20README/Pasted%20image%2020220718185349.png)
vamos a views.py y añadimos las extra_tags, en este caso cada que "success" algo (en este caso el botón que pondremos de "submit") llamara este metodo de extra_tags

```
from django.contrib import messages

from django.shortcuts import render

  

def index(request):

    if request.method== 'POST':

        messages.success(request, 'Profile details updated.', extra_tags='notification')

  

    return render(request, 'core/index.html')
```

ahora vamos a index.html y añadimos el botón y so css

```
...

        .notification {

            margin: 20px;

            color: white;

        }

    </style>

</head>

<body>

    <section class="section">

        <h1 class="title">Explore Django | Messages</h1>

  

        <form method="post" action=".">

            {% csrf_token %}

  

            <button>Submit</button>

        </form>

        {% if messages %}
...
```

actualizamos y ya que quitamos el mensaje de info no pasa nada
![image](IMG%20README/Pasted%20image%2020220718190037.png)

pero si le damos al botón que acabamos de crear

![image](IMG%20README/Pasted%20image%2020220718191039.png)


y listo con esto terminamos, como dice el buen Stein en su video, si queremos usar mas o adentrarnos mal al tema esta el link a la documentación

https://docs.djangoproject.com/en/4.0/ref/contrib/messages/

intentaremos una nueva funcionalidad para implementarla en el proyecto de Ecommerce https://github.com/kei-kusanagi/Ecommerce

para esto usaremos la pagina https://sweetalert2.github.io
![image](IMG%20README/Pasted%20image%2020220719103203.png)

para esto, tenemos que añadir ya sea un ``npm install sweetalert2`` o para términos de practicar mejor con su CDN ``<script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>``
![image](IMG%20README/Pasted%20image%2020220719103916.png)
Este lo pondremos justo antes de usar el script, o en dado caso en nuestro archivo base.html si lo tuviéramos, en este proyecto solo tenemos el index así que lo pondremos allí quitando nuestro anterior `<style>` que habíamos creado para estos mensajes
```
...

    <title>Explore Django | Messages</title>

</head>

<body>

    <section class="section">

        <h1 class="title">Explore Django | Messages</h1>

  

        <form method="post" action=".">

            {% csrf_token %}

  

            <button>Submit</button>

        </form>

        <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>

        {% if messages %}

            {% for message in messages %}
...
```

ahora en donde tenemos nuestro if para mostrar los mensajes, quitamos el `<div>` y ponemos nuestro nuevo `<script>` según la documentación
![image](IMG%20README/Pasted%20image%2020220719104019.png)

solo que le cambiaremos para que el icono sea el de 'success', el 'title' sea nuestros `{{ message.tags }}` y el 'text' sea el `{{ message }}` basado en el framework de mensajes de Django que estamos viendo

```
...
<body>

    <section class="section">

        <h1 class="title">Explore Django | Messages</h1>

        <form method="post" action=".">

            {% csrf_token %}

            <button>Submit</button>

        </form>

        <script src="//cdn.jsdelivr.net/npm/sweetalert2@11"></script>

        {% if messages %}

            {% for message in messages %}

                <script>
                    Swal.fire({

                        title: "{{ message.tags }}"

                        text: "{{ message }}",

                        icon: 'success',
                    })

                </script>

            {% endfor %}

        {% endif %}

    </section>

</body>

...
```
![image](IMG%20README/Pasted%20image%2020220719110312.png)

ahora si damos en el botón de Submit nos saldrá una bonita animación
![image](IMG%20README/Pasted%20image%2020220719104709.png)

Ahora a jugar con las demás mensajes que podemos poner e implementarlo en nuestra pagina de Ecommerce 😁