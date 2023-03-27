import requests
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title('SMS Sender')

# Create the API key input field
api_key_label = tk.Label(window, text='API Key:')
api_key_label.grid(row=0, column=0, padx=5, pady=5)
api_key_entry = tk.Entry(window)
api_key_entry.grid(row=0, column=1, padx=5, pady=5)

# Create the message input field
message_label = tk.Label(window, text='Message:')
message_label.grid(row=1, column=0, padx=5, pady=5)
message_entry = tk.Entry(window)
message_entry.grid(row=1, column=1, padx=5, pady=5)

# Create the phone number input field
phone_label = tk.Label(window, text='Phone Numbers:')
phone_label.grid(row=2, column=0, padx=5, pady=5)
phone_entry = tk.Text(window, height=5, width=20)
phone_entry.grid(row=2, column=1, padx=5, pady=5)

# Create the send button function
def send_sms():
    # Get the API key, message, and phone numbers from the input fields
    api_key = api_key_entry.get()
    message = message_entry.get()
    phone_numbers = phone_entry.get("1.0", tk.END).strip().split()

    # Set the URL for the API endpoint
    url = 'https://api.octopush.com/1/sms/send'

    # Loop through the phone numbers and send the SMS message to each
    for number in phone_numbers:
        # Set the payload data for each number
        data = {
            'key': api_key,
            'sms_text': message,
            'sms_recipients': '+{}'.format(number),
            'sms_type': 'FR'
        }

        # Send the HTTP POST request to the API endpoint
        response = requests.post(url, data=data)

        # Check the response status code
        if response.status_code == 200:
            print('SMS message sent successfully to', number)
        else:
            print('Failed to send SMS message to', number, '. Status code:', response.status_code)

# Create the send button
send_button = tk.Button(window, text='Send', command=send_sms)
send_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Run the main loop
window.mainloop()
