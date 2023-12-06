import re

#read text file
f = open("input_7_1.txt", 'r')
lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

#list of method names
methods = {}

#search all method names and append (name&defined line) to list
for i, line in enumerate(lines):
    r_e=re.compile("^def\s\w+")
    match = r_e.search(line)
    if match != None:
        name = match.group().split()[1]
        def_num = i + 1
        methods[name] = {'def_num' : def_num}

#dictionary of method informations
info = {}

#fill informations
for method_key, method_value in methods.items():
    #check the number of method's parameters
    def_index = method_value['def_num'] - 1
    def_re = re.compile(method_key+"\(([^)]*)")
    parameters = def_re.search(lines[def_index]).group().replace('(',',').split(',')
        #parameters = [ method_key , param1, param2, ... ]
    if parameters[len(parameters)-1] == '' :
        parameters.remove('')    

    #look for method calls
    call_re = re.compile(method_key + "\(([^)]*)")
    calls = []
    for i, line in enumerate(lines):
        call = call_re.search(line)
        if call != None and i != def_index:
            call_params = call.group().replace('(',',').split(',')
            if call_params[len(call_params)-1] == '':
                call_params.remove('')
            if len(parameters) == len(call_params):
                calls.append(i+1)

    #print result for current method
    result = method_key + ": def in " + str(def_index+1) + ", calls in"
    print(result, calls)


f.close()
