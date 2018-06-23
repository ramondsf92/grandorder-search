import webbrowser
# Open Servants Tier List from Gamepress

url = 'https://grandorder.gamepress.gg/'
print('''Digite a opção desejada:
1 - Abrir tier list de 5 estrelas.
2 - Abrir tier list de 4 estrelas.
3 - Abrir tier list de 1-3 estrelas
4 - Abrir Comp Buster Blitz
5 - Abrir Comp Buster Critfest
6 - Abrir Arts Spamfest
7 - Abrir Zombie Team
8 - Abrir Staple Quick Team
Digite qualquer outra tecla pra sair.''')

op = (input())

if op == '1':
    webbrowser.open_new_tab(url + '5-star-tier-list/')
elif op == '2':
    webbrowser.open_new_tab(url + '4-star-tier-list/')
elif op == '3':
    webbrowser.open_new_tab(url + '13-star-tier-list/')
elif op == '4':
    webbrowser.open_new_tab(url + 'buster-blitz/')
elif op == '5':
    webbrowser.open_new_tab(url + 'buster-critfest/')
elif op == '6':
    webbrowser.open_new_tab(url + 'arts-spamfest/')
elif op == '7':
    webbrowser.open_new_tab(url + 'zombie-team/')
elif op == '8':
    webbrowser.open_new_tab(url + 'staple-quick-team/')
