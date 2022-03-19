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

## Connectar amb MongoDB (Deprecated)
**⚠️ ATENCIÓ: Ja no cal fer-ho, us podeu saltar aquest apartat, ja que us ho he habilitat per a tots crec. Ho deixo per si de cas calgués.**
<br>
<br>
~~Per a mongo, si us sembla bé, utilitzarem el host que proporciona el propi mongoDB, aixi no cal que ens l'instalem en local cadascu, i serà una base de dades compartida. Estarà hostejada a mongoDB Atlas, que té una versió gratuita que ens permetrà fer el que necessitem.
<br>Per a conectar-vos, cal registrar la vostra IP publica per a que us pogueu conectar, o us denegarà la conexió.
<br> Per a no haver-ho de fer jo cada vegada (les IPs publiques dels routers van canviant cada cop que reinicieu el router, i si el reinicieu l'haureu de canviar) us haureu de crear un compte i us afegiré al projecte.~~
1. Anar a la següent [pàgina](https://account.mongodb.com/account/login)
2. Crear-vos un nou compte (jo ho he fet amb el correu de google de la uni, pero el que preferiu).
3. Un cop tingueu compte (crec que no cal confirmar correu) digueu-me el vostre correu i us afegeixo al projecte.
4. Un cop al projecte, aneu a la pestanya Atlas i allà a Network Access (a la barra lateral).
5. Veureu que a la dreta en verd hi ha un botó de _ADD IP ADDRESS_ i li doneu clic.
6. Allà, afegiu la vostra Ip i li doneu a confirm. Podeu saber la vostra Ip pública [aquí](https://www.whatismyip.com/)
7. Ja us hauria de funcionar.
`mongodb+srv://Hacker-News-HN22D:lbRfG9oDb5yFvGAl@hacker-news-hn22d.uq0bw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`

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

## Connectar Base de Dades a PyCharm (opcional)
PyCharm permet crear una connexio a la base de dades, la qual nomes serveix per a poder veure la base de dades des del programa. Això pot anar bé si voleu veure com va quedant la base de dades o el que necessiteu. És opcional, ja que la connexió amb Django ve donada per els arxius de configuració d'aquests i no per el IDE.
1. A la barra lateral dreta veureu un apartat anomenat Database. Allà, veureu que hi ha un simbol de suma -> Data source -> MongoDB
2. A on posa url, enganxeu la següent url: `mongodb+srv://hacker-news-hn22d.uq0bw.mongodb.net/myFirstDatabase?retryWrites=true&w=majority`
3. Li doneu a apply i a ok, i ja ho tindreu configurat.

## Enllaços d'interès
- [Documentació Django](https://docs.djangoproject.com/en/4.0/)
- [Documentació python i MongoDB](https://www.w3schools.com/python/)
- [Curs de Django a Youtube](https://www.youtube.com/playlist?list=PLU8oAlHdN5BmfvwxFO7HdPciOCmmYneAB)
- [Web a replicar](https://news.ycombinator.com/)
<br><br>Fins aquí l'explicació de com instal·lar-se les coses. Si teniu qualsevol problema, dubte o necessitat, digueu-m'ho. També sentiu-vos lliures de completar aquesta petita guia.