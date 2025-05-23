import pyautogui
import time
import keyboard  # Requires 'pip install keyboard'

buttons = ["button1.png", "button2.png", "button3.png", "button4.png", "button5.png", "button6.png", "button7.png"]

print("Started")

def click_any_button(timeout=10, confidence=0.9):
    """Searches for any button and clicks it as soon as it appears."""
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        if keyboard.is_pressed("q"):  # Stop the script if 'q' is pressed
            print("Stopping script.")
            return False
        
        for button in buttons:
            try:
                button_location = pyautogui.locateCenterOnScreen(button, confidence=confidence, grayscale=True)
                if button_location:
                    pyautogui.click(button_location)
                    print(f"Clicked on {button}")
                    return True  # Stop searching once a button is clicked
            except pyautogui.ImageNotFoundException:
                pass  # Ignore the error and continue

        time.sleep(1)  # Short delay before checking again

    return True  # Continue searching if timeout is reached

# Run in a loop until 'q' is pressed
while True:
    if not click_any_button():
        break  # Stop the loop when 'q' is pressed
    time.sleep(1)  # Wait before searching again

print("Script stopped.")
