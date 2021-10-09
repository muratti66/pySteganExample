from stegano import lsb


class SteganOps:
    @staticmethod
    def message_to_image(img_path=str(), dst_img_path=str(), msg=str()) -> None:
        secret = lsb.hide(img_path, msg)
        secret.save(dst_img_path)

    @staticmethod
    def image_to_message(img_path=str()) -> str():
        return lsb.reveal(img_path)
