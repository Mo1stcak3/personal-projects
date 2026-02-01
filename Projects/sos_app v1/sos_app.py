import customtkinter as ctk
from services import Services

#GUI CLASS

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        #CREATION OF THE GUI
        
        self.title("SOS APP") #Set window title
        self.geometry("1440x900") #Set window resolution
        ctk.set_appearance_mode("light") #Set Theme
        font = ctk.CTkFont(family="Helvetica", size=20) #Set Font and Font size
        self.textbox = ctk.CTkTextbox(self, width=1280, height=768, font = font) #Creation of the Textbox (resolution, font)
        self.textbox.pack(pady=20) #Spacing for the textbox (Margin)
        
        self.button = ctk.CTkButton(self, text="Find Nearby Services", command=self.output) #Button "Find Nearby Services"
        self.button.pack(pady =20) #Spacing for button (Margin)
    
    def output(self):
        
        #OUTPUT PROCESS
        
        s = Services() #Imported from services.py
        
        self.textbox.delete("1.0", "end") #Clearing the textbox before new output
        
        loc = s.get_location() #This is imported from the services.py and this is used to get the User's Location
        
        self.textbox._textbox.tag_configure("bold", font=("Arial", 24, "bold")) #To make a specific text bold using tag_configure()
        
        self.textbox.insert("end", "CALL 911 IF YOU ARE IN DANGER/NEED OF HELP ASAP\n\n") #This is like print() but for ctk
        
        #Print Process of output using textbox.insert() to print in the textbox
        
        self.textbox.insert("end", "Nearby Hospitals:\n\n\n") 
        for p in s.get_places(location=loc, place_type="hospital"):
            self.textbox.insert("end",f"{p['name']} - {p.get('vicinity')}\n\n")
            
        self.textbox.insert("end", "\nNearby Police Stations:\n\n\n")
        for p in s.get_places(location=loc, place_type="police"):
            self.textbox.insert("end", f"{p['name']} - {p.get('vicinity')}\n\n")
 
        self.textbox.insert("end", "\nNearby Fire Stations:\n\n\n")
        for p in s.text_search("fire station nearby"):
            self.textbox.insert("end",f"{p['name']} - {p.get('formatted_address')}\n\n")
          
        #This is used to make the first line BOLD
            
        self.textbox._textbox.tag_add("bold", "1.0", "1.end")
        
        
            
#CHECKER 

if __name__ == "__main__":
    app = App()
    app.mainloop()