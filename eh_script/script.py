import yaml

# Read in data

def read_in_data(file):
    with open (file, 'r') as fin:
       new_file = yaml.safe_load(fin)
       return new_file
    
programs = read_in_data('programs.txt')
devices = read_in_data('devices.txt')
enrollments = read_in_data('enrollments.txt')

# If enrollment contains NEST or ECOBEE migrate to program 2

for i in enrollments:
    if i['devices'][0]['manufacturer'] == 'HONEYWELL':
        pass
    else:
        i['programId'] = 2     

# Change device group to associated program default group

for i in devices:
    if i['manufacturer'] == 'HONEYWELL':
        i['group'] = 1
    else:
        i['group'] = 2

# Write outputs to updated 'migrated-enrollments.txt' and 'migrated-devices.txt'

with open('migrated-enrollments.txt', 'w') as file:
    yaml.dump(programs, file, default_flow_style=True)   

with open('migrated-devices.txt', 'w') as file:
    yaml.dump(devices, file, default_flow_style=True) 
