import re

def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    new_id = re.sub('[~!@#$%^&*()=+{}:?,<>/]', '', new_id)
    new_id = new_id.replace('[', '')
    new_id = new_id.replace(']', '')
    new_id = re.sub('[.]+', '.', new_id)
    new_id = re.sub('^[.]', '', new_id)
    new_id = re.sub('[.]$', '', new_id)
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) >= 16:
        new_id = new_id[0:15]
        new_id = re.sub('[.]$', '', new_id)
    while(len(new_id) <= 2):
        new_id += new_id[-1]
    answer= new_id
    return answer