The provided Python script automates the process of sending WhatsApp messages to a list of contacts from an Excel file, using a predefined message template from a text file. Here's an overview of the project:

Libraries Used: The script utilizes several Python libraries:

keyboard for keyboard interactions.
pyautogui for automating mouse and keyboard actions.
time for introducing delays between actions.
pandas for reading contact information from an Excel file.
webbrowser for opening a web browser.
urllib.parse for URL encoding.
Data Sources:

Contact Information: The script reads contact names and phone numbers from an Excel file (contact_file_excel).
Message Template: The message content is loaded from a text file (message_file_txt).
Message Sending Process:

The script iterates through the list of contacts, extracting the contact's name and phone number.
It then constructs a WhatsApp Web URL for each contact, including the phone number and the message content (with proper URL encoding).
The web browser is opened to the WhatsApp Web page for each contact using the generated URL.
It waits for a specified duration (60 seconds in this case) to allow time for the user to scan the QR code if required.
It simulates a mouse click at specific screen coordinates (x_cord and y_cord) to focus on the chat input area.
Another click is simulated to send the message.
The script waits for a few seconds between actions to ensure they are executed correctly.
After sending the message, it closes the chat window using a keyboard shortcut (Ctrl+W).
The script counts the number of messages sent and prints this count to the console.
File Paths:

The paths to the contact Excel file and the message text file are specified as variables (contact_path and message_path).
Output:

The script provides feedback by printing the number of messages sent and a "Done" message when the process is complete.
Overall, this script automates the task of sending personalized WhatsApp messages to a list of contacts using WhatsApp Web. However, it's essential to ensure that such automation is used responsibly and in compliance with WhatsApp's terms of service. Additionally, consider implementing error handling and potentially switching to more robust web automation libraries if the script needs to be used in a production environment.




***NOTE***
Replace the entry in contact.xlsx with correct name and number.
Correctly set the message.txt path and contact.xlsx path.