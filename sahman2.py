import random
import PySimpleGUI as sg

layout = [[sg.Text('1 ile 10 arasında bir sayı tahmin edin:')],
          [sg.Input()],
          [sg.Button('Tahmini İlet'), sg.Button('Sayıyı Yenile')]]

window = sg.Window('SAHMAN SAYI TAHMİN OYUNU!', layout)


secret_number = random.randint(1, 10)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Sayıyı Yenile'):
     
        secret_number = random.randint(1, 10)
    elif event == 'Tahmini İlet':
       
        try:
            guess = int(values[0])
            if guess == secret_number:
                sg.popup('Doğru Tahmin!')
            else:
                sg.popup(f'Yanlış Sayı Sayı Buydu: {secret_number}.')
        except ValueError:
            sg.popup('1 ile 10 arasında sayı yazınız!')

    window.close()
