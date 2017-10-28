LoraWan module with HX711
================================

Ce module est basé sur la librairie HX711 de GEDA
https://github.com/geda/hx711-lopy

Configuration
----------------------

Editer le fichier config.py et remplissez les champs suivants:

```
DEV_EUI = '<DEV_EUI>'
APP_EUI = '<APP_EUI>'
APP_KEY = '<APP_KEY>'
```

Debug
----------------------

Un debug 'visuel' a été ajouté, pour l'activer, positionnez la variable
"DEBUG_LED" à 'True'.

- LED rouge: Connection au réseau LoRa
- LED verte: Envoi d'un paquet
- LED bleue: Réception d'un paquet
