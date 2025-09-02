from tkinter import *                   # a library in creating a python app/ui
from tkinter import ttk, filedialog     # for designing the App
from bot_2 import get_response          # the bot's response function


# initialization of python ui/app
chatWindow = Tk()

quickInquiries = {
                    'A': "How to acquire a Postal ID?",
                    'B': "How to acquire a Business Permit?",
                    'C': "How to acquire a Police Clearance?",
                    'D': "How to acquire a Senior Citizen ID?",
                    'E': "How to acquire a Civil Registration?",
                    'F': "How to acquire a Cedula?"
                 } # Map/Dict for quick prompts

# a function that reads the textArea and converts it to a .txt file
def saveChatTranscript():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[
        ("Text file", ".txt"),
        ("PDF file", ".pdf")])
    fileText = str(chatArea.get(1.0,END))
    file.write(fileText)
    file.close()

def warn_clearChat():
    chatArea.configure(state=NORMAL)
    chatArea.insert(END, "[System]: Clearing... Please wait")
    chatArea.after(2000, clearChat)
    
def clearChat():
    chatArea.delete('1.0', END)
    chatArea.after(1000, headerChat)
    
def headerChat():
    str_header = "[BeA]: Hi there! I'm BeA your virtual assistant.\n\n"
    chatArea.insert(END, str_header)
    chatArea.configure(state=DISABLED)

# creating a tab
manageDisplay = ttk.Notebook(chatWindow)
mainTab = Frame(manageDisplay)
sideTab = Frame(mainTab)

mainTab_menubar = Menu(mainTab)
fileMenu = Menu(mainTab_menubar,tearoff=0)
mainTab_menubar.add_cascade(label='Chat Option', menu=fileMenu)
fileMenu.add_command(label='Clear chat', command=warn_clearChat)
fileMenu.add_command(label='Export chat transcript',command=saveChatTranscript)
fileMenu.add_separator()
fileMenu.add_command(label='Exit chat', command=quit)

mainTab.configure(width=610,
                  height=550,
                  bg='gray')



sideTab.configure(width=500, height=500, bg='dimgray')
sideTab.place(relwidth = .22, relheight=.89, relx=.765, rely=.01)

manageDisplay.add(mainTab,
                  text="BeA: Bacoor e-Assistant",
                  underline=True,
                  padding=2)

manageDisplay.pack(expand=True, fill="both")

# the widget displaying the chat
chatWindow.configure(width=610,
                     height=550,
                     bg='white',
                     menu = mainTab_menubar)
chatWindow.resizable(width=FALSE,
                 height=FALSE)

chatArea = Text(mainTab,
                bg = "white",
                fg = "black",
                font = ("Segoe UI", 12),
                padx = 8,
                pady = 8,
                wrap = WORD)
scrollbar = Scrollbar(mainTab, orient="vertical", command=chatArea.yview)
chatArea.configure(cursor = 'arrow',
                   state = DISABLED,
                   yscrollcommand=scrollbar.set)
scrollbar.place(relheight=.89, relwidth=.01, relx=.755, rely=.01)
chatArea.place(relheight=.89, relwidth=.745, relx=.01, rely=.01)


def _enter_postal(event):
    str_postal = quickInquiries["A"]
    _insert_str_msg(str_postal, "You")
    
def _enter_police_clearance(event):
    str_police = quickInquiries["C"]
    _insert_str_msg(str_police, "You")

def _enter_senior_id(event):
    str_senior = quickInquiries["D"]
    _insert_str_msg(str_senior, "You")
    
def _enter_business_perm(event):
    str_business = quickInquiries["B"]
    _insert_str_msg(str_business, "You")

def _enter_civil_reg(event):
    str_civreg = quickInquiries["E"]
    _insert_str_msg(str_civreg, "You")
    
def _enter_cedula(event):
    str_cedula = quickInquiries["F"]
    _insert_str_msg(str_cedula, "You")
    
postalButton = Button(sideTab,
                     text="Postal ID",
                     width=90,
                     command=lambda: _enter_postal(None))
postalButton.place(relwidth=.80, relx=.10, rely=.04, relheight=.1)

policeButton = Button(sideTab,
                     text="Police \nClearance",
                     width=90,
                     command=lambda: _enter_police_clearance(None))
policeButton.place(relwidth=.80, relx=.10, rely=.16, relheight=.1)

seniorButton = Button(sideTab,
                     text="Senior\nCitizen ID",
                     width=90,
                     command=lambda: _enter_senior_id(None))
seniorButton.place(relwidth=.80, relx=.10, rely=.28, relheight=.1)

businessButton = Button(sideTab,
                     text="Business\nPermit",
                     width=90,
                     command=lambda: _enter_business_perm(None))
businessButton.place(relwidth=.80, relx=.10, rely=.40, relheight=.1)

civregButton = Button(sideTab,
                     text="Civil\nRegistration",
                     width=90,
                     command=lambda: _enter_civil_reg(None))
civregButton.place(relwidth=.80, relx=.10, rely=.52, relheight=.1)

cedulaButton = Button(sideTab,
                     text="Cedula",
                     width=90,
                     command=lambda: _enter_cedula(None))
cedulaButton.place(relwidth=.80, relx=.10, rely=.64, relheight=.1)

# the textbox for entering a query
str_entry = Entry(mainTab,
                bg = "white",
                fg = "black",
                font = ("Segoe UI", 11))
str_entry.place(relheight = .07, 
                relwidth = .745, 
                relx = .01,
                rely = .915)
str_entry.focus()

def _enter_func(event):
    str_msg = str_entry.get()
    _insert_str_msg(str_msg, "You")
    

# when enter key is pressed, it calls the _enter_func
str_entry.bind("<Return>", _enter_func)

# a button calling an anonymous function lambda directly to _enter_func function
submit_button = Button(mainTab,
                       text = "Send",
                       font = 'bold',
                       fg='white',
                       width = 20,
                       bg = "gray", command = lambda: _enter_func(None),
                       activebackground='white',
                       activeforeground='black')

# positioning of the button
submit_button.place(relx = .765, 
                    relheight = .07, 
                    relwidth = .22,
                    rely = .915)

    
# get the user argument and feed it in this function
def BeA_response(str_msg):
    resp = get_response(str_msg)
    # Normalize whitespace: collapse excessive spaces after newlines
    try:
        # Remove common left-indentation produced by embedded spaces
        lines = [line.lstrip() for line in str(resp).splitlines()]
        return "\n".join(lines)
    except Exception:
        return resp


    
# a function that handles the responses and display it in mainTab
def _insert_str_msg(str_msg, sender):
    if not str_msg:
        return
    
    # user 
    str_entry.delete(0, END)
    str_msg_1 = f"[{sender}]: {str_msg} \n\n"
    chatArea.configure(state=NORMAL)
    chatArea.insert(END, str_msg_1)
    chatArea.configure(state=DISABLED)
    
    str_entry.delete(0, END)
    chatArea.configure(state=NORMAL)
    str_msg_2 = f"[BeA]: {BeA_response(str_msg)} \n\n" # calling the function with an argument inside the parameter
    chatArea.insert(END, str_msg_2)
    chatArea.yview(END)
    chatArea.configure(state=DISABLED)

# BeA intro
chatArea.configure(state = NORMAL)
headerChat()

# to run the App
window = mainloop()