# Requeriments per a poder començar a programar

## Instalar Python
1. Per a comprovar si el teniu instal·lat, proveu a escriure `python` al terminal de windows. En cas de que no el tingueu (i estigueu a windows 11) us portarà a la microsoft Store, on us dirà si voleu instalar python.
2. Allà, li doneu a _obtener_ i us instal·larà la ultima versió de python.
3. Torneu a provar a utilitzar la comanda `python` al terminal i veureu com us surt la versió i unes fletxetes.
4. En un altre terminal, proveu a posar `pip` i us sortirà les diferents opcions. Si us surten aquestes coses, es que ho teniu ben instal·lat.

## Instalar Django
1. Obrir un terminal de windows
2. Posar la següent comanda: pip install Django
3. Per veure si s'ha instalat correctament, posar en el terminal python
4. Escriure en el interpreter que es posa les següents linies:
```python
import django
django.VERSION
```
5. Si ens surt la versió, vol dir que s'ha instalat correctament.

## Instalar PyCharmProfessional
Si voleu podeu usuar el Community, però ja que sou estudiants, jo de vosaltres aprofitaria per demanar llicencia i utilitzar la versió pro, que ofereix moltes més eines.
1. Demanar compte estudiant a [Jetbrains](https://www.jetbrains.com/shop/eform/students) (no cal si ja l'heu demanat abans)
2. Descarregar-se el Pycharm Professional
3. Un cop instalat, obriu-lo i us apareixerà una finestra com aquesta:
![Imagen Pantalla inicial PyCharm](https://i.imgur.com/Z2vlOHc.png)
4. Un cop en aquesta finestra, li donarem clic a Get from VCS
5. Ens sortirà una altra finestra, i li donarem a GitHub, on linkejarem amb el nostre compte que té el projecte compartit.
6. Un cop loguejats, ens sortirà una llista dels projectes que tenim, i allà seleccionarem el `crismigo/Hacker-News-HN22D`.
7. A directory posarem el directori on volem que se'ns guardi i li donarem a clone.
![Imagen Seleccio projecte](https://i.imgur.com/WR0fkgE.png)
8. Se'ns obrirà el projecte, on tot hauria d'estar configurat. si us diu que instaleu quelcom, feu-ho.

## Instalar llibreries necessaries
Us recomano crear-vos un virtual environment, aixi no se us fa malbé el python local. Per a fer-ho, heu d'anar a pycharm i a `Add Configurations`, i allà seleccionar que el python que voleu utilitzar es el venv
1. Anar al fitxers settings.py i ja ens dirà si volem instalar les llibreries, allà, li donarem que si.
2. Proveu a iniciar l'aplicació i veure si us funciona.

## Connectar Base de Dades a PyCharm (opcional)
PyCharm permet crear una connexio a la base de dades, la qual nomes serveix per a poder veure la base de dades des del programa. Això pot anar bé si voleu veure com va quedant la base de dades o el que necessiteu. És opcional, ja que la connexió amb Django ve donada per els arxius de configuració d'aquests i no per el IDE.
1. A la barra lateral dreta veureu un apartat anomenat Database. Allà, veureu que hi ha un simbol de suma -> Data source -> PostgreSQL
2. Configurarem els diferents inputs amb la configuració que trobarem al fitxer settings.py de l'aplicació.
3. Li doneu a apply i a ok, i ja ho tindreu configurat.

## Enllaços d'interès
- [Documentació Django](https://docs.djangoproject.com/en/4.0/)
- [Documentació python i MongoDB](https://www.w3schools.com/python/)
- [Curs de Django a Youtube](https://www.youtube.com/playlist?list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB)
- [Web a replicar](https://news.ycombinator.com/)
### Enllaços REST API
- [Llibreria de rest](https://www.django-rest-framework.org/)
- [Exemple de com utilitzar REST API](https://blog.logrocket.com/django-rest-framework-create-api/#restful-structure-get-post-put-delete-methods)
- [Tutorial generar OpenApi amb swaggerUI utilitzant Django](https://hackernoon.com/openapi-30-schema-with-swagger-ui-for-django-restful-app-4w293zje)
- [Editor Swagger](https://editor.swagger.io/)
<br><br>Fins aquí l'explicació de com instal·lar-se les coses. Si teniu qualsevol problema, dubte o necessitat, digueu-m'ho. També sentiu-vos lliures de completar aquesta petita guia.