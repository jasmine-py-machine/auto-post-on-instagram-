import mimetypes    
def _is_video(file):
    if mimetypes.guess_type(file)[0].startswith('video'):
        return True
    else:
        return False
def check_file(file):
    if mimetypes.guess_type(file)[0].startswith('video') or mimetypes.guess_type(file)[0].startswith('image'):
        return True


