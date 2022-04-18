Views:
- Pagina principal (/news): Es mostren: select * from submissions order by vots desc
- Pàgina submit (/submit) --> Cal estar loguejat, en cas contrari: redirect(/login/)
  - url: title, url --> if url not exist: redirect("/newest/"); else: redirect(submission amb id que conte el url)
  - ask: title, text --> redirect("/newest/")
  - url + ask: title, url, text --> Es crea una submision de tipus url i es crea un comentari amb el contingut del text.
- Pàgina new (/newest): Es mostren: select * from submissions order by created_at desc
- Pàgina autentication (login, register)
- Pagina edit (/edit): nomes deixa modificar (url:title, ask:title/text) --> redirect a la mateixa pagina (canviar siusplau) (nomes es pot els primers 60 minuts despres de crear la publicacio)
![Imagen edit](https://cdn.discordapp.com/attachments/688116000516079621/963842885889962034/unknown.png)
- More: Mostra els seguents 30
- delete: Elimina la publicacio (nomes es pot els primers 30 minuts despres de crear la publicacio)
- like (triangle): Puja un punt
- Pàgina item (/item/?id=X): Mostra un element en concret i se li passa per get ?id=X
  - comment: Fer un comentari a una submission
  - reply: fer un comentari a un comentari ja existent
  - like/unlike: Poder donarli like i unlike a submissions i comments
- Login: Mitjançant google, github o similar.
  - Si ja existeix en el sistema: Entra i es recupera la session del usuari
  - Si no esta loguejat: Es dona d'alta a la bbdd i es crea la sessio.
- Pàgina profile (user?X): Permet veure la pagina del usuari amb la id passada
  - llistat submissions del usuari consultat
  - llistat comments del usuari consultat
  - llistat upvoted submissions(nomes usuari loguejat)
  - llistat upvoted comments (nomes usuari loguejat)
- Pàgina ask: Mostra: select * from submissions where type=ask order by vots desc
- Pàgina threads: Mostra els comentaris de l'usuari loguejat


APPS:
- news (main)
- authentication
- profile
- submit
- item
- comments
- vote

Models:
- User:
  - user
  - about
  - email
  - created_at

- Submission:
  - title: string --> edit es pot modificar
  - type: submission_type
  - author: User
  - points (default 1) = likes
  - created_at
  
- vote:
  - idsubmission
  - idcomment
  - type: actionType
  - iduser
  - created_at
  
-comment:
    - idsubmission
    - idcomment
    - type: actionType
    - iduser
    - text
- Submission_type:
  - name:[url,ask]
  - created_at

- ActionType:
  - Submission
  - comment

![Imagen](https://cdn.discordapp.com/attachments/688116000516079621/963842122115604570/unknown.png)

  

No cal fer:
- comments
- past
- show
- jobs