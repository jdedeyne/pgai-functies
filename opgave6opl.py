def line(length, fill = True, indentation = 0,  char = '*'):
    ret = ''
    space =  ' ' * indentation if indentation > 0 else ''
    cont = ''
    i=0
    while i<length:        
        if i>0 and i<length-1:
            if fill:
                cont += char
            else:
                cont += ' '
        else:
            cont += char        
        i+=1
    ret = space + cont
    return ret

def rectangle(width, height, fill = True, indentation = 0,  char = '*'):
    h=0
    ret = ''
    while h<height:
        if h==0 or h==height-1:
            #boven en onderlijn
            ret += line(width, fill=True, indentation= indentation, char = char)
        else:
            ret += line(width, fill=fill, indentation=indentation, char = char) 
        if h<height-1:
            ret += '\r\n'
        h+=1
    return ret


def square(size, fill = True, indentation = 0,  char = '*'):
    ret = rectangle(size, size, fill= fill, indentation=indentation, char=char)
    return ret


def parallelogram(width, height, fill = True, indentation = 0,  char = '*', step = -1):
    ret = ''
    h=0
    i=indentation
    if step < 0:
        i-=(step*(height-1))

    while h<height:
        print(h,i)        
        if h==0 or h==height-1:
            ret += line(width, fill=True, indentation = i, char=char)
        else:
            ret += line(width, fill=fill, indentation = i, char=char)
        if h<height-1:
            ret += '\r\n'
        i+=step
        h+=1
    return ret

def triangle(width, fill = True, indentation = 0,  char = '*', step = 0, alignRight = False, fromTopToBottom = True, rightAngled = True):
    ret = ''
    h=1
    i=indentation
    s=step
    if rightAngled:
        if fromTopToBottom:
            if alignRight:
                i=i+width-1
                s=-1            
            while h < width+1:        
                if h==1 or h==width:
                    ret += line(h, fill=True, indentation = i, char=char)
                else:
                    ret += line(h, fill=fill, indentation = i, char=char)
                if h<width:
                    ret += '\r\n'
                i += s
                h+=1
        else:
            if alignRight:
                s=step
            h=width
            while h > 0:        
                if h==1 or h==width:
                    ret += line(h, fill=True, indentation = i, char=char)
                else:
                    ret += line(h, fill=fill, indentation = i, char=char)
                if h>1:
                    ret += '\r\n'
                i += s
                h-=1
    else:
        if width%2==1:
            hmax=int((width+1)/2)
            w=1
        else:
            hmax=int(width/2)
            w=2

        if fromTopToBottom:
            h=1
            
            i = i + hmax - 1
            #gelijkbenig, alignRight negeren

            while h <= hmax:        
                if h==1 or h==hmax:
                    ret += line(w, fill=True, indentation = i, char=char)
                else:
                    ret += line(w, fill=fill, indentation = i, char=char)
                if h<hmax:
                    ret += '\r\n'
                i -= 1
                h+=1
                w+=2
        else:
            h=1
            w=width
            #gelijkbenig, alignRight negeren

            while h <= hmax:        
                if h==1 or h==hmax:
                    ret += line(w, fill=True, indentation = i, char=char)
                else:
                    ret += line(w, fill=fill, indentation = i, char=char)
                if h<hmax:
                    ret += '\r\n'
                i += 1
                h += 1
                w -= 2
    return ret