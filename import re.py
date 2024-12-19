import re
from datetime import datetime

# Exemple de contenu iCalendar
ical_data = """
BEGIN:VEVENT
DTSTAMP:20240110T053220Z
DTSTART:20240110T080000Z
DTEND:20240110T100000Z
SUMMARY:SAE1.05
LOCATION:G_011_AMPHI
DESCRIPTION:\\n\\nRT1-S1\\nLACAN DAVID\\n(Exporté le:10/01/2024 06:32)\\n
UID:ADE60323032332d3230323453542d455449454e4e452d32323839322d302d30
CREATED:19700101T000000Z
LAST-MODIFIED:20240110T053220Z
SEQUENCE:2141064552
END:VEVENT
"""

# Fonction pour lire et afficher le contenu de l'événement
def parse_ical_event(ical_data):
    event = {}
    for line in ical_data.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            event[key] = value.strip()

    # Conversion des dates au format lisible
    def format_datetime(dt_str):
        return datetime.strptime(dt_str, "%Y%m%dT%H%M%SZ").strftime("%d/%m/%Y %H:%M:%S")
    
    # Affichage des informations de l'événement
    print("Event Details:")
    print(f"- Summary: {event.get('SUMMARY', 'N/A')}")
    print(f"- Location: {event.get('LOCATION', 'N/A')}")
    # Corrige le remplacement des backslashes
    description = event.get('DESCRIPTION', 'N/A').replace("\\n", "\n")
    print(f"- Description: {description}")
    print(f"- Start Time: {format_datetime(event['DTSTART']) if 'DTSTART' in event else 'N/A'}")
    print(f"- End Time: {format_datetime(event['DTEND']) if 'DTEND' in event else 'N/A'}")
    print(f"- Last Modified: {format_datetime(event['LAST-MODIFIED']) if 'LAST-MODIFIED' in event else 'N/A'}")
    print(f"- Created: {format_datetime(event['CREATED']) if 'CREATED' in event else 'N/A'}")
    print(f"- UID: {event.get('UID', 'N/A')}")
    print(f"- Sequence: {event.get('SEQUENCE', 'N/A')}")

# Appel de la fonction
parse_ical_event(ical_data)
