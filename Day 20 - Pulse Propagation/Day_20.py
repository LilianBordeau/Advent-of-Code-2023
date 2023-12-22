OFF, ON   = False, True
LOW, HIGH = 0, 1

# Get data // parse input

def parse_file(input_file):
    
    broadcast_mod = None
    flipflop_mods = {}
    conjunct_mods = {}
    
    with open(input_file, "r") as f:

        #for line in input_test.splitlines():
        for line in f:
            line  = line.replace('\n', '')
            if line[0] in ['%', '&']:
                outs = [v.strip() for v in line.split('->')[1].split(',')]
                if line[0] == '%':
                    mod = line.split('->')[0].split('%')[-1].strip()
                    flipflop_mods[mod] = [OFF, outs]
                elif line[0] == '&':
                    mod = line.split('->')[0].split('&')[-1].strip()
                    mem = {}
                    conjunct_mods[mod] = [mem, outs]
            else:
                outs = [v.strip() for v in line.split('->')[1].split(',')]
                broadcast_mod = outs

    # Add memory for conjunctions modules

    for conjunct_mod in conjunct_mods.keys():
        flipflop_inputs = [k for k,v in flipflop_mods.items() if conjunct_mod in v[1]]
        conjunct_inputs = [k for k,v in conjunct_mods.items() if conjunct_mod in v[1]]
        broadcast_input = ['broadcast'] if conjunct_mod in broadcast_mod else []

        all_inputs = flipflop_inputs + conjunct_inputs + broadcast_input
        for input_mod in all_inputs:
            conjunct_mods[conjunct_mod][0][input_mod] = LOW
            
    return broadcast_mod, flipflop_mods, conjunct_mods

def send_pulse(input_mod: str, output_mod: str, pulse: int = LOW):
    global queue
    queue.append((input_mod, output_mod, pulse))
    
def process_pulse(input_mod: str, output_mod: str, pulse: int = LOW):
    if pulse == LOW:
        #print(input_mod, '-low->', output_mod)
        pass
    elif pulse == HIGH:
        #print(input_mod, '-high->', output_mod)
        pass
        
    global LOW_PULSES_SENT
    global HIGH_PULSES_SENT
    
    if pulse == LOW : LOW_PULSES_SENT  += 1
    if pulse == HIGH: HIGH_PULSES_SENT += 1
    
    if output_mod == 'broadcast':
        broadcast(broadcast_mod, LOW)
    elif output_mod in flipflop_mods:
        flipflop   (input_mod, output_mod, pulse)
    elif output_mod in conjunct_mods:
        conjunction(input_mod, output_mod, pulse)
        
def broadcast(broadcast_mod: list = [], pulse: int = LOW):
    for module in broadcast_mod:
        send_pulse('broadcast', module, pulse)
        
def conjunction(input_mod: str, output_mod: str, pulse: int = LOW):
    if output_mod in conjunct_mods:
        conjunct_mods[output_mod][0][input_mod] = pulse
        
        if len(conjunct_mods[output_mod][0]) == sum(conjunct_mods[output_mod][0].values()):
            for module in conjunct_mods[output_mod][1]:
                send_pulse(output_mod, module, LOW)
        else:
            for module in conjunct_mods[output_mod][1]:
                send_pulse(output_mod, module, HIGH)
    else:
        return -1
    
def flipflop(input_mod: str, output_mod: str, pulse: int = LOW):
    if output_mod in flipflop_mods:
        if pulse == LOW:
            if  flipflop_mods[output_mod][0]  == False:
                for module in flipflop_mods[output_mod][1]:
                    send_pulse(output_mod, module, HIGH)
            elif flipflop_mods[output_mod][0] == True:
                for module in flipflop_mods[output_mod][1]:
                    send_pulse(output_mod, module, LOW)        
            flipflop_mods[output_mod][0] = not flipflop_mods[output_mod][0]
    else:
        return -1
    
def push_button(times: int = 1):
    global queue
    global count_pushs
    
    if times == -1:
        i = 1
        while(1):
            count_pushs = i
            send_pulse('button', 'broadcast', LOW)
            process_queue()
            i += 1
    else:
        for i in range(times):
            count_pushs = i + 1
            send_pulse('button', 'broadcast', LOW)
            process_queue()
            
def process_queue():
    global queue
    global tracking
    global count_queue
    global count_pushs
    
    count_queue = 0
    
    while queue:
        #print('\t\t\t\t\tQ:', queue)
        (input_mod, output_mod, pulse) = queue.pop(0)
        if input_mod == 'kl' and output_mod == 'rx' and pulse == LOW:
            break
            
        
        if output_mod == 'kl' and pulse == HIGH:
            tracking[input_mod].append(count_pushs)
                
        process_pulse(input_mod, output_mod, pulse)
        count_queue += 1
        
if __name__ == '__main__':

    input_file  = "input_day_20.txt"

    broadcast_mod, flipflop_mods, conjunct_mods = parse_file(input_file)

    #print('bc:',  broadcast_mod)
    #print('ff:', flipflop_mods)
    #print('cj:', conjunct_mods)
    #print()
    
    tracking = {
    'mk': [],
    'fp': [],
    'xt': [],
    'zc': []
    }
    
    LOW_PULSES_SENT  = 0
    HIGH_PULSES_SENT = 0 

    queue = []
    count_pushs = 0
    count_queue = 0

    push_button(10000)

    score = LOW_PULSES_SENT * HIGH_PULSES_SENT

    print('Low pulses sent:', LOW_PULSES_SENT)
    print('High pulses sent:', HIGH_PULSES_SENT)
    print('Score:', score)
    print('Count:', count_pushs)
    
    cycles = [min(l) for l in tracking.values()]
    result = math.lcm(*cycles)
    print(cycles)
    print('RX will be fired with LOW PULSE at button push', result)