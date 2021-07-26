import json
import pdfrw
import sys
from tkinter.filedialog import askopenfilename

if len(sys.argv) >1:
    inputfile = str(sys.argv[1])
else:
    inputfile=askopenfilename()       
with open(inputfile) as f:
  character = json.load(f)
f.close

jName=character['name']
jAgility = 'd'+str(character['data']['attributes']['agility']['die']['sides'])
jAgilityMod = str(character['data']['attributes']['agility']['die']['modifier'])
jStrength = 'd'+str(character['data']['attributes']['strength']['die']['sides'])
jStrengthMod = str(character['data']['attributes']['strength']['die']['modifier'])
jSmarts = 'd'+str(character['data']['attributes']['smarts']['die']['sides'])
jSmartsMod = str(character['data']['attributes']['smarts']['die']['modifier'])
jSpirit = 'd'+str(character['data']['attributes']['spirit']['die']['sides'])
jSpiritMod = str(character['data']['attributes']['spirit']['die']['modifier'])
jVigor = 'd'+str(character['data']['attributes']['vigor']['die']['sides'])
jVigorMod = str(character['data']['attributes']['vigor']['die']['modifier'])
jBennies = character['data']['bennies']['value']
jPace = character['data']['stats']['speed']['value']
jParry = character['data']['stats']['parry']['value']
jToughness = character['data']['stats']['toughness']['value']
jRace = character['data']['details']['species']['name']
jSkillDie = []
jSkill = []
jSkillMod = []
jHindrance = []
jEdge = []
jGear = []
jPower = []
jPowerRange = []
jPowerPP = []
jPowerDur= []
jPowerEffect = []
jWeapon = []
jWeaponDamage = []
jWeaponAP =[]
jWeaponRange =[]
jWeaponROF=[]

if jAgilityMod == '0':
    jAgilityMod = ''
if jAgilityMod == 0:
    jAgilityMod = ''
if jStrengthMod == '0':
    jStrengthMod = ''
if jStrengthMod == 0:
    jStrengthMod = ''
if jSmartsMod == '0':
    jSmartsMod = ''
if jSmartsMod == 0:
    jSmartsMod = ''
if jSpiritMod == '0':
    jSpiritMod = ''
if jSpiritMod == 0:
    jSpiritMod = ''
if jVigorMod == 0:
    jVigorMod = ''
if jVigorMod == '0':
    jVigorMod = ''


for key in character:
    if key == 'items':
        for key2 in character['items']:
            if key2['type'] == 'skill':
                jSkill.append(key2['name'])
                jSkillDie.append(key2['data']['die']['sides'])
                temp=key2['data']['die']['modifier']
                if temp == '0':
                    temp=''
                if temp == 0:
                    temp=''
                jSkillMod.append(temp)
            if key2['type'] == 'hindrance':
                jHindrance.append(key2['name'])
            if key2['type'] == 'power':
                jPower.append(key2['name'])
                jPowerRange.append(key2['data']['range'])
                jPowerPP.append(key2['data']['pp'])
                jPowerDur.append(key2['data']['duration'])
                jPowerEffect.append(key2['data']['damage'])
            if key2['type'] == 'edge':
                jEdge.append(key2['name'])
            if key2['type'] == 'weapon':
                jWeapon.append(key2['name'])
                jWeaponRange.append(key2['data']['range'])
                jWeaponROF.append(key2['data']['rof'])
                jWeaponAP.append(key2['data']['ap'])
                jWeaponDamage.append(key2['data']['damage'])
            if key2['type'] == 'gear':
                jGear.append(key2['name'])
            if key2['type'] == 'armor':
                jGear.append(key2['name'])
       

