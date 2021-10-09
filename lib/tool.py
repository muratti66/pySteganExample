import errno
import os

IMG_SUFFIX = '-steganed'


class Toolkit:
    @staticmethod
    def get_re_named(f_path=str()) -> str:
        global IMG_SUFFIX
        fsp = os.path.splitext(os.path.basename(f_path))
        return '{}{}{}'.format(fsp[0], IMG_SUFFIX, fsp[1])

    @staticmethod
    def file_path_check(f_path=str()) -> None:
        if not os.path.isfile(f_path):
            FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), f_path)

    @staticmethod
    def dst_file_clean(f_path=str()) -> None:
        re_f_path = Toolkit.get_re_named(f_path=f_path)
        if os.path.isfile(re_f_path):
            os.remove(re_f_path)

    @staticmethod
    def check_params(args=tuple()) -> None:
        if args.__len__() < 2:
            raise Exception(
                'Please use the command like ./main.py /full/or/direct/path/file-is-here.png "message is here"')

    @staticmethod
    def get_params(args=tuple()) -> tuple:
        Toolkit.check_params(args=args)
        return str(args[1]).strip(), str(args[2]).strip()
