import subprocess


def dict_to_string(params_dict):
    str = ''
    for param_name, param_value in params_dict.items():
        str += f'{param_name},{param_value}\n'
    return str


if __name__ == '__main__':

    loop_param_name = 'numThreads'
    output_file_name = f'results/results_{loop_param_name}.csv'
    loop_values_list = [1, 2, 4, 8, 16, 32, 64, 128]

    params = {'numThreads': 32,
              'numTX': 10000,
              'numOpsPerTX': 10,
              'readRatio': 0.5,
              'writeRatio': 0.5,
              'deleteRatio': 0,
              'maxKey': 100000,
              'startAmountOfKeys': 10000,
              'rebuildMinTreeLeafSize': 4,
              'rebuildCollaborationThreshold': 60,
              }

    output_file = open(output_file_name, 'w')
    output_str = ','.join(list(params.keys()))
    output_str += ',Time,Aborts'
    output_str += '\n'

    for value in loop_values_list:
        f = open('config.csv', 'w')
        params[loop_param_name] = value
        config = dict_to_string(params_dict=params)
        output_str += ','.join([str(val) for val in list(params.values())])

        f.write(config)
        f.close()
        # now run java program and get output
        out = subprocess.check_output(
            ['java', '-cp', 'target/classes:target/test-classes:target/dependency/*', 'ISTWorkLoad', 'config.csv'])
        out_list = ' '.join(out.decode("utf-8").split('\n')).split(' ')
        time = out_list[out_list.index('[ms]') - 1]
        print(out_list)
        aborts = out_list[-2]
        output_str += f',{time},{aborts}'
        output_str += '\n'

    output_file.write(output_str)
