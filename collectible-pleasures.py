"""This script generates a three-letter GIF, in the style of Unknown Pleasures."""
import os

dirname = os.path.split(__file__)[0]
outdir = os.path.join(dirname, "gifs")
w, h = 640, 640  # width, height
lw = w / 3  # letter width
lineSpace = h / 50  # space between lines


def main(nft):
    """Runs all the functionality."""
    for i in range(4):
        newPage(w, h), frameDuration(1 / 12)
        with savedState():
            fill(0), rect(0, 0, w, h)
        createNft(nft)
    saveImage(os.path.join(outdir, f'{nft.replace(" ", "0")}.gif'))
    newDrawing()


def createNft(nft):
    """Generates the art."""
    for i, letter in enumerate([l for l in nft]):
        position = lw * i
        for mod in letters[letter]:
            module(*mod, position)


def module(reps, kndList, wave=0, xTrans=0):
    """Generates the art."""
    fill(None), stroke(1), strokeWidth(1)
    for _ in range(int(reps)):
        points = lsPts(kndList)
        path = BezierPath()
        with savedState():
            translate(xTrans, lw * 0.2 + wave)
            path.moveTo((0, 0)), path.curveTo(*points)
            drawPath(path)
        wave += lineSpace


def lsPts(num, wave=lw * 0.5):
    """Generates the points of the waves."""
    points = []
    for x in range(0, int(lw), 4):
        if num == 1:
            y = setY(x, wave, 0.1, 0.9)
        elif num == 2:
            y = setY(x, wave, 0.1, 0.4)
        elif num == 3:
            y = setY(x, wave, 0.1, 0.9, True)
        elif num == 4:
            y = setY(x, wave, 0.35, 0.65)
        elif num == 5:
            y = setY(x, wave, 0.1, 0.7)
        elif num == 6:
            y = setY(x, wave, 0.1, 0.9, True, 2, {"l": 0.1, "r": 0.01})
        elif num == 7:
            y = setY(x, wave, 0.6, 0.9)
        elif num == 8:
            y = setY(x, wave, 0.1, 0.9, True, 3)
        elif num == 9:
            y = setY(x, wave, 0.1, 1)
        else:
            break
        if y < 0:
            points.append([x, y * -1])
        else:
            points.append([x, y])
    return points


def setY(x, wave, left, right, chopped=False, chops=2, ch={"l": 0.1, "r": 0.1}):
    """Sets the y height of every point in the wave."""
    half = left + (right - left) / 2
    third = left + (right - left) / 3
    a1, a2, a3, a4 = (
        x > 0 and x < lw * left,
        x > lw * right and x <= lw,
        x > lw * (half - ch["l"]) and x < lw * (half + ch["r"]),
        x > lw * third and x < lw * (third + ch["r"]),
    )
    b1, b2, b3, b4, b5 = (
        x > lw * left,
        x <= lw * half,
        x <= lw * (half - ch["l"] * 2),
        x > lw * (half + ch["r"]) and x < lw * (half + ch["r"] * 2),
        x > lw * (third + ch["r"]) and x < lw * (third + ch["r"] * 2),
    )
    c1, c2, c3, c4, c5 = (
        x > lw * half,
        x <= lw * right,
        x > lw * (half - ch["l"] * 2) and x <= lw * (half - ch["l"]),
        x >= lw * (half + ch["r"] * 2),
        x >= lw * (third + ch["r"] * 3),
    )
    a, b, c = (a1 or a2, b1 and b2, c1 and c2)

    if chopped and chops == 2:
        a = a1 or a3 or a2
        b = (b1 and b3) or b4
        c = c3 or (c4 and c2)
    if chopped and chops == 3:
        a = a4
        b = (b1 and b3) or b5
        c = c3 or (c5 and c2)

    if a:
        y = sin(x * randint(1, 3))
    elif b:
        y = (x * sin(radians(x * randint(-100, 100)))) / 10
    elif c:
        y = (wave * sin(radians(wave * randint(-100, 100)))) / 10
    else:
        y = 0
    return y


