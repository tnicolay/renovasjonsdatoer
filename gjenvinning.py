import sys

sys.path.insert(0,'/home/pi/.local/lib/python3.9/site-packages')

# Vi importerer de nødvendige bibliotekene først.
from min_renovasjon import MinRenovasjon
import requests


# Denne funksjonen henter de første datoene for de forskjellige avfallstypene.
def hent_datoer_for_avfall(adresse):
    # Vi oppretter en MinRenovasjon-instans med den gitte adressen.
    ren = MinRenovasjon(adresse)
    
    # Vi henter de første datoene for restavfall, papir/plast og glass/metall.
    rest_mat_date = ren.waste_collections[2].first_date
    papp_plast_date = ren.waste_collections[0].first_date
    glass_metall_date = ren.waste_collections[4].first_date
    
    # Vi returnerer datoene.
    return rest_mat_date, papp_plast_date, glass_metall_date

# Denne funksjonen formaterer datoene til strenger.
def formater_datoer(rest_mat_date, papp_plast_date, glass_metall_date):
    # Vi formaterer datoene til strenger.
    rest_mat_formatted_date = f"{str(rest_mat_date.day).zfill(2)}-{str(rest_mat_date.month).zfill(2)}-{rest_mat_date.year}"
    papp_plast_formatted_date = f"{str(papp_plast_date.day).zfill(2)}-{str(papp_plast_date.month).zfill(2)}-{papp_plast_date.year}"
    glass_metall_formatted_date = f"{str(glass_metall_date.day).zfill(2)}-{str(glass_metall_date.month).zfill(2)}-{glass_metall_date.year}"
    
    # Vi returnerer de formaterte datoene.
    return rest_mat_formatted_date, papp_plast_formatted_date, glass_metall_formatted_date

# Denne funksjonen sender GET-forespørsler til de forskjellige URLene.
def send_get_forespørsler(rest_mat_formatted_date, papp_plast_formatted_date, glass_metall_formatted_date):
    # Vi bygger URLene med de formaterte datoene.
    rest_url = f"https://5b2ca124209efc623c9c5732.connect.athom.com/api/manager/logic/webhook/restavfall?tag={rest_mat_formatted_date}"
    papp_url = f"https://5b2ca124209efc623c9c5732.connect.athom.com/api/manager/logic/webhook/pappogplast?tag={papp_plast_formatted_date}"
    glass_url = f"https://5b2ca124209efc623c9c5732.connect.athom.com/api/manager/logic/webhook/glassogmetall?tag={glass_metall_formatted_date}"
    
    # Vi sender GET-forespørsler til URLene.
    r = requests.get(rest_url)
    r = requests.get(papp_url)
    r = requests.get(glass_url)
    
    #print for  sjekke datoene
    #print (rest_mat_formatted_date)
    #print (papp_plast_formatted_date)
    #print (glass_metall_formatted_date)

# Vi kjører hovedkoden vår.
def hovedfunksjon():
    # Vi definerer adressen.
    adresse = "Luksefjellvegen 13d, 3716 Skien"
    
    # Vi henter de første datoene for de forskjellige avfallstypene.
    rest_mat_date, papp_plast_date, glass_metall_date = hent_datoer_for_avfall(adresse)
    
    # Vi formaterer datoene.
    rest_mat_formatted_date, papp_plast_formatted_date, glass_metall_formatted_date = formater_datoer(rest_mat_date, papp_plast_date, glass_metall_date)
    
    # Vi sender GET-forespørsler til de forskjellige URLene.
    send_get_forespørsler(rest_mat_formatted_date, papp_plast_formatted_date, glass_metall_formatted_date)

# Vi kaller hovedfunksjonen for å kjøre programmet.
hovedfunksjon()