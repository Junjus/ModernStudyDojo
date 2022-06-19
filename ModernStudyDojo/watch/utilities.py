

# Define helper functions

def handle_uploaded_file(f):
    with open(f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def user_video_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)