pdf_template = "swade.pdf"
pdf_output = "output.pdf"
template_pdf = pdfrw.PdfReader(pdf_template)
template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject("true")))
ANNOT_KEY = '/Annots'
ANNOT_FIELD_KEY = '/T'
ANNOT_VAL_KEY = '/V'
ANNOT_RECT_KEY = '/Rect'
SUBTYPE_KEY = '/Subtype'
WIDGET_SUBTYPE_KEY = '/Widget'
for page in template_pdf.pages:
    annotations = page[ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
#                print(key)
                if key == 'Name':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jName)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Agility Die':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jAgility)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Agility Mod':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jAgilityMod)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Strength Die':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jStrength)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Strength Mod':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jStrengthMod)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Smarts Die':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jSmarts)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Smarts Mod':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jSmartsMod)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Spirit Die':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jSpirit)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Spirit Mod':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jSpiritMod)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Vigor Die':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jVigor)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Vigor Mod':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jVigorMod)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Bennies':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jBennies)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Pace':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jPace)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Parry':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jParry)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Toughness':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jToughness)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                if key == 'Race':
                    annotation.update(pdfrw.PdfDict(V='{}'.format(jRace)))
                    annotation.update(pdfrw.PdfDict(AP=''))
                skillcount = 0
                for eachone in jSkill:
                    skillcount +=1
                    comp = 'Skills ' + str(skillcount)
                    compdie = comp+' Die'
                    compmod = comp+' Mod'
                    if key == comp:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jSkill[skillcount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == compdie:
                        temp='d'+str(jSkillDie[skillcount-1])
                        annotation.update(pdfrw.PdfDict(V='{}'.format(temp)))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == compmod:
                        temp=str(jSkillMod[skillcount-1])
                        annotation.update(pdfrw.PdfDict(V='{}'.format(temp)))
                        annotation.update(pdfrw.PdfDict(AP=''))
                hindrancecount = 0
                for eachone in jHindrance:
                    hindrancecount +=1
                    comp = 'Hindrances ' + str(hindrancecount)
                    if key == comp:
#                        print('hit',jHindrance[hindrancecount-1])
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jHindrance[hindrancecount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                edgecount = 0
                for eachone in jEdge:
                    edgecount +=1
                    comp = 'Edges & Advancements ' + str(edgecount)
                    if key == comp:
#                        print('hit',jEdge[edgecount-1])
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jEdge[edgecount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                gearcount = 0
                for eachone in jGear:
                    gearcount +=1
                    comp = 'Gear ' + str(gearcount)
                    if key == comp:
 #                       print('hit',jGear[gearcount-1])
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jGear[gearcount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                powercount = 0
                for eachone in jPower:
                    powercount +=1
                    comp = 'Power ' + str(powercount)
                    comppp = 'PP ' + str(powercount)
                    comprange ='Power Range ' + str(powercount)
                    compdur = 'Duration ' + str(powercount)
                    compeffect = 'Effect ' + str(powercount)
                    if key == comp:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jPower[powercount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == comppp:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jPowerPP[powercount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == comprange:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jPowerRange[powercount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == compdur:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jPowerDur[powercount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == compeffect:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jPowerEffect[powercount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                weaponcount = 0
                for eachone in jWeapon:
                    weaponcount +=1
                    comp = 'Weapons ' + str(weaponcount)
                    comprange = 'Weapon Range ' + str(weaponcount)
                    compdamage = 'Weapon Damage ' +str(weaponcount)
                    compap = 'Weapon AP ' + str(weaponcount)
                    comprof ='Weapon ROF ' + str(weaponcount)
                    if key == comp:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jWeapon[weaponcount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == comprange:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jWeaponRange[weaponcount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == compdamage:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jWeaponDamage[weaponcount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == compap:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jWeaponAP[weaponcount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                    if key == comprof:
                        annotation.update(pdfrw.PdfDict(V='{}'.format(jWeaponROF[weaponcount-1])))
                        annotation.update(pdfrw.PdfDict(AP=''))
                                        
pdf_output= jName+'.pdf'
pdfrw.PdfWriter().write(pdf_output,template_pdf)
