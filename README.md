# Acme-REST-API

## Prueba del REST API

En el escenario, la compañía ACME está ofreciendo un servicio que cuenta con códigos de descuento y se necesita una REST API que tenga un CRUD sobre los códigos y una que además chequee si un código está disponible.
Para el desarrollo/prueba se uso un Entorno Virtual.

- En la dirección '' (es decir, el home directory) se encuentra el **checker** que verifica el código, su disponibilidad & existencia.
- En la dirección '/root' se encuentra el browsable API del DRF que lleva a dos links:
  - 'Codes' que otorga una lista de códigos existentes.
  - 'Empresas' que otorga una lista de empresas existentes.
  
## Para registrar un código / empresa

Para registrar un código a través de la API (ACMEREST) primero debe existir una empresa. Los modelos están relacionados de una manera one-to-many, de modo que una empresa puede tener varios códigos pero cada código solamente tiene una empresa.
La empresa cuenta con los siguientes campos:
* {
  *    "nombre": "", <---- CharField
  *   "tipo": "" <---- CharField especificando qué tipo de empresa es.
* }
  
Luego, el código debe ser registrado a una empresa ya existente con los siguientes campos:
* {
  *  "code": 13123, <--- IntegerField
  *  "empresa": null, <--- El nombre de la empresa **ya registrada** a la que pertenece el código, CharField.
  *  "valor": "24%", <--- CharField especificando, con el símbolo porcentual, el valor de descuento que tiene el código.
  *  "usado": "Si" <--- Charfield (máx 2 chars) especificando, con "sí" o "no" si el código está usado.
* }

## Estructura del Servicio
Cuenta con dos apps:
  * Checker
  * ACMEREST
  
### Checker
El Checker se encarga, como su nombre lo asoma, de verificar la existencia de un código en la base de datos (en este caso, la proporcionada por Django). También se encarga de la presentación en HTML, es decir, las páginas web, e interactividad con el usuario como tal.

### ACMEREST
Es el REST API que se encarga del CRUD de los códigos y las empresas. 

## Recuerde cambiar la 'secret key' con la función  _get_random_secret_key()_ incluida en Django
