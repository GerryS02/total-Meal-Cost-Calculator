# Module: ECGUI.py
#
# Python Version: 3.9
#
# Description: This module contains a collection of functions designed to make 
#              creating a GUI in Python easier for the beginning programmer. 
#              The programmer need only add this module to their project and 
#              place 'import ECGUI' (without the single quotation marks) at the 
#              top of their python file to use it.
#
#              It purposefully avoids using OOP to make it more understandable 
#              to the beginning programmer. There are also no libraries that 
#              need to be added to the standard Python installation to make this
#              module work.
#
#              Note that the GUI design concept is one of rows of controls in an 
#              ECGUI window, where any control can be a frame that contains more 
#              rows of controls. When any function is called, the programmer
#              has the option of providing (1) only those arguments without 
#              keywords, (2) a sequential subset of arguments starting at the 
#              first, (3) those arguments without keywords followed by key-value 
#              pairs of selected arguments, or (4) a sequential subset of 
#              arguments starting at the first followed by key-value pairs of 
#              selected arguments.
#
#              Examples:
#                  lbl_ex1 = ECGUI.add_label(root_window)
#                  lbl_ex2 = ECGUI.add_label(root_window, 'Hello World', 'red', 
#                                           'yellow')
#                  lbl_ex3 = ECGUI.add_label(root_window, message='Hello World', 
#                                            side='left', padding_left=5)
#                  lbl_ex4 = ECGUI.add_label(root_window, 'Hello World', 'red', 
#                                           'yellow', side='left', fill='x')
#
# Version: 1.1.0
# Last Modified: 11/1/2021
# Author: Linda Zuvich (linda.zuvich@edmonds.edu)
#         CS Department, Edmonds College, Lynnwood, WA
#
# License: This module may be used or distributed without modification by anyone
#          for personal or educational use. It may not be sold individually or
#          as part of any other program or collection of modules. Any
#          modification to the code requires that the module name be amended,
#          a list of the modifications be added to this header, and the authors
#          of the modification be added under the original author, with contact
#          information. The Version and Last Modified date must also be updated.
#          This license agreement must remain unchanged as it applies to all
#          future variants of this software.

import tkinter as tk
from tkinter import messagebox


# Function: make_window
# Description: Creates the ECGUI window in which all other components will
#              be added.
# Input: title (optional - default is 'ECGUI Window') - the text that
#              appears in the top left corner of the window's title bar
#        bg_color (optional - default is 'white') - the background color
#                             of the window, which can be a basic text
#                             color or a CSS-style hexadecimal value
#                             beginning with a hashtag
#                             (ex. 'white' or '#990000')
# Output: a reference to the window object created
def make_window(title='ECGUI Window', bg_color='white'):
    window = tk.Tk()
    window.title(title)
    window['background'] = bg_color
    return window


# Function: add_frame
# Description: Creates a frame (a container control) and places is in the
#              given container.
# Input: container - the window or frame that will hold this frame
#        bg_color (optional - default is 'white') - the background color of the
#                 frame, which can be a basic text color or a CSS-style
#                 hexadecimal value beginning with a hashtag (ex. 'white' or
#                 '#990000')
#        padding_top (optional - default is 0) - the amount of space above the
#                    label, measured in pixels
#        padding_right (optional - default is 0) - the amount of space after
#                      the label, measured in pixels
#        padding_bottom (optional - default is 0) - the amount of space below
#                       the label, measured in pixels
#        padding_left (optional - default is 0) - the amount of space before
#                     the label, measured in pixels
#        side (optional - default is '') - determines if this control should be
#             placed in its own row in the container or if it should be moved
#             to the 'left' or 'right' to make room for other controls in the
#             same row
#        fill (optional - default is 'none') - expands the frame to the
#             available space in the container, with options being 'x' for
#             horizontal, 'y' for vertical, 'both' for horizontal and vertical,
#             or 'none'
# Output: a reference to the frame created
def add_frame(container, bg_color='white', padding_top=0, padding_right=0,
              padding_bottom=0, padding_left=0, side='', fill='none'):
    frame = tk.Frame(container)
    if side == '' or (side != 'left' and side != 'right'):
        frame.pack(padx=(padding_left, padding_right),
                   pady=(padding_top, padding_bottom), expand=1, fill=fill)
    else:
        frame.pack(padx=(padding_left, padding_right),
                   pady=(padding_top, padding_bottom), side=side, expand=1,
                   fill=fill)
    frame['background'] = bg_color
    return frame


