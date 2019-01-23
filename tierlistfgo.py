import webbrowser

# Open Servants Tier List from Gamepress

url = 'https://grandorder.gamepress.gg/'

print('''Digite a opção desejada:
1 - Consultar dados sobre um servo.
2 - Abrir tier list.
3 - Abrir team comp.
Digite qualquer outra tecla pra sair.''')

try:
    op = int(input())
    if op == 1: #Servo
        servo = input('Digite o nome do servo para consulta: ').lower().strip()
        servo = servo.replace(' ', '-')
        if '(' in servo:
            servo = servo.replace('(', '')
            servo = servo.replace(')', '')

        print(servo)

        webbrowser.open_new_tab('https://grandorder.gamepress.gg/servant/' + servo)

    elif op == 2: #Tier list
        print('''1 - Abrir tier list de 5 estrelas.
2 - Abrir tier list de 4 estrelas.
3 - Abrir tier list de 1-3 estrelas
Digite qualquer outra tecla pra sair.''')

        op = input()
        if op == '1':
            webbrowser.open_new(url + '5-star-tier-list/')
        elif op == '2':
            webbrowser.open_new_tab(url + '4-star-tier-list/')
        elif op == '3':
            webbrowser.open_new_tab(url + '13-star-tier-list/')

    elif op == 3: #Team comp
        print('''1 - Abrir Comp Buster Blitz
2 - Abrir Comp Buster Critfest
3 - Abrir Arts Spamfest
4 - Abrir Zombie Team
5 - Abrir Staple Quick Team
Digite qualquer outra tecla pra sair.''')

        op = int(input())
        if op == 1:
            webbrowser.open_new_tab(url + 'buster-blitz/')
        elif op == 2:
            webbrowser.open_new_tab(url + 'buster-critfest/')
        elif op == 3:
            webbrowser.open_new_tab(url + 'arts-spamfest/')
        elif op == 4:
            webbrowser.open_new_tab(url + 'zombie-team/')
        elif op == 5:
            webbrowser.open_new_tab(url + 'staple-quick-team/')
except ValueError:
    pass

