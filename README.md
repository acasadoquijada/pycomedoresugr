# pycomedores
[![Build Status](https://travis-ci.org/acasadoquijada/pycomedoresugr.svg?branch=master)](https://travis-ci.org/acasadoquijada/pycomedoresugr)
[![Coverage Status](https://coveralls.io/repos/github/acasadoquijada/pycomedoresugr/badge.svg?branch=master)](https://coveralls.io/github/acasadoquijada/pycomedoresugr?branch=master)

##Introducción

Esta pequeña biblioteca realizada usando python3 permite acceder a los datos del menu de los comedores de la Universidad de Granada de una manera sencilla.

Los datos son consultados en la [web de comedores](http://scu.ugr.es/)


## Funciones actuales

* get_menu_semana -> Obtiene en "crudo" el menú semanal

* menu_semana_diccionario -> Se pasa del menú en "crudo" a un diccionario

* menu_semana_json -> Del menú en diccionario se pasa a json

* menu_dia -> Usando  `menu_semana_diccionario` se obtiene el menú del día deseado, si no se especifica ningún día, se devuelve el menú del día actual


##Tests

Como el menú cambia cada semana, hemos creado 3 ficheros html solo con la información necesaria para nuestros test, dichos fichero se encuentran en el directorio `Test`.

[Licencia](LICENSE)

Nota: La licencia afecta SOLO a la biblioteca
