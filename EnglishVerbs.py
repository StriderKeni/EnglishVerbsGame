import gspread
import random
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_name('EnglishVerbs_secret.json')
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = credentials.create_scoped(scope)
gc = gspread.authorize(credentials)

sheet1 = gc.open('Verbs').sheet1

result_a = sheet1.col_values(1)
results_b = sheet1.col_values(2)

'''
Game of Verbs in English
'''
verbs = sheet1.col_values(1)
past_verbs = sheet1.col_values(2)

playing = True

# Funcion para lista de verbos a jugar


def numbers_to_play(numero):
    # numeros en range son valor fijo ya que por el momento solo se tiene una cantidad de 100 verbos a jugar.
    return random.sample(range(1, len(result_a)), numero)


class Verbo:
    def __init__(self, presente, pasado):
        self.presente = presente
        self.pasado = pasado

    def __str__(self):
        return 'Presente: '+self.presente + ' | Pasado: '+self.pasado


def cantidad_verbos():
    global cant_verbos

    while True:
        try:
            cant_verbos = int(
                input("Favor ingresa la cantidad de verbos a jugar (Rango entre 1-100): "))
        except ValueError:
            print('Ese no es un numero o caracter valido, favor vuelve a intentarlo ')
            continue
        else:
            print("\nValor aceptado. Comienza el juego!")
            break


'''
GAME
'''


def start_game():
    global playing

    while playing:

        puntaje = 0  # suma 1 cada respuesta correcta
        string_resultados = ''

        # BIENVENIDA AL JUEGO
        print("\n\nWelcome to Verbs in English - The Game!")

        # SOLICITAR CANTIDAD DE VERBOS A JUGAR.
        cantidad_verbos()  # Funcion que solicita la cantidad de verbos a jugar
        # Se genera una lista random para jugar los verbos
        list_verbs = numbers_to_play(cant_verbos)

        for x in list_verbs:
            print("\nVerbo: {}".format(verbs[x+1]))
            answer = input("\nRespuesta: ")
            verbo = Verbo(verbs[x+1], past_verbs[x+1])

            if answer.lower() == past_verbs[x+1]:
                string_resultados += '\n'+verbo.__str__() + ' Correcto! Tu respuesta fue: '+answer
                puntaje += 1

            else:
                if answer.lower() != past_verbs[x+1]:
                    string_resultados += '\n'+verbo.__str__() + ' Incorrecto! Tu respuesta fue: '+answer
                    puntaje -= 1

        print("\nLista completada, tus resultados son los siguientes: \n"+string_resultados)
        print("\nTu puntaje final es: {}\n".format(puntaje))

        volver_jugar = input("Deseas volver a jugar? Si o No ")
        if volver_jugar[0].lower() == 's':
            playing = True
            continue
        else:
            print("\nGracias por jugar!")
            break


if __name__ == '__main__':
    start_game()
