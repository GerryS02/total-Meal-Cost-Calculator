# Total Meal Coast Estimator
# Gerry 

import ECGUI
import Util

TIP_FACTOR = 18/100
TAX_FACTOR = 7/100

def main():
    my_window = ECGUI.make_window('Total Price', 'white')

    # create an entry widget for price of meal
    str_message = "Input Total price of the meal:  "
    txt_price = build_entry_widget(my_window, str_message)

    # create a button
    btn_submit = ECGUI.add_button(my_window, 'Submit', 6, 5, 4, 2)
    # create 3 labels for outputs
    lbl_price = ECGUI.add_label(my_window)
    lbl_tax = ECGUI.add_label(my_window)
    lbl_tip = ECGUI.add_label(my_window)

    btn_submit['command'] = \
        lambda: btn_submit_click(txt_price, lbl_price, lbl_tip, lbl_tax)

    my_window.mainloop()

def build_entry_widget(window, message):
    # frame is a container
    frame = ECGUI.add_frame(window, bg_color='beige', fill='x')
    # add instructional label: static
    ECGUI.add_label(frame, message, bg_color='beige', side='left',
                    padding_left=5)
    # add textbox: input
    entry = ECGUI.add_entry_box(frame, width=25, side='right', padding_right=5)
    # return the textbox
    return entry

# button submit function
def btn_submit_click(txt_price ,lbl_price, lbl_tip , lbl_tax):
    # clear previous results in labels
    ECGUI.change_label(lbl_price, "")
    ECGUI.change_label(lbl_tax, "")
    ECGUI.change_label(lbl_tip, "")

    # get inputs from textboxes
    str_price = txt_price.get()
    
    # call functions to calculate total price, tip and tax
    tax = CalcTax(str_price)
    tip = CalcTip(str_price)
    total_price = CalcTotPrice(str_price, tax, tip)

    # analyze the resulting data and put in output label
    if total_price > 0:
        # print the results
        ECGUI.change_label(lbl_price,"Total Price: $" + str(total_price))
        ECGUI.change_label(lbl_tax,"Tax: $" + str(tax))
        ECGUI.change_label(lbl_tip,"Tip: $" + str(tip))
    else:
        ECGUI.change_label(lbl_price, "Inputs must be numeric")

# function to calculate total price including tax and tip
def CalcTotPrice(string_price, st_tax, st_tip):

    # check if input is numeric
    if Util.is_numeric(string_price):
        price = float(string_price)
        tax = float(st_tax)
        tip = float(st_tip)

        total_p = price + tax + tip
        total_p = round(total_p, 2)
    else:
        total_p = 0
    return total_p

def CalcTax(string_price):
    if Util.is_numeric(string_price):
        amount = float(string_price)
        tax = amount * TAX_FACTOR
        tax = round(tax,2)
    else:
        tax = 0
    return tax

def CalcTip(string_price):
    if Util.is_numeric(string_price):
        amount = float(string_price)

        tip = amount * TIP_FACTOR
        tip = round(tip,2)
    else:
        tip = 0
    return tip

main()

