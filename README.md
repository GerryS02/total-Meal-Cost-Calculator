Meal Price Calculator
A beginner-level Python GUI program that helps users calculate the total cost of a meal by including tip and tax. This program provides a simple, user-friendly way to quickly figure out how much to pay for a meal, with the ability to enter the meal price and automatically calculate the tip (18%) and tax (7%) based on that price.

Project Overview
The Meal Price Calculator is a simple Python application built with a basic graphical user interface (GUI). The app asks for the price of the meal and then calculates the amount of tip and tax based on predefined percentages. It then displays the total price to the user, making it easy for anyone to calculate meal costs in a restaurant setting or similar situations.

The program was designed with simplicity and ease of use in mind. The user is only required to enter the meal price, and the app handles the rest, calculating the tip and tax automatically.

Key Features
User Input: Allows users to input the price of the meal.
Automatic Calculations: The program automatically calculates the tip (18%) and tax (7%) based on the input price.
Total Price Display: Displays the total price, including tip and tax.
Simple GUI: Uses a lightweight GUI framework (ECGUI) that makes it easy for anyone, even beginners, to use.
Error Handling: If a non-numeric value is entered, the program will notify the user and ask them to input a valid price.
How the Program Works
User Interface:

The user is prompted to input the price of their meal into a text field.
Upon submitting the input, the program performs the necessary calculations and displays the results in a clear and easy-to-read format.
Calculation Logic:

The program calculates the tip (18% of the meal price) and tax (7% of the meal price).
The total price is then computed as:
Total Price
=
Meal Price
+
Tax
+
Tip
Total Price=Meal Price+Tax+Tip
The calculated tip and tax are displayed along with the total amount to pay.
Example Calculation:

For a meal priced at $50:
Tip: $9.00 (18% of $50)
Tax: $3.50 (7% of $50)
Total Price: $62.50 (Meal Price + Tip + Tax)
Practical Use Cases
This project is ideal for:

Restaurant Goers: Quickly calculate the total cost of a meal, including tip and tax, without needing to manually figure it out.
Service Industry Workers: Easily determine the tip based on meal price.
Learning Projects: Perfect for beginners wanting to practice Python programming and GUI development.
By building this program, you can also get hands-on experience with user interface design and handling user input in a Python environment.

Technologies Used
Python: The main programming language used to build the application.
ECGUI: A simple Python GUI library used to create the graphical interface. (Can be swapped for more popular libraries like Tkinter, PyQt, or others if desired.)
Util: A helper module for verifying if the user's input is numeric.
GUI Design with ECGUI
ECGUI makes creating graphical interfaces in Python simple. The window contains:

Input field: For entering the price of the meal.
Submit button: To trigger the calculation.
Labels: To display the tip, tax, and total price.
The visual design is clean and easy to use, making this project suitable for a beginner-level GUI project.

Example
When the user enters a meal price of $50, the application will display:

Tip: $9.00
Tax: $3.50
Total Price: $62.50
These results help users quickly know how much they need to pay, including the suggested tip and applicable tax.

Future Enhancements
Although the program is functional as it stands, there are several ways it could be enhanced in future iterations:

Adjustable Tip and Tax Rates: Allow users to adjust the percentage for tip and tax, making the application more customizable.
More Detailed Error Handling: Improve error handling to handle edge cases like negative numbers, zero, or empty inputs.
Save/Print Receipt: Add functionality for saving or printing the calculated total as a receipt.
Improved UI: Enhance the user interface with more interactive features like sliders for selecting meal prices or tip amounts.
