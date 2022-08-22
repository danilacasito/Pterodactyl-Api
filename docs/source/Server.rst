Clase Server (perteneciente a client)
===========================================
La clase server es un tipo de datos que contiene información util sobre el servidor sobre que se maneja,  como nombre, identificador, etc

No es muy necesario crear una clase Server manualmente, ya que se crea nada mas por ejemplo al usar el ``api.servers()`` este te devuelve tus servidores a base de esta clase

Variables
==========================

Tendremos en cuenta que la clase esta usandose en la variable myServ.

``myServ.name``: El Nombre del servidor

``myServ.allocation``: una Lista de puertos alojados en el servidor

``myServ.owner``: Si eres el propietario del servidor, aparece como true, si no, en false

``myServ.identifier``: El identificador, se usa en ciertas Funciones


Cargar la clase manualmente para usarlo en ciertas Funciones
=================================================================
Por ahora ciertas funciones que toman el identificador requieren de la clase cargada, para cargarla:

``from pterodactyl_api import client
myServ = client.Server()
myServ.setIdentifier("<identifier>")
``

Ya tienes tu clase manual cargada en la variable myServ, y lista para que la puedas usar