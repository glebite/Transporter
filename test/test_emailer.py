
"""
test_emailer - testcases for the Transporter class
"""
import sys
import pytest
sys.path.append('../src')
from transporter import Transporter

@pytest.mark.test_id(1)
def test_Transporter_creation():
    trans_obj = Transporter()
    assert trans_obj is not None

@pytest.mark.test_id(2)
def test_Transporter_field_validation():
    trans_obj = Transporter(from_address='what@test.com', to_address='what2@test2.com', user_password='secret', subject='something')
    assert trans_obj.msg_root['From'] == 'what@test.com'
    assert trans_obj.msg_root['To'] == 'what2@test2.com'
    assert trans_obj.msg_root['Subject'] == 'something'
    assert trans_obj.password == 'secret'

@pytest.mark.test_id(3)
def test_Transporter_message_text():
    trans_obj = Transporter()
    trans_obj.build_message_text(string_message='this is a message')
    assert trans_obj.string_message == 'this is a message'

# beginning to add tests first and then correcting code from here on in
@pytest.mark.test_id(4)
def test_Transporter_no_args_send():
    trans_obj = Transporter()
    try:
        trans_obj.send_it()
        assert False
    except ValueError as e:
        assert True

@pytest.mark.test_id(5)
def test_Transporter_no_images():
    trans_obj = Transporter()
    trans_obj.add_images()
    # if there are no images, then no Content-ID added to msg_root
    assert 'Content-ID' not in trans_obj.msg_root

@pytest.mark.test_id(6)
def test_Transporter_missing_images():
    trans_obj = Transporter()
    trans_obj.add_images(["missing_image.jpg"])
    # if there are no images, then no Content-ID added to msg_root
    assert 'Content-ID' not in trans_obj.msg_root

@pytest.mark.test_id(7)
def test_Transporter_images_is_a_string_and_is_missing():
    trans_obj = Transporter()
    trans_obj.add_images("missing_image.jpg")
    # if there are no images, then no Content-ID added to msg_root
    assert 'Content-ID' not in trans_obj.msg_root