# Function: add_label
# Description: Adds a label control to a container, such as a window or a frame.
#              A label control displays a single line of text and can be used
#              as a heading, a prompt for an entry box, or a place to output
#              results.
# Input: container - the window or frame that will hold this label control
#        message (optional - default is '') - what the label should say
#        fg_color (optional - default is 'black') - the text color, which can
#                 be a basic text color or a CSS-style hexadecimal value
#                 beginning with a hashtag (ex. 'black' or '#990000')
#        bg_color (optional - default is 'white') - the background color, which
#                 can be a basic text color or a CSS-style hexadecimal value
#                 beginning with a hashtag (ex. 'black' or '#990000')
#        font_family (optional - default is the Tk default font for labels) -
#                    this may be any of the Tk platform-independent fonts such
#                    as 'TkFixedFont' or a system-specific font such as 'Arial'
#        font_size (optional - default is 12) - the size of the text, measured
#                  in points
#        bold (optional - default is False) - a Boolean (True or False) that
#             makes the label text bold or normal weight
#        italics (optional - default is False - a Boolean (True or False) that
#                makes the label text italics or not
#        padding_top (optional - default is 0) - the amount of space above the
#                    label text, measured in pixels
#        padding_right (optional - default is 0) - the amount of space after
#                      the label text, measured in pixels
#        padding_bottom (optional - default is 0) - the amount of space below
#                       the label text, measured in pixels
#        padding_left (optional - default is 0) - the amount of space before
#                     the label text, measured in pixels
#        side (optional - default is '') - determines if this control should be
#             placed in its own row in the container or if it should be moved
#             to the 'left' or 'right' to make room for other controls in the
#             same row
#        fill (optional - default is 'none') - expands the label to the
#             available space in the container, with options being 'x' for
#             horizontal, 'y' for vertical, 'both' for horizontal and vertical,
#             or 'none'
# Output: a reference to the label control created
def add_label(container, message='', fg_color='black', bg_color='white',
              font_family='', font_size=12, bold=False, italics=False,
              padding_top=0, padding_right=0, padding_bottom=0,
              padding_left=0, side='', fill='none'):
    if font_family != '':
        font_style = font_family + ' ' + str(font_size)
        if bold:
            font_style += ' bold'
        if italics:
            font_style += ' italic'
        label = tk.Label(container, text=message, fg=fg_color, bg=bg_color,
                         font=font_style)
    else:
        label = tk.Label(container, text=message, fg=fg_color, bg=bg_color)
    if side == 'left' or side == 'right':
        label.pack(padx=(padding_left, padding_right),
                   pady=(padding_top, padding_bottom), side=side,
                   expand=0 if fill == 'none' else 1, fill=fill)
    else:
        label.pack(padx=(padding_left, padding_right),
                   pady=(padding_top, padding_bottom),
                   expand=0 if fill == 'none' else 1, fill=fill)
    return label


# Function: change_label
# Description: Changes the setting and/or text of an existing label control.
# Input: label - the reference to the label control that should be changed
#        message (optional - default is the current message) - what the label
#                should say
#        fg_color (optional - default is the current color) - the text color,
#                 which can be a basic text color or a CSS-style hexadecimal
#                 value beginning with a hashtag (ex. 'black' or '#990000')
#        bg_color (optional - default is the current color) - the background
#                 color, which can be a basic text color or a CSS-style
#                 hexadecimal value beginning with a hashtag
#                 (ex. 'black' or '#990000')
#        font_family (optional - default is the current font) - this may be any
#                    of the Tk platform-independent font such as 'TkFixedFont'
#                    or a system-specific font such as 'Arial'
#        font_size (optional - default is the current size if no font family is
#                  selected or 12 pt. if one is) - the size of the text,
#                  measured in points
#        bold (optional - default is False) - a Boolean (True or False) that
#             makes the label text bold or normal weight, which only changes if
#             a font_family is provided
#        italics (optional - default is False) - a Boolean (True or False) that
#                makes the label text italics or not, which only changes if a
#                font_family is provided
# Output: nothing
def change_label(label, message='_SAME_', fg_color='', bg_color='',
                 font_family='', font_size=12, bold=False, italics=False):
    if message != '_SAME_':
        label.config(text=message)
    if fg_color != '':
        label['foreground'] = fg_color
    if bg_color != '':
        label['background'] = bg_color
    if font_family != '':
        font_style = font_family + ' ' + str(font_size)
        if bold:
            font_style += ' bold'
        if italics:
            font_style += ' italic'
        label.config(font=font_style)


