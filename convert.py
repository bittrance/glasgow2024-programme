#!/usr/bin/env python3

import csv, requests, os, sys

def category_join(tags, category):
    return '; '.join([tag['label'] for tag in tags if tag['category'] == category]) or '-'

programme = requests.get('https://guide.glasgow2024.org/schedule.json').json()

output = csv.writer(sys.stdout)
output.writerow([
    'datetime',
    'mins',
    'title',
    'desc',
    'loc',
    'environment',
    'area',
    'tag',
    'note',
])
for entry in programme:
    row = [
        entry['datetime'],
        entry['mins'],        
        (entry['title'] or '').replace('\n', ' '),
        (entry['desc'] or '').replace('\n', ' '),
        '; '.join(entry['loc']),
        category_join(entry['tags'], 'Environment'),
        category_join(entry['tags'], 'Area'),
        category_join(entry['tags'], 'Tag'),
        category_join(entry['tags'], 'Note'),
    ]
    output.writerow(row)