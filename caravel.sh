#!/bin/bash
sudo fabmanager create-admin --app caravel
sudo caravel db upgrade
sudo caravel init
sudo caravel runserver
