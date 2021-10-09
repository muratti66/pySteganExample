import sys
from lib.operation import SteganOps
from lib.tool import Toolkit

if __name__ == '__main__':

    img_path = sys.argv[1]

    print('* Checking image file path.')
    Toolkit.file_path_check(f_path=img_path)
    print('* Getting the message from file for test..')
    msg_from_file = SteganOps.image_to_message(img_path=img_path)
    print('* Message : "{}"'.format(msg_from_file))
