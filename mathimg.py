from matplotlib import font_manager, figure
import matplotlib as mpl
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 
import threading

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
    if default_timer() - then > 0.5:
        print('test', '%.4f' % (default_timer() - then))
    return fileName

def render_output(new_txt: list | str, fileName='output'):
    txt = isinstance(new_txt, list) and '\n'.join(new_txt) or new_txt  # join the expressions with the newline character
    return make_img(txt, fileName, 'png', 300, 'White')

def pre_load():
    make_img('', 'output', 'png')
    make_img('', 'choice1', 'png')
    make_img('', 'choice2', 'png')
    make_img('', 'choice3', 'png')
    make_img('', 'choice4', 'png')

threading.Thread(target=pre_load).start()
#render_output([r'$\frac{1}{2} + \frac{1}{3}$', r'$\frac{1}{3} + \frac{4}{3}$', r'$\frac{x}{z} + \frac{2}{y}$'])