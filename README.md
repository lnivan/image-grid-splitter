<div align="center">

# Image Grid Splitter

*A one-button desktop tool that cuts a photo into a 4 × 4 grid of tiles, for printing a large poster on ordinary sheets.*

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-30363D?style=flat-square)
![Pillow](https://img.shields.io/badge/Pillow-30363D?style=flat-square)
![Status](https://img.shields.io/badge/status-working-2DA44E?style=flat-square)

</div>

## About

A small Tkinter window with a single button. You pick a photo, and the script cuts it into 16 tiles of almost equal size and saves them, numbered in reading order, in a new folder next to the original. The tiles are meant to be printed on A4 or A3 sheets and joined into an A0-sized poster. The cropping is done with Pillow, and the window, file picker and message boxes are plain Tkinter.

> [!NOTE]
> The window text, file picker title and messages are in Spanish. The button reads `Seleccionar Foto y Dividir` ("Select photo and split").

## Quick start

```bash
python -m pip install -r requirements.txt
python divisor_imagenes.py
```

## Controls

| Input | Action |
| --- | --- |
| `Seleccionar Foto y Dividir` button | Choose a PNG, JPEG, BMP, WebP or TIFF file and split it |
| Close the window | Quit |

## How it works

- **Tile size.** For an image of $W \times H$ pixels split into $4 \times 4$ cells, each tile is $\lfloor W/4 \rfloor \times \lfloor H/4 \rfloor$ pixels. The last column and the last row absorb the remainder, so no pixel is lost. A 1003 × 707 image, for example, gives tiles of 250 × 176 px, 253 px wide in the last column and 179 px tall in the last row.
- **Cropping.** Tile $(r, c)$ is cut with `Image.crop` from the box $(c\,w,\ r\,h,\ c\,w + w,\ r\,h + h)$, where $w$ and $h$ are the tile width and height and the right and bottom edges of the last column and row are moved to the image border.
- **Output.** Tiles go to a folder named `<name>_16_partes` ("16 parts") beside the source image, as `<name>_parte_01` to `<name>_parte_16` with the original extension. The two-digit numbers keep them in order when sorted by name, row by row from the top left.
- **Feedback.** A message box reports the output folder when it finishes, and any exception is shown in an error box instead of crashing the window.

## Limitations

- The grid is fixed at 4 × 4 in the interface. `split_image` takes `rows` and `cols` arguments, but the button always passes 4 and 4.
- Tiles keep the photo's own aspect ratio, so they only fill A-series sheets exactly when the photo has the $1 : \sqrt 2$ shape of the paper. There is no overlap margin for trimming or gluing.
- JPEG tiles are re-encoded at Pillow's default quality of 75, so they lose a little detail compared with the original.
- The EXIF orientation tag is ignored, so a phone photo that is stored sideways is split sideways.
- Running it twice on the same photo silently overwrites the earlier tiles.

---

<div align="center"><sub>Part of <a href="https://github.com/lnivan">lnivan's projects</a> · <b>Tools</b></sub></div>
