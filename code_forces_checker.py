import requests
import random
import sys

abc = 'ABCDEF'
logins = []
def protect(logins):
    nicknames = logins[0]
    for i in range(1, len(logins)):
        nicknames += ';'+logins[i]
    req = requests.post(f"https://codeforces.com/api/user.info?handles={nicknames}")
    if req.json()['status'] == 'FAILED':
        return "Ошибка: Неверно указан(ы) логин(ы)."
    return req.json()['status']
def checker(logins):
    if protect(logins) != 'OK':
        return protect(logins)
    attempt = 0
    while attempt < 10000:
        contest_random = random.randint(0, 1700)    
        g = True
        for i in range(len(logins)):
            try:
                req = requests.post(f"https://codeforces.com/api/contest.status?contestId={contest_random}&handle={logins[i]}")
            except:
                g = False
                break
            try:
                if len(req.json()['result']) > 0:
                    g = False
                    break
            except:
                g = False
                break
        if g:
            task = random.randint(0, 5)
            return f'https://codeforces.com/contest/{contest_random}/problem/{abc[task]}'

        attempt += 1
    else:
        return "Ошибка: Слишком большой объем данных :("
