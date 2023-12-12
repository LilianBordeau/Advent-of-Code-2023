# Part Two

insideLoop = False
counter    = 0
inside     = {}

for y, blocs in enumerate(labyrinth):
    for x, bloc in enumerate(blocs):
        if (y,x) in history:
            if history[(y,x)] == 'D':
                insideLoop = not insideLoop
                #print(insideLoop)
        else:
            if insideLoop:
                inside[(y,x)] = bloc
                counter += 1
                
print(counter)

for y, blocs in enumerate(labyrinth):
    for x, bloc in enumerate(blocs):
        if (y,x) in history:
            if history[(y,x)] == 'D':
                print(bloc,end='')
                #print('■',end='')
            else:
                print(bloc,end='')
        else:
            if (y,x) in inside:
                print('0',end='')
            else:
                print('.',end='')
    print()