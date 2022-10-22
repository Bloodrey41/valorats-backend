import os
from bs4 import BeautifulSoup
import requests

def get_agent_role(agent_name):
    duelists = ('Jett', 'Raze', 'Neon', 'Yoru', 'Reyna', 'Phoenix')

    initiators = ('Sova', 'Fade', 'KAY/O', 'Skye', 'Breach')

    controllers = ('Omen', 'Brimstone', 'Viper', 'Astra', 'Harbor')

    sentinels = ('Killjoy', 'Cypher', 'Chamber', 'Sage')

    if agent_name in duelists:
        return 'duelist'

    if agent_name in initiators:
        return 'initiator'

    if agent_name in controllers:
        return 'controller'

    if agent_name in sentinels:
        return 'sentinel'

def get_data(url):
    html = requests.get(url).text.encode('utf-8')

    soup = BeautifulSoup(html, 'lxml')

    table = soup.find('div', class_ = 'event_column__K2XPK event_agentPicks__wlhpD')

    header = table.find('div', class_ = 'event_tableHeader__9HLCu')

    headers = tuple(map(lambda x: x.text.lower(), header.find_all('div')))

    data = []

    for row in table.find_all('div', class_ = 'event_tableRow__5JpdP'):
        agent_data = {}

        agent_data['maps'] = {}

        for index, column in enumerate(row.find_all('div')):
            header = headers[index]

            if header == 'pickrate': 
                header = 'all'

            if index == 0:
                agent_name = column.text.strip()

                agent_role = get_agent_role(agent_name)

                agent_data[header] = { 
                                'name': agent_name,
                                'role': agent_role,
                                'picture': 'https://www.thespike.gg' 
                                + column.find('img', { 'srcset': True })['src']
                                }
            else: 
                agent_data['maps'][header] = column.text.strip().split('(')[0].replace('%', '')

            data.append(agent_data)

    return data
