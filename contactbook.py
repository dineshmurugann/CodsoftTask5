import tkinter as tk
from tkinter import messagebox

class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.configure(bg="#FFD7BE")

        # Create frames
        self.frame1 = tk.Frame(self.root, bg="#FFD7BE")
        self.frame1.pack(fill="x", pady=5)

        self.frame2 = tk.Frame(self.root, bg="#FFD7BE")
        self.frame2.pack(fill="x", pady=5)

        self.frame3 = tk.Frame(self.root, bg="#FFD7BE")
        self.frame3.pack(fill="x", pady=5)

        # Create labels and entries
        self.name_label = tk.Label(self.frame1, text="Name:", bg="#FFD7BE")
        self.name_label.pack(side="left", padx=5)

        self.name_entry = tk.Entry(self.frame1, width=30)
        self.name_entry.pack(side="left", padx=5)

        self.phone_label = tk.Label(self.frame2, text="Phone:", bg="#FFD7BE")
        self.phone_label.pack(side="left", padx=5)

        self.phone_entry = tk.Entry(self.frame2, width=30)
        self.phone_entry.pack(side="left", padx=5)

        self.email_label = tk.Label(self.frame3, text="Email:", bg="#FFD7BE")
        self.email_label.pack(side="left", padx=5)

        self.email_entry = tk.Entry(self.frame3, width=30)
        self.email_entry.pack(side="left", padx=5)

        # Create buttons
        self.button_frame = tk.Frame(self.root, bg="#FFD7BE",bd=2,relief="ridge")
        self.button_frame.pack(fill="both", pady=5)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", width=12, command=self.add_contact)
        self.add_button.pack(side="top", pady=5)

        self.view_button = tk.Button(self.button_frame, text="View Contacts",width=12,command=self.view_contacts)
        self.view_button.pack(side="top", pady=5)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact",width=12, command=self.delete_contact)
        self.delete_button.pack(side="top", pady=5)

        self.edit_button = tk.Button(self.button_frame, text="Edit Contact",width=12, command=self.edit_contact)
        self.edit_button.pack(side="top", pady=5)

        # Create listbox
        self.contacts_listbox = tk.Listbox(self.root, width=40, bg="#FFD7BE")
        self.contacts_listbox.pack(fill="both", expand=True, pady=5)

        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="y", pady=5)

        # Configure listbox and scrollbar
        self.contacts_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.contacts_listbox.yview)

        # Initialize contacts list
        self.contacts = [
            {"name": "John Doe", "phone": "123-456-7890", "email": "john.doe@example.com"},
            {"name": "Jane Doe", "phone": "098-765-4321", "email": "jane.doe@example.com"},
            {"name": "Bob Smith", "phone": "555-123-4567", "email": "bob.smith@example.com"},
        ]

        # Populate listbox with initial contacts
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")
            self.contacts_listbox.insert(tk.END, "")  # add padding between each line

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        if name and phone and email:
            self.contacts.append({"name": name, "phone": phone, "email": email})
            self.contacts_listbox.insert(tk.END, f"{name} - {phone} - {email}")
            self.contacts_listbox.insert(tk.END, "")  # add padding between each line
            self.name_entry.delete(0, tk.END)
            self.phone_entry.delete(0, tk.END)
            self.email_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Please fill in all fields")

    def view_contacts(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, f"{contact['name']} - {contact['phone']} - {contact['email']}")
            self.contacts_listbox.insert(tk.END, "")  # add padding between each line

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            self.contacts.pop(selected_index[0])
            self.contacts_listbox.delete(selected_index[0])
        else:
            messagebox.showerror("Error", "Please select a contact to delete")

    def edit_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            contact = self.contacts[selected_index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, contact["name"])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, contact["phone"])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, contact["email"])
        else:
            messagebox.showerror("Error", "Please select a contact to edit")

if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.geometry("300x400")
    root.mainloop()