def wrap(string, max_width):
    if 0<len(string)<1000 and 0<max_width<len(string):
        return '\n'.join(string[i:i+max_width]for i in range(0,len(string),max_width))
    else :
        return "Invalid Output"