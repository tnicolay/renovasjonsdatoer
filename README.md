# renovasjonsdatoer

Dette Python-scriptet er utviklet for å hente og formatere hentingsdatoer for ulike typer avfall for en spesifikk adresse, og deretter sende disse datoene til definerte webhooks. Dette er spesielt nyttig for automatisering av avfallshåndtering og planlegging.

## Funksjoner

- Henter første hentingsdato for restavfall, papir/plast og glass/metall.
- Formaterer hentingsdatoene til en lesbar format.
- Sender hentingsdatoene til forhåndsdefinerte webhooks.

## Installasjon

Før du bruker dette scriptet, sørg for at du har installert Python 3.9 og `requests` biblioteket. 

For å installere `requests`, kjør følgende kommando:

```bash
pip install requests
```

## Bruk

1. Klone dette repositoriet eller last ned scriptet.
2. Åpne scriptet i en teksteditor.
3. Endre `adresse` variabelen i `hovedfunksjon()` til din faktiske adresse.
4. Kjør scriptet ved å bruke følgende kommando:

```bash
python hent_datoer_for_avfall.py
```