# Function: get_label_text
# Description: Reports the text currently displayed in the given label.
# Input: label - the reference to the label control that should be changed
# Output: a string that holds the text in the given label
def get_label_text(label):
    return label['text']


# Function: load_image
# Description: Loads a gif or ppm image into the program, allowing it to be
#              added to a container using the add_image function. Note that
#              only images saved as a gif or ppm will work. There are free
#              converters online that will allow a jpg to be converted into a
#              ppm, such as:
#              https://onlineconvertfree.com/convert-format/jpg-to-ppm/
# Input: file_name - if the file is stored in the same directory as the program
#                    files, this should be just the file name with extension
#                    (ex. 'photo.ppm') or provide either the relative or
#                    complete directory path and the file name with extension
#                    (ex. 'images/photo.ppm')
# Output: a reference to the image stored in the program
def load_image(file_name):
    img = tk.PhotoImage(file=file_name)
    return img


# Function: add_image
# Description: Adds an image control to a container, such as a window or a
#              frame. Usually the width and height of the control matches the
#              dimensions of the image being displayed. The background color
#              will only show if the image is smaller thant the control or if
#              padding has been applied.
# Input: container - the window or frame that will hold this image control
#        image - the reference to the image already loaded into the program
#                that should be displayed in this control
#        width (optional - default is 300) - the width of the image control
#              in pixels
#        height (optional - default is 200) - the height of the image control
#               in pixels
#        bg_color (optional - default is 'white') - the background color, which
#                 can be a basic text color or a CSS-style hexadecimal value
#                 beginning with a hashtag (ex. 'black' or '#990000')
#        padding_top (optional - default is 0) - the amount of space above the
#        image, measured in pixels
#        padding_right (optional - default is 0) - the amount of space after
#                      the image, measured in pixels
#        padding_bottom (optional - default is 0) - the amount of space below
#                       the image, measured in pixels
#        padding_left (optional - default is 0) - the amount of space before
#                     the image, measured in pixels
# Output: a reference to the image control created
def add_image(container, image, width=300, height=200, bg_color='white',
              padding_top=0, padding_right=0, padding_bottom=0, padding_left=0):
    canvas = tk.Canvas(container, width=width, height=height)
    canvas['background'] = bg_color
    canvas.pack(padx=(padding_left, padding_right),
                pady=(padding_top, padding_bottom))
    canvas.create_image(width / 2, height / 2, anchor=tk.CENTER, image=image)
    return canvas


# Function: change_image
# Description: Changes the image in an existing image control.
# Input: canvas - the reference to the image control that should be changed
#        image - the reference to the image already loaded into the program
#                that should be displayed in this control
#        width (optional - default is 300) - the width of the image control
#              in pixels
#        height (optional - default is 200) - the height of the image control
#               in pixels
# Output: nothing
def change_image(canvas, image, width=300, height=200):
    canvas.delete('all')
    canvas.config(width=width, height=height)
    canvas.create_image(width / 2, height / 2, anchor=tk.CENTER, image=image)


