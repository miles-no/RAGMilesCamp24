# RAGMilesCamp24 - RAG Pipeline - README
###Disclaimer: Stort sett generert av ChatGPT, feil kan forekomme!

Introduksjon

Denne workshopen veileder deg gjennom oppsettet og bruken av en Retrieval-Augmented Generation (RAG) pipeline, som kombinerer dokumentgjenfinning og AI-genererte svar. Prosjektet bruker OpenAI sitt API for embeddings og chat-modeller til å svare på brukerforespørsler basert på innholdet i tekstfiler.

Forutsetninger

Før du starter, sørg for at du har følgende:

Python 3.7 eller nyere installert.
Satt opp VS Code, se Guide_Sette_Opp_VSCode
En OpenAI API-nøkkel. Denne får du av Olve.

Trinn 1: Klone prosjektet
Start med å klone prosjektet fra GitHub:

bash
git clone https://github.com/miles-no/RAGMilesCamp24.git
cd RAGMilesCamp24

Trinn 2: Opprett og aktiver et virtuelt miljø
Det anbefales å bruke et virtuelt miljø for å isolere avhengighetene i prosjektet.

Opprett et virtuelt miljø ved å kjøre følgende kommandoer:

bash

python3 -m venv venv
source venv/bin/activate  # På Windows: venv\Scripts\activate

Trinn 3: Installer avhengigheter

Installer nødvendige Python-pakker ved å bruke requirements.txt-filen:

bash

pip install -r requirements.txt

Trinn 4: Opprett en .env-fil

For å bruke OpenAI API, må du sette opp en miljøvariabel for API-nøkkelen din. Dette gjøres ved å opprette en .env-fil i rotmappen av prosjektet.

Slik oppretter du .env-filen:

Lag en ny fil i prosjektets rotmappe med navnet .env.
Åpne filen og legg til følgende linje, hvor API_NØKKEL er din egen API-nøkkel:
makefile
OPENAI_API_KEY=API_NØKKEL
Bytt ut API_NØKKEL med din faktiske API-nøkkel fra OpenAI.

Trinn 5: Struktur for dokumenter

Sørg for at du har en mappe som heter data i prosjektets rotmappe. Denne mappen skal inneholde tekstfiler (.txt) som pipelinen skal bruke. Hvis mappen ikke finnes, kan du opprette den slik:

bash
mkdir data
Legg deretter til de relevante tekstfilene i denne mappen.

Trinn 6: Kjør programmet

Du er nå klar til å kjøre pipelinen. Kjør følgende kommando for å starte programmet:

bash
python app.py
Programmet vil be deg om å skrive inn en brukerforespørsel, som deretter behandles ved å hente relevante dokumenter og generere et svar.

Trinn 7: Deaktiver virtuelt miljø

Når du er ferdig med prosjektet, kan du deaktivere det virtuelle miljøet ved å kjøre:

bash
deactivate

Feilsøking
Ingen nøkkel angitt: Hvis du får en feilmelding som sier at OpenAI-nøkkelen ikke er funnet, dobbeltsjekk at du har opprettet .env-filen riktig og at den er plassert i rotmappen til prosjektet.

Oppsummering
I denne workshopen har du satt opp en Retrieval-Augmented Generation (RAG) pipeline for å svare på spørsmål basert på innholdet i tekstfiler. Ved å følge trinnene ovenfor har du installert alle nødvendige avhengigheter, konfigurert miljøvariabler, og kjørt programmet med dine egne dokumenter.
