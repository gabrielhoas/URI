hora_inicio, minuto_inicio, hora_final, minuto_final = [int(x) for x in input().split(maxsplit=4)]
if (hora_inicio == hora_final and minuto_inicio >= minuto_final) or (hora_inicio > hora_final):
    hora_final += 24
if minuto_inicio > minuto_final:
    minuto_final += 60
    hora_final -= 1
hora = int(hora_final - hora_inicio)
minuto = int(minuto_final - minuto_inicio)
if (hora == 0 and minuto >= 1 and minuto <= 59) or (hora >= 1 and hora <= 24 and minuto >= 0 and minuto <= 59):
    print("O JOGO DUROU",hora,"HORA(S) E",minuto,"MINUTO(S)")