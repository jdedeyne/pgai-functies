def line(length, fill=True, indentation=0,  char='*'):
    cont = ''
    for i in range(0, indentation):
        cont += ' '
    for i in range(0, length):
        if 0 < i < length - 1:
            if fill:
                cont += char
            else:
                cont += ' '
        else:
            cont += char
    return cont

def shape(indentstart, indentstep, widthstart, widthstep, height, fill, char):
    ret = ''
    for h in range(1, height + 1):
        ret += line(widthstart, fill=fill or (h == 1 or h == height), indentation=indentstart, char=char)
        if h < height:
            ret += '\r\n'
        indentstart += indentstep
        widthstart += widthstep
    return ret

def rectangle(width, height, fill=True, indentation=0,  char='*'):
    return shape(indentation, 0, width, 0, height, fill, char)


def square(size, fill=True, indentation=0,  char='*'):
    return rectangle(size, size, fill=fill, indentation=indentation, char=char)


def parallelogram(width, height, fill=True, indentation=0, char='*', step=-1):
    if step < 0:
        indentation -= (step*(height-1))
    return shape(indentation, step, width, 0, height, fill, char)


def rightAngledTriangle(width, fill=True, indentation=0,  char='*', step=0, alignRight=False, fromTopToBottom=True):
    ret = ''
    if fromTopToBottom:
        if alignRight:
            indentation = indentation + width - 1
            step = -1
        ret += shape(indentation, step, 1, 1, width, fill, char)
    else:
        ret += shape(indentation, step, width, -1, width, fill, char)

    return ret

def nonRightAngledTriangle(width, fill=True, indentation=0,  char='*', step=0, alignRight=False, fromTopToBottom=True):
    ret = ''
    hmax = int((width + (width % 2)) / 2)
    w = 2 - (width % 2)
    if fromTopToBottom:
        indentation = indentation + hmax - 1
        ret += shape(indentation, -1, w, 2, hmax, fill, char)
    else:
        w = width
        ret += shape(indentation, 1, w, -2, hmax, fill, char)
    return ret


def triangle(width, fill=True, indentation=0,  char='*', step=0, alignRight=False, fromTopToBottom=True, rightAngled=True):
    ret = ''
    if rightAngled:
        ret = rightAngledTriangle(width, fill, indentation,  char, step, alignRight, fromTopToBottom)
    else:
        ret = nonRightAngledTriangle(width, fill, indentation, char, step, alignRight, fromTopToBottom)
    return ret