# Function: add_button
# Description: Adds a button control to a container, such as a window or a
#              frame. To program the button's click event, set the button's
#              'command' option equal to (1) the name of a function that has
#              no parameters, (2) lambda: followed by a single function call,
#              or (3) lambda: followed by a list of function calls in square
#              brackets and separated by commas. Examples (assuming a reference
#              to a button named btn_submit):
#                  btn_submit['command'] = btn_submit_clicked
#                  btn_submit['command'] = lambda: ECGUI.change_image(
#                                          img_control, image2, 320, 240)
#                  btn_submit['command'] = lambda: [ECGUI.change_image(
#                                          img_control, image2, 320, 240),
#                                          ECGUI.change_label(lbl_heading,
#                                          'Second Image')]
# Input: container - the window or frame that will hold this button control
#        message (optional - default is '') - what the button should say
#        padding_top (optional - default is 0) - the amount of space above the
#                    button, measured in pixels
#        padding_right (optional - default is 0) - the amount of space after
#                      the button, measured in pixels
#        padding_bottom (optional - default is 0) - the amount of space below
#                       the button, measured in pixels
#        padding_left (optional - default is 0) - the amount of space before
#                     the button, measured in pixels
#        side (optional - default is '') - determines if this control should
#             be placed in its own row in the container or if it should be
#             moved to the 'left' or 'right' to make room for other controls
#             in the same row
# Output: a reference to the button control created
def add_button(container, message='', padding_top=0, padding_right=0,
               padding_bottom=0, padding_left=0, side=''):
    button = tk.Button(container, text=message)
    if side == 'left' or side == 'right':
        button.pack(padx=(padding_left, padding_right),
                    pady=(padding_top, padding_bottom), side=side)
    else:
        button.pack(padx=(padding_left, padding_right),
                    pady=(padding_top, padding_bottom))
    return button


# Function: add_entry_box
# Description: Adds an entry box control to a container, such as a window or
#              a frame.
# Input: container - the window or frame that will hold this entry box
#        message (optional - default is '') - what the entry box should say
#                 to start with
#        padding_top (optional - default is 0) - the amount of space above
#                    the entry box, measured in pixels
#        padding_right (optional - default is 0) - the amount of space after
#                      the entry box, measured in pixels
#        padding_bottom (optional - default is 0) - the amount of space below
#                       the entry box, measured in pixels
#        padding_left (optional - default is 0) - the amount of space before
#                     the entry box, measured in pixels
#        side (optional - default is '') - determines if this control should
#             be placed in its own row in the container or if it should be
#             moved to the 'left' or 'right' to make room for other controls
#             in the same row
# Output: a reference to the entry box created
def add_entry_box(container, width=10, padding_top=0, padding_right=0,
                  padding_bottom=0, padding_left=0, side=''):
    entry_box = tk.Entry(container, width=width)
    if side == 'left' or side == 'right':
        entry_box.pack(padx=(padding_left, padding_right),
                       pady=(padding_top, padding_bottom), side=side)
    else:
        entry_box.pack(padx=(padding_left, padding_right),
                       pady=(padding_top, padding_bottom))
    return entry_box


# Function: clear_entry_box
# Description: Clears the text from an existing entry box control.
# Input: entry_box - the entry box to clear
# Output: nothing
def clear_entry_box(entry_box):
    entry_box.delete(0, tk.END)


# Function: fill_entry_box
# Description: Clears the text from an existing entry box control and then
#              fills it with the value provided.
# Input: entry_box - the entry box to fill
#        value - the value to use to fill the entry box
# Output: nothing
def fill_entry_box(entry_box, value):
    entry_box.delete(0, tk.END)
    entry_box.insert(0, value)


