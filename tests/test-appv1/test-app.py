import customtkinter as ctk

PLACEHOLDER = "Select a generator"
ERRORPH = "Unknown generator"

GENERATORS = {
    "Beaconing": {
        "description": "Outbound connections at a regular interval (C2).",
        "example": "event=network_connect dst_port=443",
    },
    "Failed logins": {
        "description": "Repeated authentication attempts with a wrong password.",
        "example": "action=failure user=admin",
    },
    "DNS Poisoning": {
        "description": "Manipulation of DNS cache to redirect traffic to unauthorized or malicious IP addresses.",
        "example": "event=dns_query query=bank.com response=10.10.10.10 ttl=0",
    },
    "SQL Injection": {
        "description": "Insertion of malicious SQL statements into entry fields for execution or data leakage.",
        "example": "event=http_request uri='/login.php?user=admin%27%20OR%201%3D1%20--' status=200",
    },
    "Brute Force": {
        "description": "High volume of rapid authentication attempts targeting multiple accounts or variations.",
        "example": "event=auth_attempt status=failed count=150 src_ip=11.11.11.11 user=root",
    },
    "Data Exfiltration": {
        "description": "Unauthorized transfer of sensitive data from inside the network to an external destination.",
        "example": "event=file_transfer bytes_sent=4500000000 dst_ip=12.12.12.12 protocol=ftp",
    },
    "Ransomware Activity": {
        "description": "Massive and rapid modification of file extensions and headers indicating bulk encryption.",
        "example": "event=file_modify path='C:\\Users\\Shares\\document.pdf.locked' action=renamed",
    },
    "Atributo sem valor": {
        "description": "",
        "example": "",
    }
}


def on_select(name):
    info = GENERATORS.get(name, {})
    desc_text = info.get("description") or ERRORPH
    exam_text = info.get("example") or ERRORPH

    description.configure(text=desc_text)
    example.configure(text=exam_text)

def on_generate():
    name = menu.get()
    if name == PLACEHOLDER:
        status.configure(text="Pick a generator first")
        return
    status.configure(text=f"Selected: {name}")

root = ctk.CTk()
root.title("SIEM DETECTION SIMULATOR")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

menu = ctk.CTkOptionMenu(root, values=list(GENERATORS), command=on_select)
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

root.mainloop()