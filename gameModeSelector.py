from Interface import *;

class gameModeSelector():
    def __init__(self, root):
        self.master : "Tk" = root;
        self.create_mode_selector();

    def create_mode_selector(self):
        self.master.config(background=BACKGROUND_JANELA);
        self.build_root();
        self.select_text = self.build_select_test();
        self.choose_menu = self.create_choose_menu();
        self.choose_human = self.build_choose_human();
        self.choose_machine = self.build_choose_machine();
    
        self.choose_human.bind("<Button-1>", self.on_click_choose_human);
        self.choose_human.bind("<ButtonRelease-1>", self.on_button_release_choose_human);

        self.choose_machine.bind("<Button-1>", self.on_click_choose_machine);
        self.choose_machine.bind("<ButtonRelease-1>", self.on_button_release_choose_machine);
    
        self.master.bind("<Key>", self.restart_game);
    
    def restart_game(self, event):
        if (event.keysym == "Escape"):
            self.master.destroy();
    
    def choose_human(self):
        self.master.destroy();
        root = Tk();
        objectGame = interfaceGame(root, 0);
        root.mainloop();
    
    def on_click_choose_human(self, event):
        visionImage = PhotoImage(file=PRESSED_H_IMG);
        figura = Label(self.master, image=visionImage);
        figura.image = visionImage;

        self.choose_human.config(image=visionImage);
    
    def on_button_release_choose_human(self, event):
        visionImage = PhotoImage(file=IMG_CHOOSE_HUMAN);
        figura = Label(self.master, image=visionImage);
        figura.image = visionImage;

        self.choose_human.config(image=visionImage);
           
    def choose_machine(self):
        self.master.destroy();
        root = Tk();
        objectGame = interfaceGame(root, 1);
        root.mainloop();

    def on_click_choose_machine(self, event):
        visionImage = PhotoImage(file=PRESSED_M_IMG);
        figura = Label(self.master, image=visionImage);
        figura.image = visionImage;

        self.choose_machine.config(image=visionImage);

    def on_button_release_choose_machine(self, event):
        visionImage = PhotoImage(file=IMG_CHOOSE_MACHINE);
        figura = Label(self.master, image=visionImage);
        figura.image = visionImage;

        self.choose_machine.config(image=visionImage);

    def build_root(self):
        self.master.geometry(str(WIDTH_SELECT_WINDOW) + 'x' + str(HEIGHT_SELECT_WINDOW) + "+" + str(PADX_SELECT_JANELA) + "+" + str(PADY_SELECT_JANELA));
        #self.master.attributes('-fullscreen', True);
        self.master.title("Selecione o Modo de Jogo");
        self.master.config(background=BACKGROUND_JANELA);
    
    def create_choose_menu(self):
        aux = Frame(self.master, 
                background=BACKGROUND_JANELA,
                width=WIDTH_CHOOSE_MENU,          height=HEIGHT_CHOOSE_MENU);

        aux.pack(pady=PADY_CHOOSE_MENU, 
                 padx=PADX_CHOOSE_MENU);
        return aux;

    def build_select_test(self):
        visionImage = PhotoImage(file=IMG_SELECT_TEXT);
        figura = Label(self.master, image=visionImage);
        figura.image = visionImage;

        aux = Label(self.master,
                    background=BACKGROUND_JANELA,
                    image=visionImage,
                    width=WIDTH_SELECT_TEXT,
                    height=HEIGHT_SELECT_TEXT);
        aux.pack(padx=PADX_SELECT_TEXT, 
                 pady=[PADY_TOP_SELECT_TEXT, PADY_BOTTOM_SELECT_TEXT]);
        return aux;

    def build_choose_human(self):
        visionImage = PhotoImage(file=IMG_CHOOSE_HUMAN);
        figura = Label(self.choose_menu, image=visionImage);
        figura.image = visionImage;

        aux = Button(self.choose_menu,
                    background=BACKGROUND_JANELA,
                    activebackground=BACKGROUND_JANELA,
                    image=visionImage,
                    width=WIDTH_CHOOSE_BUTTON,
                    height=HEIGHT_CHOOSE_BUTTON,
                    command=self.choose_human,
                    border=0);
        aux.pack(padx=PADX_CHOOSE_BUTTON, 
                 pady=PADY_CHOOSE_BUTTON,
                 side=LEFT);
        return aux;        

    def build_choose_machine(self):
        visionImage = PhotoImage(file=IMG_CHOOSE_MACHINE);
        figura = Label(self.choose_menu, image=visionImage);
        figura.image = visionImage;

        aux = Button(self.choose_menu,
                    activebackground=BACKGROUND_JANELA,
                    background=BACKGROUND_JANELA,
                    image=visionImage,
                    width=WIDTH_CHOOSE_BUTTON,
                    height=HEIGHT_CHOOSE_BUTTON,
                    command=self.choose_machine,
                    border=0);
        aux.pack(padx=PADX_CHOOSE_BUTTON, 
                 pady=PADY_CHOOSE_BUTTON,
                 side=RIGHT);
        return aux;        