# Function: add_radio_buttons
# Description: Adds a series of connected radio buttons to the given container.
#              If a button_message is provided, a button is added to program a
#              selection event. If no button_message is provided, no button is
#              added, allowing for each radio button click event to be
#              programmed separately.
# Input: container - the window or frame that will hold the radio button series
#                    and optional button
#        names - a list of strings used to label the radio buttons, contained
#                within square brackets and separated by a comma
#        selected (optional - default is 0) - the zero-based index of the radio
#                 button that should be selected at start up
#        horizontal (optional - default is False) - a Boolean (True or False)
#                   that adds the buttons horizontally across the container or
#                   vertically in the container
#        button_message (optional - default is '') - determines if a button is
#                       to be added at the end of the radio buttons and if so,
#                       what the text in the button should be, with a blank
#                       button_message indicating that no button should be added
#        spacing (optional - default is 5) - the amount of padding around each
#                radio button and optional button
# Output: a reference to the button if one is added or a reference to the list
#         of radio buttons and, in either case, the zero-based index of the
#         currently selected radio button as an IntVar. To get the integer value
#         out of this, use the get() method. Example:
#                btn_go, choice = ECGUI.add_radio_buttons(my_frame,
#                                 ['one', 'two', 'three'], button_message='GO')
#                btn_go['command'] = lambda: change_image(img_top,
#                                                         images[choice.get()])
def add_radio_buttons(container, names, selected=0, horizontal=False,
                      button_message='', spacing=5):
    rb_choice = tk.IntVar()
    rb_list = []
    for index in range(0, len(names)):
        rb_list.append(tk.Radiobutton(container, text=names[index],
                                      variable=rb_choice, value=index))
        if horizontal:
            rb_list[index].pack(padx=5, pady=5, side='left')
        else:
            rb_list[index].pack(padx=5, pady=5)
    rb_choice.set(selected)
    if button_message != '':
        button = tk.Button(container, text=button_message)
        if horizontal:
            button.pack(padx=spacing, pady=spacing, side='left')
        else:
            button.pack(padx=spacing, pady=spacing)
        return button, rb_choice
    else:
        return rb_list, rb_choice


# Function: select_radio_button
# Description:
# Input: rb_choice - the IntVar returned when adding radio buttons, which
#                    provides the zero-based index of the currently selected
#                    radio button
#        selected (optional - default is 0) - the zero-based index of the radio
#                 button that should be selected at this time
# Output: nothing
def select_radio_button(rb_choice, selected=0):
    rb_choice.set(selected)


# Function: add_check_box
# Description: Adds a check box control to a container, such as a window or
#              a frame.
# Input: container - the window or frame that will hold this button control
#        name - the text to associate with this check box
#        padding_top (optional - default is 0) - the amount of space above the
#                    check box, measured in pixels
#        padding_right (optional - default is 0) - the amount of space after
#                      the check box, measured in pixels
#        padding_bottom (optional - default is 0) - the amount of space below
#                       the check box, measured in pixels
#        padding_left (optional - default is 0) - the amount of space before
#                     the check box, measured in pixels
#        side (optional - default is '') - determines if this control should be
#             placed in its own row in the container or if it should be moved
#             to the 'left' or 'right' to make room for other controls in the
#             same row
# Output: a reference to the check box control created
def add_check_box(container, name, padding_top=0, padding_right=0,
                  padding_bottom=0, padding_left=0, side=''):
    cb_choice = tk.IntVar()
    cb = tk.Checkbutton(container, text=name, variable=cb_choice)
    if side == 'left' or side == 'right':
        cb.pack(padx=(padding_left, padding_right),
                pady=(padding_top, padding_bottom), side=side)
    else:
        cb.pack(padx=(padding_left, padding_right),
                pady=(padding_top, padding_bottom))
    return cb_choice


# Function: add_check_boxes
# Description: Adds a series of check boxes to the given container.
# Input: container - the window or frame that will hold the check box series
#        names - a list of strings used to label the check boxes, contained
#                within square brackets and separated by a comma
#        horizontal (optional - default is False) - a Boolean (True or False)
#                   that adds the check boxes horizontally across the container
#                   or vertically in the container
#        spacing (optional - default is 5) - the amount of padding around
#                each check box
# Output: a reference to the list of IntVal objects with values of 1 or 0,
#         indicating which check boxes are currently checked. These values can
#         be used as Booleans. To get the value out an IntVal, use the get()
#         method. Example:
#                selections = ECGUI.add_check_boxes(cb_frame,
#                             ['bold', 'italics'], True)
#                bold_setting = selections[0].get()
def add_check_boxes(container, names, horizontal=False, spacing=5):
    cb_choices = []
    for index in range(0, len(names)):
        cb_choices.append(tk.IntVar())
        cb_choices[index].set(0)
    cb_list = []
    for index in range(0, len(names)):
        cb_list.append(tk.Checkbutton(container, text=names[index],
                                      variable=cb_choices[index]))
        if horizontal:
            cb_list[index].pack(padx=spacing, pady=spacing, side='left')
        else:
            cb_list[index].pack(padx=spacing, pady=spacing)
    return cb_choices


