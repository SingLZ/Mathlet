from matplotlib import font_manager, figure
import matplotlib as mpl
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 
import threading
import io
import numpy as np
from PIL import Image, ImageFont

font_manager.FontProperties('cm')

mpl.rcParams.update(mpl.rcParamsDefault) 
mpl.rcParams['savefig.transparent'] = True
mpl.rcParams['text.usetex'] = True # turn off temporarily if causing problems
mpl.use('Agg') # Set backend to Agg

texFont = font_manager.FontProperties(size=30, family='serif', math_fontfamily='cm')
from timeit import default_timer

pad_inches = 0.1
fig = figure.Figure(figsize=(4, 2))
FigureCanvas(fig)

font = ImageFont.truetype(font_manager.findfont(texFont), int(texFont.get_size_in_points()))
total_width = 0
num_characters = 0
for i in range(32, 127): # ASCII characters range from 32 to 126
    width = font.getlength(chr(i))
    total_width += width
    num_characters += 1

average_width = total_width / num_characters
def text_wrap(txt: str, max_line_amount: float = 20.0, size: int = 40, debug: bool = False):
    single_width = texFont.get_size_in_points() * average_width // 72 # each pt is 72 inches long
    max_line_amount = int((max_line_amount - pad_inches)*single_width) 
    current = 0
    new_txt = ""
    print('new max line amount:', max_line_amount)
    while True:
        if current != 0 or current > len(txt)*single_width:
            new_txt += (debug and r'\n') or '\n'
            if current < max_line_amount:
                new_txt += txt[current:len(txt)]
                break
        new_txt += txt[current:(current+max_line_amount)]
        current += max_line_amount

def make_img(txt: str, fileName: str = 'output', format: str = 'png', customDpi: int = 300, color: str = 'White'):
    then = default_timer()

    fig.text(0.5, 0.5, txt, color=color, fontsize=texFont.get_size_in_points(), fontproperties=texFont, verticalalignment='center', horizontalalignment='center')
    fileName += f'.{format}'
    
    fig.savefig(fileName, dpi=customDpi, transparent=True, bbox_inches='tight', pad_inches=0.1) # adjust padding here
    fig.clear()
    if default_timer() - then > 0.5:
        print('test', '%.4f' % (default_timer() - then))
    return fileName

# make_img is the fastest, but make_bytes is the best for network connectivity, so only use if transferring images
def make_bytes(txt: str, fileName: str = 'output', format: str = 'png', customDpi: int = 300, color: str = 'White'):
    fig.text(0.5, 0.5, txt, color=color, fontsize=texFont.get_size_in_points(), fontproperties=texFont, verticalalignment='center', horizontalalignment='center')

    buf = io.BytesIO()
    fig.savefig(buf, dpi=customDpi, transparent=True, bbox_inches='tight', pad_inches=pad_inches, format=format)
    buf.seek(0)

    img_arr = np.asarray(bytearray(buf.read()), dtype=np.uint8)
    pil_im = Image.fromarray(img_arr)
    b = io.BytesIO()
    pil_im.save(b, 'png')
    im_bytes = b.getvalue()

    fig.clear()

    return im_bytes

def render_output(new_txt: list | str, fileName='output'):
    txt = isinstance(new_txt, list) and '\n'.join(new_txt) or new_txt  # join the expressions with the newline character
    return make_img(txt, fileName, 'png', 300, 'White')

def pre_load():
    make_img('', 'output', 'png')
    make_img('', 'choice1', 'png')
    make_img('', 'choice2', 'png')
    make_img('', 'choice3', 'png')
    make_img('', 'choice4', 'png')

thread = threading.Thread(target=pre_load)
thread.start()

if __name__ == "__main__":
    thread.join()
    from random import randint
    randomized = r'$\frac{1}{2} + \frac{1}{3}$' #chr(randint(ord('a'), ord('z')))
    then = default_timer()
    make_bytes(randomized + ' $x^{2}$', 'output')
    time1 = default_timer() - then

    then = default_timer()
    make_img(randomized + ' $x^{2}$', 'output')
    
    print("Image size is", Image.open("output.png").size)
    print("Wrapped result is", text_wrap(randomized, 20.0, 40, True))
    print(f'bytes: {time1}, image: {default_timer() - then}')

#render_output([r'$\frac{1}{2} + \frac{1}{3}$', r'$\frac{1}{3} + \frac{4}{3}$', r'$\frac{x}{z} + \frac{2}{y}$'])