import customtkinter as ctk

PLACEHOLDER = "Select a generator"
ERRORPH = "Unknown generator"

def run(generators):
    def on_select(name):
        info = generators.get(name, {})
        description.configure(text=info.get("description") or ERRORPH)
        example.configure(text=info.get("example") or ERRORPH)
        status.configure(text="")

    def on_generate():
        name = menu.get()
        if name == PLACEHOLDER:
            status.configure(text="Pick a generator first")
            return
        generate = generators[name].get("generate")
        if generate is None:
            status.configure(text=f"{name}: not implemented yet")
            return
        lines = generate()
        output.delete("1.0", "end")
        output.insert("1.0", "\n".join(lines))
        status.configure(text=f"{len(lines)} lines generated")

    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.title("SIEM DETECTION SIMULATOR")

    menu = ctk.CTkOptionMenu(root, values=list(generators), command=on_select)
    menu.set(PLACEHOLDER)
    menu.pack(pady=20)

    description = ctk.CTkLabel(root, text="")
    description.pack(pady=5)

    example = ctk.CTkLabel(root, text="")
    example.pack(pady=5)

    button = ctk.CTkButton(root, text="Generate", command=on_generate)
    button.pack(pady=10)

    status = ctk.CTkLabel(root, text="")
    status.pack(pady=5)

    output = ctk.CTkTextbox(root, width=500, height=200)
    output.pack(pady=10)

    root.mainloop()