# Function: add_dropdown
# Description: Adds a single-selection dropdown menu control to a container,
#              such as a window or a frame.
# Input: container - the window or frame that will hold this dropdown menu
#                    control
#        options - a list of strings that are the menu options, contained within
#                  square brackets and separated by a comma
#        selected (optional - default is none) - the string option that should
#                 be selected by default
#        padding_top (optional - default is 0) - the amount of space above the
#                    dropdown, measured in pixels
#        padding_right (optional - default is 0) - the amount of space after
#                      the dropdown, measured in pixels
#        padding_bottom (optional - default is 0) - the amount of space below
#                       the dropdown, measured in pixels
#        padding_left (optional - default is 0) - the amount of space before
#                     the dropdown, measured in pixels
#        side (optional - default is '') - determines if this control should be
#             placed in its own row in the container or if it should be moved
#             to the 'left' or 'right' to make room for other controls in the
#             same row
# Output: a reference to the dropdown itself and a StringVar that holds the
#         currently selected menu option. To get the string value from this,
#         use the get method.
#         Example:
#                menu, color_option = ECGUI.add_dropdown(frame,
#                                                  ['red', 'white', 'blue'],
#                                                  'white')
#                color_selected = color_option.get()
def add_dropdown(container, options, selected='', padding_top=0,
                 padding_right=0, padding_bottom=0, padding_left=0, width=10,
                 side=''):
    menu_choice = tk.StringVar()
    menu_choice.set(selected)
    menu = tk.OptionMenu(container, menu_choice, *options)
    menu.config(width=width)
    if side == 'left' or side == 'right':
        menu.pack(padx=(padding_left, padding_right),
                  pady=(padding_top, padding_bottom), side=side)
    else:
        menu.pack(padx=(padding_left, padding_right),
                  pady=(padding_top, padding_bottom))
    return menu, menu_choice


# Function: change_dropdown_list
# Description: Allows the list of options in a single-selection dropdown menu
#              control to be changed.
# Input: dropdown - a reference to the dropdown to change
#        choice - the StringVar that holds the currently selected menu option
#        options - a list of strings that are the new menu options, contained
#                  within square brackets and separated by a comma
#        selected (optional - default is none) - the string option that should
#                 be selected by default
# Output: nothing
def change_dropdown_list(dropdown, choice, options, selected=''):
    # Reset var and delete all old options
    dropdown['menu'].delete(0, 'end')
    for o in options:
        dropdown['menu'].add_command(label=choice, command=tk._setit(choice, o))
    menu = dropdown["menu"]
    menu.delete(0, "end")
    for string in options:
        menu.add_command(label=string,
                         command=lambda value=string: choice.set(value))
    choice.set(selected)


# Function: add_multiline_label
# Description: Adds a multiline label control to a container, such as a window
#              or a frame. A multiline label is a non-editable box that holds
#              multiple lines of text. Lines longer than the box width can be
#              automatically word-wrapped. Text may be appended
#              programmatically with the append_multiline_label function.
# Input: container - the window or frame that will hold this multiline label
#                    control
#        message (optional - default is '') - the text that should be placed
#                 in the box to start with. Note that this function does not
#                 add a newline character at the end of this text. To cause
#                 appended text to start on the next line, add a '\n' to the
#                 end of this message.
#        height (optional - default is 10) - the number of lines high to make
#                the box that holds the multiline label
#        width (optional - default is 25) - the number of characters across to
#               make the box that holds the multiline label
#        wrap (optional - default is True) - a Boolean (True or False) that
#              turns word wrapping on or off
#        scroll (optional - default is False) - a Boolean (True or False) that
#                makes a vertical scrollbar appear to the left of the text
#                or not, which, when applied, allows the user to scroll through
#                more text than can fit in the height of the box.
# Output: a reference to the multiline label control created
def add_multiline_label(container, message='', height=10, width=25, wrap=True,
                        scroll=False):
    frame = add_frame(container)
    if scroll:
        scroll_bar = tk.Scrollbar(frame)
        scroll_bar.pack(side='right', fill='y')
        multi_label = tk.Text(frame, height=height, width=width,
                              yscrollcommand=scroll_bar.set)
        multi_label.pack(side='left')
        scroll_bar.config(command=multi_label.yview)
    else:
        multi_label = tk.Text(frame, height=height, width=width)
        multi_label.pack()
    if wrap:
        multi_label.config(wrap='word')
    if message != '':
        multi_label.configure(state='normal')
        multi_label.insert(tk.END, message)
    multi_label.configure(state='disabled')
    return multi_label


