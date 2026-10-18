import customtkinter as ctk

PLACEHOLDER = "Select a generator"

GENERATORS = {
    "Beaconing": {
        "description": "Outbound connections at a regular interval (C2).",
        "example": "event=network_connect dst_port=443",
    },
    "Failed logins": {
        "description": "Repeated authentication attempts with a wrong password.",
        "example": "action=failure user=admin",
    },
}

def on_select(name):
    info = GENERATORS[name]
    description.configure(text=info["description"])
    example.configure(text=info["example"])

def on_generate():
    name = menu.get()
    if name == PLACEHOLDER:
        status.configure(text="Pick a generator first")
        return
    status.configure(text=f"Selected: {name}")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("SIEM DETECTION SIMULATOR")

menu = ctk.CTkOptionMenu(root, values=list(GENERATORS), command=on_select)
menu.set(PLACEHOLDER)
menu.pack(pady=20)

description = ctk.CTkLabel(root, text="", wraplength=300)
description.pack(pady=5)

example = ctk.CTkLabel(root, text="", wraplength=300)
example.pack(pady=5)

button = ctk.CTkButton(root, text="Generate", command=on_generate)
button.pack(pady=10)

status = ctk.CTkLabel(root, text="")
status.pack(pady=5)

root.mainloop()