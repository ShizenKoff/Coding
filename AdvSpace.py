import sys
import time
import tkinter as tk
from tkinter import font

class AdventureConsole:
    def __init__(self, master):
        self.master = master
        master.title("Choose Your Own Adventure")

        # Set the default font
        self.default_font = font.Font(family="OCR A Extended", size=16)


        self.console = tk.Text(master, wrap=tk.WORD, bg='black', fg='green', insertbackground='green', height=25, width=80)
        self.console.pack()

        # Create a tag for center alignment
        self.console.tag_configure("center", justify="center")

        self.entry_label = tk.Label(master, text=">")
        self.entry_label.pack(side=tk.LEFT)

        self.entry = tk.Entry(master, fg='green', bg='black', insertbackground='green', width=50)
        self.entry.pack(side=tk.LEFT)
        self.entry.bind('<Return>', self.handle_input)

        # Initialize the adventure
        self.current_phase = 1
        self.start_adventure()

    
    def print_slow(self, text, font=None):
        if font is None:
            font = self.default_font
        
        
        for char in text:
            self.console.insert(tk.END, char, 'center')  # Center-align each character
            self.console.see(tk.END)
            self.console.update()
            time.sleep(0.05)
        self.console.insert(tk.END, '\n', 'center')  # Center-align the new line
        self.console.see(tk.END)

    def handle_input(self, _event):
        user_choice = self.entry.get().lower()
        self.entry.delete(0, tk.END)  # Clear the entry
        
         # Clear the existing text in the Text widget
        self.console.delete("1.0", tk.END)

        # Handle user choice based on the current phase of the adventure
        if self.current_phase == 1:
            self.handle_phase_1(user_choice)
            # 'Arms' or 'Cables' choice
        elif self.current_phase == 2:
            self.handle_phase_2(user_choice)
            # adv_2 is phase 2. Choices are 'Console' or 'Forward'

    def start_adventure(self):
        self.print_slow("Your head is ringing...\n"
                        "You realize you are floating, weightless...\n"
                        "What happened here...?\n"
                        "You shake your head and try to gain your bearings...\n"
                        "As you look around, you see some cables...\n"
                        "You could reach for the 'cables', or you could try and spin your 'arms' as a gyro to move...\n"
                        "What do you choose?")

    def handle_phase_1(self, user_choice):
        if user_choice == 'arms':
            self.print_slow("You start to spin your arms, but as you do, you begin to spin too fast and black out from the forces")
            self.start_adventure()
        elif user_choice == 'cables':
            self.print_slow("Your shoulder screams in pain, but you are able to grab onto the cables...")
            self.current_phase = 2  # Move to the next phase
            self.adv_2()

    def adv_2(self):
        self.print_slow("You start to pull yourself down the cables, the power keeps flickering on and off...\n"
                        "You notice a console across the corridor...\n"
                        "You could try and float across to the 'console' to find out what happened here, or you can continue 'forward'...?\n"
                        "What do you choose...?")

    def handle_phase_2(self, user_choice):
        if user_choice == 'console':
            self.print_slow("You steady yourself against the wall...\n"
                            "You aim towards the console and take a deep breath...\n"
                            "You push off and start across, but just then, a micro meteor strikes the hull...")
            self.adv_2A()  # Move to the first alternate branch of Phase 2
            
            
        elif user_choice == 'forward':
            self.print_slow("You continue forward down the cables, but the cables come to an end, about 15 meters short of the doors to the hydroponics bay...\n"
                            "You could 'jump' across to the hydroponics bay, or take a 'breather' and reassess the situation...\n"
                            "What do you choose...")



    def adv_2A(self):
        self.print_slow("Suddenly all the air in the corridor starts rushing towards the strike...\n"
                        "You feel helpess for a moment, but your suit snags on a pipe...\n"
                        "You gotta think quick, you remember your suit has ballistic plates...\n"
                        "You could use one of the 'plates' to try and plug the hole, or you could try and free yourself and shoot to a 'hatch' if you time it right...\n"
                        "What do you choose...")

# Create the main Tkinter window and start the adventure
root = tk.Tk()
adventure_console = AdventureConsole(root)
root.mainloop()
