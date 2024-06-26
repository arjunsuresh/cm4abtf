from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']

    env = i['env']

    state = i['state']

    print ('')
    print ('Current directory: {}'.format(os.getcwd()))

    print ('')

    extra = ''

    if env.get('CM_ABTF_ML_MODEL_TRAINING_PRETRAINED_PATH', '') != '':
        extra +=' --pretrained-model ' + env['CM_ABTF_ML_MODEL_TRAINING_PRETRAINED_PATH']


    if extra!='':
        print ('')
        print ('Extra command line: {}'.format(extra))

    env['CM_ABTF_EXTRA_CMD'] = extra

    return {'return':0}

def postprocess(i):

    return {'return':0}
