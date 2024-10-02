from pyfiglet import Figlet
from hello_git import style_text

for style in style_text():
    f = Figlet(font='starwars')
    print(f.renderText(style))