# Function: append_multiline_label
# Description: Adds text to any text already in an existing multiline label.
#              Each append creates a new line of text with the option of
#              double spacing between lines.
# Input: multi_label - the multiline label control to append
#        message - the text to append to the multiline label
#        skip_a_line (optional - default is False) - a Boolean (True or False)
#                     that turns double spacing on or off
# Output: nothing
def append_multiline_label(multi_label, message, skip_a_line=False):
    multi_label.configure(state='normal')
    if skip_a_line:
        multi_label.insert(tk.END, message + '\n\n')
    else:
        multi_label.insert(tk.END, message + '\n')
    multi_label.configure(state='disabled')


# Function: clear_multiline_label
# Description: Deletes all text in an existing multiline label.
# Input: multi_label - the multiline label control to clear.
# Output: nothing
def clear_multiline_label(multi_label):
    multi_label.configure(state='normal')
    multi_label.delete("1.0", tk.END)
    multi_label.configure(state='disabled')


# Function: add_list_box
# Description: Adds a list box control to a container, such as a window
#              or a frame. A list box is a single-selection list of
#              options. The currently selected option is highlighted and
#              can be accessed using the get('anchor') function. Example:
#                  selection = lst_options.get['anchor']
#              The selection variable would contain the string currently
#              selected.
# Input: container - the window or frame that will hold this list box control
#        entries - a list of strings that make up the options that should
#                  go into the list box, contained within square brackets and
#                  separated by a comma
#        height (optional - default is 10) - the number of lines high to make
#                the list box
#        width (optional - default is 25) - the number of characters across to
#               make the list box
#        select_color (optional - default is 'white') - text color for selected
#                      item in the list
#        highlight (optional - default is 'black') - background color for
#                   selected item in the list
#        scroll (optional - default is False) - a Boolean (True or False) that
#                makes a vertical scrollbar appear to the left of the list
#                or not, which, when applied, allows the user to scroll through
#                more options than can fit in the height of the box.
# Output: a reference to the list box control created
def add_list_box(container, entries, height=10, width=25,
                 select_color='white', highlight='black', scroll=False):
    if scroll:
        scroll_bar = tk.Scrollbar(container)
        scroll_bar.pack(side='right', fill='y')
        list_box = tk.Listbox(container, yscrollcommand=scroll_bar.set,
                              selectforeground=select_color,
                              selectbackground=highlight, activestyle='none',
                              height=height, width=width)
        list_box.pack(side='left', fill='y')
        scroll_bar.config(command=list_box.yview)
    else:
        list_box = tk.Listbox(container, selectforeground=select_color,
                              selectbackground=highlight, activestyle='none',
                              height=height, width=width)
        list_box.pack()
    for line in entries:
        list_box.insert(tk.END, line)
    list_box.select_set(0)
    list_box.see(0)
    list_box.select_anchor(0)
    return list_box


# Function: show_message_box
# Description: Displays a popup message box with an OK button.
# Input: title - the text that will appear in the title bar of the popup window
#        message - the text that will appear in the body of the popup window
#        message_type (optional - default is 'info') - the type of message the
#                       popup window is providing. Options are 'info',
#                       'warning', or 'error'. Each option produces a different
#                       icon next to the popup message.
# Output: nothing
def show_message_box(title, message, message_type='info'):
    if message_type == 'info':
        messagebox.showinfo(title, message)
    elif message_type == 'warning':
        messagebox.showwarning(title, message)
    else:
        messagebox.showerror(title, message)
