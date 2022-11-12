input_file = []
num_error = int(input())
for i in range(num_error):
    input_file.append(input())

allValid = []
err_list = []
for record in input_file:
    err_msg = record.split()
    assert len(err_msg) >= 2
    assert err_msg[1].lower() in ['true', 'false']
    allValid.append(1 if err_msg[1].lower() == 'true' else 0)
    
    if err_msg[1].lower() != 'true':
        err_list.append(err_msg[2])
    
if all(allValid):
    print('Yes')
else:
    print('No')
    print(err_list)
