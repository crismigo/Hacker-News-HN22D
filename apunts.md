# Apunts

Per tal de realitzar la segona entrega, cal fer una REST API, la qual implementarem mitjançant [Django Rest Framework](https://www.django-rest-framework.org/), una llibreria de django (third party) que ens permet crear una rest api fàcilment, i el qual ja té un mòdul per a generar l'esquema OpenAPI.<br>
> Per si no sabeu que és OpenAPI, simplement es un fitxer on s'explica tots els endpoints de la nostra api, de manera que, si algú vol saber a que pot accedir, només cal que miri aquest fitxer. [Exemple](https://atenea.upc.edu/pluginfile.php/4532654/mod_resource/content/3/wot-api.yaml)

Jo ja us ho he deixat tot configurat, per tal que només us calgui implementar la REST API a la vostra part. Els models ja estan fets, així com la instalació i configuració de les llibreries. També els CORS (uns headers que gestionen l'accés a l'API. Ara mateix per a desenvolupar estan desactivats per tal que poguem treballar més fàcilment).
<br><br>
Per tal de fer la REST API, us recomano seguir el següent [enllaç](https://blog.logrocket.com/django-rest-framework-create-api/#restful-structure-get-post-put-delete-methods), el qual està molt bé i us pot servir per aprendre a utilitzar-ho. També us podeu guiar pel que he fet jo, el qual està basat en l'enllaç.

## Estructura RESTful que seguirem
L'estructura restful simplement ens serveix per quedar entre nosaltres com nombrem les coses, per tal que estigui estandaritzat. Si no m'equivoco la openAPI també diu quelcom, però mirant-ho rapid no ho he trobat, si algú ho veu, que ho apunti per aquí.
### Exemple de requests per endpoint:
#### news/
- **GET :** Retorna totes les instàncies que hi hagi de news
- **POST :** Crea una nova instància de news i la retorna. En cas que no es pugui crear, es retorna `error 400`
#### news/``<int:news_id>``
- **GET :** Retorna la instància de news que conté la news_id. En cas que no existeixi es retorna `error 400`.
- **PUT :** Actualitza la instància amb la id passada i la retorna. En cas que no existeixi es retorna `error 400`. 
- **DELETE :** Elimina la instància amb la id passada i la retorna. En cas que no existeixi es retorna `error 400`.

> Un endpoint és una url concreta, per exemple *news/*, la qual pot tenir més d'un tipus de request assignat. També hi haurà endpoints que no en tenen cap, i al intentar d'accedir, el matiex framework posa la pàgina d'error 404.

En cas de voler agrupar, podem utilitzar:
#### news/user/``<int:user_id>``
- **GET :** Retorna totes les instàncies que hi hagi de news fetes per l'usuari passat per paràmetre
- **DELETE :** Elimina totes les instàncies que tenen al usuari assignat. En cas que no existeixi es retorna `error 400`.
## Punts a fer per tal de crear la REST API
Per tal de crear la REST API, haurieu de seguir els següents passos:
1. Crear un fitxer dins el directori anomenat serializers.py. Fer el model Serializer del model del qual heu d'extreure la informació.
2. A views.py, crear una classe per cada endpoint (cada direcció), la qual heredi de APIView.
3. Crear un metode d'aquesta classe per cada request que volem que respongui l'endpoint. Dins d'aquest, fer les operacions que calguin i, un cop acabat, fer la Response amb la data necessària i l'status.
4. Afegir els endpoints al fitxer urls.py tot indicant la APIView que volem relacionar-hi.
5. Comprovar que l'endpoint que hem posat funciona accedint des del navegador.