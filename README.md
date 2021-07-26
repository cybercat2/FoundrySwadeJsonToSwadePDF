# FoundrySwadeToSwadePDF
Utility to convert Foundry Swade character .json export files to Swade character sheet pdf files.
Code is written in python version 3.7.3, and runs on Raspberry Pi OS version 10 (buster).
Also runs in Win10, python 3.7.3, with pip pdfrw addon.

Current revision - Foundry2pdf is 0.3 beta. 

Json files are exported from Foundry 8.8. 

Game subsystem is Peginc Swade 0.19.5.

Known bugs - 

  Die modifiers aren't handling 0 mod correctly. Will be fixed in 0.2 (soon). DONE v0.27/25/21

  PDF file is giveaway from Peginc, and I'm only Annotatiing them, not changing them, but i probably should get permission to use, or workaround (version 0.3.1).
  
  PDFRW is throwing warnings about stream length. Unknown cause or fix time. Does not affect output.

Upgrades -

  Will add file picker in version v0.3 DONE v0.3 7/25/21

  Will test on Win10 in near future (version 0.4). DONE v0.3 7.25/21


Instructions - 

Export character from foundry.

Either pass your json file in command line param, or if no name passed, will drop to Tk file picker. 
