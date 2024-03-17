import nyan

cat = nyan.new_text('=^.^=', font_size=70)

@nyan.repeat_forever
async def move_cat():
    cat.x = nyan.random_number(-200, 200)
    cat.y = nyan.random_number(-200, 200)
    cat.color = nyan.random_color()
    
    cat.show()

    await nyan.sleep(seconds=0.4)

    cat.hide()

    await nyan.sleep(seconds=0.4)

@cat.when_clicked
def win_function():
    cat.show()
    cat.text = 'You won!'

nyan.start_program()