import customtkinter
from database import ClientDB
from calculator import Calculator


class AdminApp:

    def __init__(self):

        customtkinter.set_appearance_mode("dark")

        self.root = customtkinter.CTk()
        self.root.title("Sistema Administrativo")
        self.root.geometry("600x700")
        self.db = ClientDB()
        self.calc = Calculator()
        self.setup_ui()
        self.load_clients()

    def setup_ui(self):
        titulo = customtkinter.CTkLabel(
            self.root,
            text="GESTION DE CLIENTES",
            font=("Arial", 24, "bold"))
        
        titulo.pack(pady=20)
        frame = customtkinter.CTkFrame(self.root)
        frame.pack(pady=10, padx=20, fill="x")
        self.entry_nombre = customtkinter.CTkEntry(frame,placeholder_text="Nombre")
        self.entry_nombre.pack(pady=5, padx=10)
        self.entry_email = customtkinter.CTkEntry(frame,placeholder_text="Email")
        self.entry_email.pack(pady=5, padx=10)
        self.entry_tel = customtkinter.CTkEntry(frame,placeholder_text="Telefono")
        self.entry_tel.pack(pady=5, padx=10)

        boton = customtkinter.CTkButton(frame,text="Registrar Cliente",command=self.add_client)
        boton.pack(pady=10)
        self.scroll = customtkinter.CTkScrollableFrame(self.root, height=200)
        self.scroll.pack(padx=20, pady=10, fill="both", expand=False)

        titulo2 = customtkinter.CTkLabel(self.root,text="CALCULADORA ADMINISTRATIVA",font=("Arial", 20, "bold"))
        titulo2.pack(pady=10)

        frame_calc = customtkinter.CTkFrame(self.root)
        frame_calc.pack(pady=10)

        self.entry_costo = customtkinter.CTkEntry(frame_calc,placeholder_text="Costo del servicio")
        self.entry_costo.pack(pady=5)

        self.entry_imp = customtkinter.CTkEntry(frame_calc,placeholder_text="Impuesto (%)")
        self.entry_imp.pack(pady=5)

        boton_calc = customtkinter.CTkButton(frame_calc,text="Calcular Total",command=self.calcular)
        boton_calc.pack(pady=10)

        self.label_total = customtkinter.CTkLabel(frame_calc,text="Total: ")
        self.label_total.pack()

    def add_client(self):
        nombre = self.entry_nombre.get().strip()
        email = self.entry_email.get().strip()
        telefono = self.entry_tel.get().strip()
        if nombre == "":
            return

        self.db.add_client(nombre, email, telefono)

        self.entry_nombre.delete(0, "end")
        self.entry_email.delete(0, "end")
        self.entry_tel.delete(0, "end")
        self.load_clients()

    def load_clients(self):

        for widget in self.scroll.winfo_children():
            widget.destroy()

        clientes = self.db.get_all()

        for cliente in clientes:
            self.create_client_item(cliente)

    def create_client_item(self, cliente):

        client_id, nombre, email, telefono, fecha = cliente

        frame = customtkinter.CTkFrame(self.scroll)
        frame.pack(fill="x", pady=5, padx=5)

        label = customtkinter.CTkLabel(frame,text=f"{nombre} | {telefono}")
        label.pack(side="left", padx=10)

        boton = customtkinter.CTkButton(
            frame,text="Eliminar",fg_color="red",width=80,
            command=lambda: self.delete_client(client_id))
        boton.pack(side="right", padx=5)

    def delete_client(self, client_id):
        self.db.delete_client(client_id)
        self.load_clients()

    def calcular(self):
        try:
            costo = float(self.entry_costo.get())
            impuesto = float(self.entry_imp.get())
            total = self.calc.calcular_total(costo, impuesto)
            self.label_total.configure(text=f"Total: {total}")
        except:
            self.label_total.configure(text="Error en datos")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AdminApp()
    app.run()