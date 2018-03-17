"""
Project Information:
    Author      : Pallab Maji
    Co-Authors  : Rahul Ambati
    Date        : 
    Project     : PoesNet - Pose Estimation Network
    
Functional Information:
    Aim     : To detect joint points and in turn generate skeleton for all persons present in the image
    Inputs  :
    Outputs :
    
"""
import datetime


def logger(file, str2log):
    with open(file, 'w+') as fptr:
        fptr.write(str(datetime.datetime.now()) + ':\t' + str2log + '\n')