letters = {
    "A": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.4) / lineSpace, 3, h * 0.4],
        [(h * 0.1) / lineSpace, 1, h * 0.3],
        [(h * 0.3) / lineSpace, 3, 0],
    ],
    "B": [
        [(h * 0.1) / lineSpace, 5, 0],
        [(h * 0.3) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 5, h * 0.4],
        [(h * 0.3) / lineSpace, 3, h * 0.5],
        [(h * 0.1) / lineSpace, 5, h * 0.8],
    ],
    "C": [
        [(h * 0.1) / lineSpace, 1, 0],
        [(h * 0.1) / lineSpace, 3, h * 0.1],
        [(h * 0.5) / lineSpace, 2, h * 0.2],
        [(h * 0.1) / lineSpace, 3, h * 0.7],
        [(h * 0.1) / lineSpace, 1, h * 0.8],
    ],
    "D": [
        [(h * 0.1) / lineSpace, 5, 0],
        [(h * 0.7) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 5, h * 0.8],
    ],
    "E": [
        [(h * 0.1) / lineSpace, 1, 0],
        [(h * 0.3) / lineSpace, 2, h * 0.1],
        [(h * 0.1) / lineSpace, 1, h * 0.4],
        [(h * 0.3) / lineSpace, 2, h * 0.5],
        [(h * 0.1) / lineSpace, 1, h * 0.8],
    ],
    "F": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.3) / lineSpace, 2, h * 0.5],
        [(h * 0.1) / lineSpace, 1, h * 0.4],
        [(h * 0.4) / lineSpace, 2, 0],
    ],
    "G": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.1) / lineSpace, 3, h * 0.7],
        [(h * 0.2) / lineSpace, 2, h * 0.5],
        [(h * 0.1) / lineSpace, 6, h * 0.4],
        [(h * 0.3) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 1, 0],
    ],
    "H": [
        [(h * 0.4) / lineSpace, 3, 0],
        [(h * 0.1) / lineSpace, 1, h * 0.4],
        [(h * 0.4) / lineSpace, 3, h * 0.5],
    ],
    "I": [
        [(h * 0.1) / lineSpace, 1, 0],
        [(h * 0.7) / lineSpace, 4, h * 0.1],
        [(h * 0.1) / lineSpace, 1, h * 0.8],
    ],
    "J": [
        [(h * 0.5) / lineSpace, 7, h * 0.4],
        [(h * 0.3) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 1, 0],
    ],
    "K": [
        [(h * 0.4) / lineSpace, 3, 0],
        [(h * 0.1) / lineSpace, 5, h * 0.4],
        [(h * 0.4) / lineSpace, 3, h * 0.5],
    ],
    "L": [
        [(h * 0.8) / lineSpace, 2, h * 0.1],
        [(h * 0.1) / lineSpace, 1, 0],
    ],
    "M": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.8) / lineSpace, 8, 0],
    ],
    "N": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.8) / lineSpace, 3, 0],
    ],
    "O": [
        [(h * 0.1) / lineSpace, 1, 0],
        [(h * 0.7) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 1, h * 0.8],
    ],
    "P": [
        [(h * 0.1) / lineSpace, 5, h * 0.8],
        [(h * 0.4) / lineSpace, 3, h * 0.4],
        [(h * 0.1) / lineSpace, 5, h * 0.3],
        [(h * 0.3) / lineSpace, 2, 0],
    ],
    "Q": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.7) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 9, 0],
    ],
    "R": [
        [(h * 0.1) / lineSpace, 5, h * 0.8],
        [(h * 0.3) / lineSpace, 3, h * 0.5],
        [(h * 0.1) / lineSpace, 5, h * 0.4],
        [(h * 0.4) / lineSpace, 3, 0],
    ],
    "S": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.2) / lineSpace, 3, h * 0.6],
        [(h * 0.1) / lineSpace, 2, h * 0.5],
        [(h * 0.1) / lineSpace, 1, h * 0.4],
        [(h * 0.1) / lineSpace, 7, h * 0.3],
        [(h * 0.2) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 1, 0],
    ],
    "T": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.8) / lineSpace, 4, 0],
    ],
    "U": [
        [(h * 0.8) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 1, 0],
    ],
    "V": [
        [(h * 0.8) / lineSpace, 3, h * 0.1],
        [(h * 0.1) / lineSpace, 4, 0],
    ],
    "W": [
        [(h * 0.8) / lineSpace, 8, h * 0.1],
        [(h * 0.1) / lineSpace, 1, 0],
    ],
    "X": [
        [(h * 0.4) / lineSpace, 3, 0],
        [(h * 0.1) / lineSpace, 4, h * 0.4],
        [(h * 0.4) / lineSpace, 3, h * 0.5],
    ],
    "Y": [
        [(h * 0.5) / lineSpace, 3, h * 0.4],
        [(h * 0.4) / lineSpace, 4, 0],
    ],
    "Z": [
        [(h * 0.1) / lineSpace, 1, h * 0.8],
        [(h * 0.2) / lineSpace, 7, h * 0.6],
        [(h * 0.2) / lineSpace, 4, h * 0.4],
        [(h * 0.3) / lineSpace, 2, h * 0.1],
        [(h * 0.1) / lineSpace, 1, 0],
    ],
    " ": [[(h * 0.9) / lineSpace, 1, 0]],
}


if __name__ == "__main__":
    alphabet = "".join(letters.keys())
    for i in alphabet:
        for j in alphabet:
            for k in alphabet:
                cnft = f"{i}{j}{k}".lower().replace(" ", "0")
                if f'{cnft}.gif' in os.listdir(outdir): continue
                else: main(cnft)
