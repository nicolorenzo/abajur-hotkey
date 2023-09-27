from pynput import keyboard
from pynput.keyboard import Controller, Key
import lorem

c = Controller()

print('Programa em execução. Utilize o comando CTRL + ALT + L + I para gerar um parágrafo de "Lorem Ipsum"')


def newLorem():

    c.release(Key.ctrl)
    c.release(Key.alt)
    c.release('l')
    c.release('i')

    c.type(lorem.paragraph())


with keyboard.GlobalHotKeys(
        {
            '<ctrl>+<alt>+l+i': newLorem,
        }
) as h:
    h.join()
