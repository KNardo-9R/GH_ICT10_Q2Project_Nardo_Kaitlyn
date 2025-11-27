from pyscript import display, document 

# the format heavily follows EX11; key: value 

# commarts dictionary
commarts_club = {
        'Description':'A place for people that love speaking & writing!',
        'Meetings':'Mondays (2:30-3:30) & Tuesdays (2:30-4:30)',
        'Location':'Room 711', 
        'Moderator': 'Sir Loreto',
        'Members': '40'
    }


def commarts_result(e): 
    # gets id of output 
    document.getElementById('output').innerHTML = " "

    commarts = f'''
    Communication Arts Club
        Description: {commarts_club['Description']}
        Meeting Time: {commarts_club['Meetings']}
        Location: {commarts_club['Location']}
        Club Moderator: {commarts_club['Moderator']}
        Number of Members: {commarts_club['Members']}
        '''
    display(commarts, target='output')

# math dictionary 
math_club = {
    'Description':'The haven of all numerical fanatics, from 1 to infinity!',
    'Meetings':'Tuesdays (2:30-3:30)',
    'Location':'Room 510', 
    'Moderator': 'Sir Ferma',
    'Members': '20'
}


def math_result(e): 
    document.getElementById('output').innerHTML = " "

    math = f'''
    Math Club 
        Description: {math_club['Description']}
        Meeting Time: {math_club['Meetings']}
        Location: {math_club['Location']}
        Club Moderator: {math_club['Moderator']}
        Number of Members: {math_club['Members']}
    '''
    display(math, target='output')

# science dictionary 
science_club = {
    'Description':'An oasis to quench the thirst of all curious scientists ready to step up for the greater good.',
    'Meetings':'Tuesdays (2:30-3:30)',
    'Location':'Room 502', 
    'Moderator': 'Sir Calpo',
    'Members': '24'
}


def sci_result(e): 
    document.getElementById('output').innerHTML = " "

    science = f'''
    Science Club
        Description: {science_club['Description']}
        Meeting Time: {science_club['Meetings']}
        Location: {science_club['Location']}
        Club Moderator: {science_club['Moderator']}
        Number of Members: {science_club['Members']}
    '''
    display(science, target='output')

# social sciences dictionary 
ss_club = {
    'Description':'Ever curious about society, politics, and current events? This club tackles all you want to know about the social sciences and more.',
    'Meetings':'Tuesdays (2:30-4:00)',
    'Location':'Room 708', 
    'Moderator': 'Ma\'am Libremonte',
    'Members': '19'
}


def ss_result(e): 
    document.getElementById('output').innerHTML = " "

    ss = f'''
    Social Sciences Club 
        Description: {ss_club['Description']}
        Meeting Time: {ss_club['Meetings']}
        Location: {ss_club['Location']}
        Club Moderator: {ss_club['Moderator']}
        Number of Members: {ss_club['Members']}
    '''
    display(ss, target='output')

# vball dictionary 
vball_club = {
    'Description':'From hitting, blocking, receiving, and serving to camaraderie and teamwork, Volleyball Club has it all!',
    'Meetings':'Tuesdays (3:00-5:00)',
    'Location':'OBMC Quadrangle', 
    'Moderator': 'Sir Gervacio',
    'Members': '30'
}


def vball_result(e): 
    document.getElementById('output').innerHTML = " "

    vball = f'''
    Volleyball Varsity Club 
        Description: {vball_club['Description']}
        Meeting Time: {vball_club['Meetings']}
        Location: {vball_club['Location']}
        Club Moderator: {vball_club['Moderator']}
        Number of Members: {vball_club['Members']}
    '''
    display(vball, target='output')









