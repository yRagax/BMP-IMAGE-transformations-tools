def RGB_to_HSV(R,G,B):
    Bb = B/255
    Gg = G/255
    Rr = R/255
    C_max = max(Bb,Gg,Rr)
    C_min = min(Bb,Gg,Rr)
    delta = C_max - C_min
    V = C_max
    S = (0 if C_max==0 else delta/C_max)
    if delta==0:
        H = 0
    elif C_max == Rr:
        H = (((Gg-Bb)/delta)%6)/6
    elif C_max == Gg:
        H = (((Bb-Rr)/delta)+2)/6
    else:
        H = (((Rr-Gg)/delta)+4)/6
    return H,S,V