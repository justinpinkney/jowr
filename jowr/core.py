import cv2
import os

# Constants
DEFAULT_WINDOW_NAME = "default"
ESC_CODE = 27
"""Key code for Esc """


def show(frame, window_name=DEFAULT_WINDOW_NAME, wait_time=0, callbacks=None,
         esc_close=True, auto_close=True):
    """Show the image. Return False if quit key pressed."""
    # Could have another method e.g. show and close, or flash?
    # TODO deal with different data types
    cv2.imshow(window_name, frame)
    key_code = cv2.waitKey(wait_time)
    if callbacks and (key_code in callbacks):
        callbacks[key_code]()

    # Close the window on Esc
    if esc_close and (key_code is ESC_CODE):
        cv2.destroyWindow(window_name)

    # Close the window on timeout
    if auto_close and (key_code is -1):
        cv2.destroyWindow(window_name)


def play(frame_generator):
    """Convenience method to play all the frames in a iterable."""
    for frame in frame_generator:
        show(frame, wait_time=30, auto_close=False)
    close()


def close(window_name=DEFAULT_WINDOW_NAME):
    cv2.destroyWindow(window_name)


def im_read_resize(filename, new_width=0, new_height=0):
    return cv2.resize(cv2.imread(filename), None, fx=new_width, fy=new_height)


def rgb2gray(input_image):
    pass


def rgb2hsv(input_image):
    pass


def hsv2rgb(input_image):
    pass


def rgb2lab(input_image):
    pass


def lab2rgb(input_image):
    pass
