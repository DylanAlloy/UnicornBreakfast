#!/bin/bash

fabmanager create-admin --app caravel
caravel db upgrade
caravel init
caravel runserver
