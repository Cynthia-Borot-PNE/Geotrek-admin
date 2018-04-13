from django.core.files.uploadedfile import SimpleUploadedFile

import factory
import base64


# Produce a small red dot
IMG_FILE = 'iVBORw0KGgoAAAANSUhEUgAAAAUAAAAFCAYAAACNbyblAAAAHElEQVQI12P4//8/w38GIAXDIBKE0DHxgljNBAAO9TXL0Y4OHwAAAABJRU5ErkJggg=='


def get_dummy_img():
    return base64.b64decode(IMG_FILE)


def get_dummy_uploaded_image(name='dummy_img.png'):
    return SimpleUploadedFile(name, get_dummy_img(), content_type='image/png')


def get_dummy_uploaded_file(name='dummy_file.txt'):
    return SimpleUploadedFile(name, b'HelloWorld', content_type='plain/text')


def get_dummy_uploaded_document(name='dummy_file.odt', size=128):
    return SimpleUploadedFile(name, ('*' * size).encode(), content_type='application/vnd.oasis.opendocument.text')


def dummy_filefield_as_sequence(toformat_name):
    """Simple helper method to fill a models.FileField"""
    return factory.Sequence(lambda n: get_dummy_uploaded_image(toformat_name % n))
