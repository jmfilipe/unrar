
import argparse
import logging
import os
import subprocess
import time

dir_path = os.path.dirname(os.path.realpath(__file__))
logging.basicConfig(filename=os.path.join(dir_path, 'debug.log'),
                    level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%Y-%m-%d %H:%M',
                    )

logging.info('Program Started.')

parser = argparse.ArgumentParser(
    description='This is a simple program to unzip the contents of a file',
)
parser.add_argument('-rar', action="store", dest="rar_path", type=str, help='path to the rar/zip/7zip executable')
parser.add_argument('-folder', action="store", dest="folder_path", type=str, help='path to the folder where the file is contained')
parser.add_argument('-file', action="store", dest="file_name", type=str, help='filename')

args = parser.parse_args()
logging.debug('RAR path: \'{}\''.format(args.rar_path))
logging.debug('File path: \'{}\''.format(args.folder_path))
logging.debug('File name: \'{}\''.format(args.file_name))

# check if file is a container:
path_ = os.path.join(args.folder_path, args.file_name)
logging.debug('Complete path: \'{}\''.format(path_))
to_unzip = True

if os.path.isfile(path_ + '.rar'):
    path_ += '.rar'
    logging.debug('File is a .rar file')
elif os.path.isfile(path_ + '.zip'):
    path_ += '.zip'
    logging.debug('File is a .zip file')
elif os.path.isfile(path_ + '.7z'):
    path_ += '.7z'
    logging.debug('File is a .rar file')
else:
    to_unzip = False
    logging.debug('File is not a container')

if to_unzip:
    time.sleep(10)

    all_files = os.listdir(args.folder_path)

    cmd = []
    cmd.append(f'{args.rar_path}')
    cmd.append('x')
    cmd.append(f'{path_}')
    cmd.append('-o{}'.format(args.folder_path))
    logging.debug('Running the following command: \'{}\''.format(''.join(cmd)))
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    logging.debug(stdout)
    logging.debug(stderr)

    time.sleep(10)
    new_all_files = os.listdir(args.folder_path)
    new_file = [f for f in new_all_files if f not in all_files]
    logging.debug('New file extracted successfully: {}'.format(new_file))

logging.info('Program Ended\n')
