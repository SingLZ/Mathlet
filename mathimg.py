from matplotlib import font_manager, figure
import matplotlib as mpl
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas 
import threading
import io
import numpy as np
import PIL.Image as Image

from timeit import default_timer

font_manager.FontProperties('cm')

mpl.rcParams.update(mpl.rcParamsDefault) 
mpl.rcParams['savefig.transparent'] = True
mpl.rcParams['text.usetex'] = True # turn off temporarily if causing problems
mpl.use('Agg') # Set backend to Agg

texFont = font_manager.FontProperties(size=30, family='serif', math_fontfamily='cm')

fig = figure.Figure(figsize=(4, 2))
fig.patch.set_alpha(0)
FigureCanvas(fig)

import re
def fill(text, width=70):
    then = default_timer()
    lines = []
    current_line = ""
    line_length = 0
    in_control_sequence = False
    control_sequence_length = 0

    # pseudo text fill/wrap, does not actually fill up to width, but compromises when words become long

    for char in text:
        if char == "$":
            if in_control_sequence:
                line_length -= control_sequence_length
                control_sequence_length = 0
            in_control_sequence = not in_control_sequence

        if in_control_sequence:
            control_sequence_length += 1
            current_line += char
        else:
            current_line += char
            line_length += 1

            if line_length >= width:
                last_word_match = re.search(r'\b\w+$', current_line) # last word fits in remaining space
                if last_word_match:
                    last_word = last_word_match.group()
                    word_length = len(last_word)

                    # word fits on next line
                    if word_length > width:
                        # if huge word, make it its own line
                        lines.append(current_line.rstrip())
                        current_line = last_word
                    else:
                        # move last word to next line if unable to fit
                        current_line = current_line[:last_word_match.start()].rstrip()
                        lines.append(current_line)
                        current_line = last_word
                else:
                    lines.append(current_line.rstrip())
                    current_line = ""
                line_length = len(current_line)

    if current_line:
        lines.append(current_line)

    result = "\n".join(lines)
    now = default_timer() - then
    if now > 0.2:
        print(f"Text wrap/fill bottleneck detected. Time: {now}")

    return result

def make_img(txt: str, fileName: str = 'output', format: str = 'png', customDpi: int = 300, color: str = 'White'):
    txt = fill(txt, 20)
    fig.text(0.5, 0.5, txt, color=color, fontsize=texFont.get_size_in_points(), fontproperties=texFont, verticalalignment='center', horizontalalignment='center')
    fileName += f'.{format}'
    
    fig.savefig(fileName, dpi=customDpi, transparent=True, bbox_inches='tight', pad_inches=0.1) # adjust padding here
    fig.clear()
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
    make_img(' ', 'output', 'png')
    make_img(' ', 'choice1', 'png')
    make_img(' ', 'choice2', 'png')
    make_img(' ', 'choice3', 'png')
    make_img(' ', 'choice4', 'png')

thread = threading.Thread(target=pre_load)
thread.start()

if __name__ == "__main__":
    thread.join()
    #print(fill('Correct! We move onto multiplication after parentheses'))
    # empty

#render_output([r'$\frac{1}{2} + \frac{1}{3}$', r'$\frac{1}{3} + \frac{4}{3}$', r'$\frac{x}{z} + \frac{2}{y}$'])