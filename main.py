import sys
from lib.operation import SteganOps
from lib.tool import Toolkit

if __name__ == '__main__':

    img_path, msg = Toolkit.get_params(args=sys.argv)
    re_img_path = Toolkit.get_re_named(f_path=img_path)

    print('* Checking image file path.')
    Toolkit.file_path_check(f_path=img_path)
    Toolkit.dst_file_clean(f_path=img_path)
    print('* Hidding the message in to {} file'.format(re_img_path))
    SteganOps.message_to_image(img_path=img_path, dst_img_path=re_img_path, msg=msg)
    print('* Getting the message from file for test..')
    msg_from_file = SteganOps.image_to_message(img_path=re_img_path)
    print('* Message will be testing..')
    if msg != msg_from_file:
        raise Exception('Hidden message is not matched with original message !!!')

    print('* All step is done, file is ready with message.')
