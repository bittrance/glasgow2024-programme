#!/usr/bin/env python3

import csv, requests, os, sys

programme = requests.get('https://guide.glasgow2024.org/schedule.json').json()

output = csv.writer(sys.stdout)
output.writerow(['datetime', 'mins', 'title', 'desc', 'loc'])
for entry in programme:
    row = [
        entry['datetime'],
        entry['mins'],        
        (entry['title'] or '').replace('\n', ' '),
        (entry['desc'] or '').replace('\n', ' '),
        ', '.join(entry['loc']),
    ]
    output.writerow(row)