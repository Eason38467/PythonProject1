
def filedead(filename):
    try:
        with open(filename) as f:
            content=f.read()
    except FileNotFoundError:
        msg='sorry, the file'+ filename +' does not exist.'
        print(msg)
    else:
        words = content.split()
        number=len(words)
        print('this file '+filename+' has about '+str(number)+' words.')
        print('they are:')
        for a in set(words):
            print(a)

filedead("session.log")
filedead('feature.txt')
filedead('showlog.log')