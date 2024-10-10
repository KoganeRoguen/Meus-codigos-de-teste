import keyboard

paused = False

def toggle_pause():
    global paused
    paused = not paused # Alterna o estado de pausa
    if paused:
        print('\n< OFF >\n')
    else:
        print('\n< ON >\n')

def write_colchetes():
    if not paused:
        keyboard.press_and_release('backspace')
        keyboard.write("[]")
        keyboard.press_and_release('left')
        
def write_parenteses():
    if not paused:
        keyboard.press_and_release('backspace')
        keyboard.write("()")
        keyboard.press_and_release('left')

def write_asteriscos():
    if not paused:
        keyboard.press_and_release('backspace')
        keyboard.write("**")
        keyboard.press_and_release('left')
        
def write_apostrofo():
    if not paused:
        keyboard.press_and_release('backspace')
        keyboard.write("``")
        keyboard.press_and_release('left')

# Adiciona listeners para as teclas desejadas
keyboard.add_hotkey('[', write_colchetes)
keyboard.add_hotkey('(', write_parenteses)
keyboard.add_hotkey('*', write_asteriscos)
keyboard.add_hotkey("'", write_apostrofo)
keyboard.add_hotkey('pause', toggle_pause) # listener para a tecla Pause

print('\n=== Pression a tecla "Pause" para pausar o programa e "End" para fechar o programa ===\n')
keyboard.wait('end')