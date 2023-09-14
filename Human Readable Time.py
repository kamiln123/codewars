#funkcja zwraca godzinę która jest przeliczona z sekund
#np. make_readable(60), "00:01:00"
    
def make_readable(seconds):
    if seconds <60:
        return sec(seconds)
    elif seconds >=60 and seconds <3600:
        return minutes(seconds)
    elif seconds >=3600:
        return hours(seconds)

def sec(seconds):
    s=seconds
    if len(str(s)) ==1:
        return f'00:00:0{s}'
    elif len(str(s)) >1:
        return f'00:00:{s}'

def minutes(seconds):
    m=int(seconds/60)
    s=seconds-60*m
    if len(str(m)) ==1:
        if len(str(s)) ==1:
            return(f'00:0{m}:0{s}')
        elif len(str(seconds-60*int(seconds/60))) >1:
            return(f'00:0{m}:{s}')
    elif len(str(m)) >1:
        if len(str(s)) ==1:
            return(f'00:{m}:0{s}')
        elif len(str(s)) >1:
            return(f'00:{m}:{s}')

def hours(seconds):
    h=int(seconds/3600)
    m=int((seconds-3600*h)/60)
    s=seconds-3600*h-60*m
    if len(str(h)) ==1:
        if len(str(m)) ==1:
            if len(str(s)) ==1:
                return(f'0{h}:0{m}:0{s}')
            elif len(str(s)) >1:
                return(f'0{h}:{m}:{s}')
        elif len(str(m)) >1:
            if len(str(s)) ==1:
                return(f'0{h}:0{m}:0{s}')
            elif len(str(s)) >1:
                return(f'0{h}:{m}:{s}')
    elif len(str(h)) >1:
        if len(str(m)) ==1:
            if len(str(s)) ==1:
                return(f'{h}:0{m}:0{s}')
            elif len(str(s)) >1:
                return(f'{h}:0{m}:{s}')
        elif len(str(m)) >1:
            if len(str(s)) ==1:
                return(f'{h}:{m}:0{s}')
            elif len(str(s)) >1:
                return(f'{h}:{m}:{s}')
        
