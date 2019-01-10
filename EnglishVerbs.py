'''
Game of Verbs in English
'''
import random

verbs = ('awake','be','beat','begin','bite','blow','break','bring','build','buy','catch','choose','come','cost','cut','do','deal','dig','dream','draw','drink','drive','eat','fall','feed','feel','fight','find','fly','forget','forgive','freeze','get','give','go','grow','hang','have','hear','hide','hit','hold','hurt','keep','know','lay','lead','leave','lend','let','lie','lose','make','mean','meet','pay','put','quit','read','ride','ring','rise','run','say','see','seek','sell','send','set','sew','shake','shine','shoot','show','sing','sink','sit','sleep','slide','speak','spend','spread','stand','steal','stick','strike','swear','sweep','swell','swim','swing','take','teach','tear','tell','think','wear','weep','win','write')
past_verbs =  ('awoke','was','beat','began','bit','blew','broke','brought','built','bought','caught','chose','came','cost','cut','did','dealt','dug','dreamt','drew','drank','drove','ate','fell','fed','felt','fought','found','flew','forgot','forgave','froze','got','gave','went','grew','hung','had','heard','hid','hit','held','hurt','kept','knew','laid','led','left','lent','let','lay','lost','made','meant','met','paid','put','quit','read','rode','rang','rose','ran','said','saw','sought','sold','sent','set','sewed','shook','shone','shot','showed','sang','sank','sat','slept','slid','spoke','spent','spread','stood','stole','stuck','struck','swore','swept','swelled','swam','swung','took','taught','tore','told','thought','wore','wept','won','wrote')
playing = True


# Funcion para lista de verbos a jugar

def numbers_to_play(numero):
	return random.sample(range(1,100), numero) #numeros en range son valor fijo ya que por el momento solo se tiene una cantidad de 100 verbos a jugar.


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
			cant_verbos = int(input("Favor ingresa la cantidad de verbos a jugar (Rango entre 1-100) "))
		except ValueError:
			print('Ese no es un numero o caracter valido, favor vuelve a intentarlo ')
			continue
		else:
			print("Valor aceptado. Comienza el juego!")
			break


'''
GAME
'''

def start_game():
	
	while True:

		puntaje = 0 # suma 1 cada respuesta correcta
		string_resultados = ''

		# BIENVENIDA AL JUEGO
		print("Bienvenido a Verbos en English - The Game!")

		# SOLICITAR CANTIDAD DE VERBOS A JUGAR.
		cantidad_verbos() #Funcion que solicita la cantidad de verbos a jugar
		list_verbs = numbers_to_play(cant_verbos) # Se genera una lista random para jugar los verbos

		for x in list_verbs:
			print("\nVerbo: {}".format(verbs[x]))
			answer = raw_input("\nRespuesta: ")
			verbo = Verbo(verbs[x], past_verbs[x])

			print(answer)
			if answer.lower() == past_verbs[x]:
				puntaje+=1
				string_resultados+= '\n'+verbo.__str__()+ ' Correcto! Tu respuesta fue: '+answer
			else:
				if answer.lower() != past_verbs[x]:
				 puntaje-=1
				 string_resultados+= '\n'+verbo.__str__()+ ' Incorrecto! Tu respuesta fue: '+answer

		print("Lista completada, tus resultados son los siguientes:\n"+string_resultados)
		print("\nTu puntaje final es: {}\n".format(puntaje))
		
		volver_jugar = input("Deseas volver a jugar? Si o No")
		if volver_jugar[0].lower() == 's':
			playing=True
			continue
		else:
			break



if __name__ == '__main__':
	start_game()

