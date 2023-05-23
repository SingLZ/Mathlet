from matplotlib import font_manager, figure
import matplotlib as mpl
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 
import threading
import io
import numpy as np
import PIL.Image as Image

font_manager.FontProperties('cm')

mpl.rcParams.update(mpl.rcParamsDefault) 
mpl.rcParams['savefig.transparent'] = True
mpl.rcParams['text.usetex'] = True # turn off temporarily if causing problems
mpl.use('Agg') # Set backend to Agg

texFont = font_manager.FontProperties(size=30, family='serif', math_fontfamily='cm')

from timeit import default_timer

fig = figure.Figure(figsize=(4, 2))
FigureCanvas(fig)

def make_img(txt: str, fileName: str = 'output', format: str = 'png', customDpi: int = 300, color: str = 'White'):
    then = default_timer()

    fig.text(0.5, 0.5, txt, color=color, fontsize=texFont.get_size_in_points(), fontproperties=texFont, verticalalignment='center', horizontalalignment='center')
    fileName += f'.{format}'
    
    fig.savefig(fileName, dpi=customDpi, transparent=True, bbox_inches='tight', pad_inches=0.1) # adjust padding here
    fig.clear()
    if default_timer() - then > 0.6:
        print('image load time:', '%.4f' % (default_timer() - then))
    return fileName

# make_img is the fastest, but make_bytes is the best for network connectivity, so only use if transferring images
def make_bytes(txt: str, fileName: str = 'output', format: str = 'png', customDpi: int = 300, color: str = 'White'):
    fig.text(0.5, 0.5, txt, color=color, fontsize=texFont.get_size_in_points(), fontproperties=texFont, verticalalignment='center', horizontalalignment='center')

    buf = io.BytesIO()
    fig.savefig(buf, dpi=customDpi, transparent=True, bbox_inches='tight', pad_inches=0.1, format=format)
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
    
    print(f'bytes: {time1}, image: {default_timer() - then}')

#render_output([r'$\frac{1}{2} + \frac{1}{3}$', r'$\frac{1}{3} + \frac{4}{3}$', r'$\frac{x}{z} + \frac{2}{y}$'])