from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from database import Database


# DATABASE OBJECT
db = Database()


# MAIN WINDOW
root = Tk()

root.title("Mental Health Resource Finder")

root.geometry("1250x700")

root.config(bg="#0f172a")


# ================= TITLE =================

title = Label(
    root,
    text="🧠 Mental Health Resource Finder",
    font=("Helvetica", 28, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)

title.pack(pady=20)


# ================= MAIN FRAME =================

main_frame = Frame(
    root,
    bg="#1e293b",
    bd=5,
    relief=RIDGE
)

main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)


# ================= LEFT FRAME =================

left_frame = Frame(
    main_frame,
    bg="#1e293b"
)

left_frame.pack(side=LEFT, fill=Y, padx=20, pady=20)


# LABEL STYLE
label_style = {
    "font": ("Arial", 13, "bold"),
    "bg": "#1e293b",
    "fg": "white"
}


# ENTRY STYLE
entry_style = {
    "font": ("Arial", 12),
    "width": 30
}


# CITY
Label(
    left_frame,
    text="City",
    **label_style
).grid(row=0, column=0, pady=10, sticky=W)

city_entry = Entry(
    left_frame,
    **entry_style
)

city_entry.grid(row=0, column=1, pady=10)


# ORGANIZATION
Label(
    left_frame,
    text="Organization",
    **label_style
).grid(row=1, column=0, pady=10, sticky=W)

org_entry = Entry(
    left_frame,
    **entry_style
)

org_entry.grid(row=1, column=1, pady=10)


# HELPLINE
Label(
    left_frame,
    text="Helpline",
    **label_style
).grid(row=2, column=0, pady=10, sticky=W)

helpline_entry = Entry(
    left_frame,
    **entry_style
)

helpline_entry.grid(row=2, column=1, pady=10)


# WEBSITE
Label(
    left_frame,
    text="Website",
    **label_style
).grid(row=3, column=0, pady=10, sticky=W)

website_entry = Entry(
    left_frame,
    **entry_style
)

website_entry.grid(row=3, column=1, pady=10)


# ADDRESS
Label(
    left_frame,
    text="Address",
    **label_style
).grid(row=4, column=0, pady=10, sticky=W)

address_entry = Entry(
    left_frame,
    **entry_style
)

address_entry.grid(row=4, column=1, pady=10)


# ================= FUNCTIONS =================

selected_resource_id = None


# CLEAR FIELDS
def clear_fields():

    city_entry.delete(0, END)
    org_entry.delete(0, END)
    helpline_entry.delete(0, END)
    website_entry.delete(0, END)
    address_entry.delete(0, END)


# SHOW ALL
def show_all_resources():

    resource_table.delete(*resource_table.get_children())

    data = db.view_all_resources()

    for row in data:

        resource_table.insert("", END, values=row)


# ADD RESOURCE
def add_resource():

    try:

        city = city_entry.get()
        organization = org_entry.get()
        helpline = helpline_entry.get()
        website = website_entry.get()
        address = address_entry.get()

        if city == "" or organization == "" or helpline == "":

            messagebox.showerror(
                "Error",
                "Please fill required fields"
            )

            return

        db.insert_resource(
            city,
            organization,
            helpline,
            website,
            address
        )

        messagebox.showinfo(
            "Success",
            "Resource Added Successfully"
        )

        clear_fields()

        show_all_resources()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# SEARCH RESOURCE
def search_resource():

    try:

        city = city_entry.get()

        if city == "":

            messagebox.showerror(
                "Error",
                "Enter city name"
            )

            return

        data = db.search_resource(city)

        resource_table.delete(*resource_table.get_children())

        if len(data) == 0:

            messagebox.showinfo(
                "Not Found",
                "No resources found"
            )

        for row in data:

            resource_table.insert("", END, values=row)

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# DELETE RESOURCE
def delete_resource():

    try:

        selected = resource_table.focus()

        if selected == "":

            messagebox.showerror(
                "Error",
                "Select a row"
            )

            return

        values = resource_table.item(selected, "values")

        resource_id = values[0]

        db.delete_resource(resource_id)

        messagebox.showinfo(
            "Deleted",
            "Resource Deleted Successfully"
        )

        show_all_resources()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# SELECT RECORD
def select_record(event):

    global selected_resource_id

    selected = resource_table.focus()

    values = resource_table.item(selected, "values")

    if values:

        selected_resource_id = values[0]

        clear_fields()

        city_entry.insert(0, values[1])
        org_entry.insert(0, values[2])
        helpline_entry.insert(0, values[3])
        website_entry.insert(0, values[4])
        address_entry.insert(0, values[5])


# UPDATE RESOURCE
def update_resource():

    try:

        if selected_resource_id is None:

            messagebox.showerror(
                "Error",
                "Select a row first"
            )

            return

        city = city_entry.get()
        organization = org_entry.get()
        helpline = helpline_entry.get()
        website = website_entry.get()
        address = address_entry.get()

        db.update_resource(
            city,
            organization,
            helpline,
            website,
            address,
            selected_resource_id
        )

        messagebox.showinfo(
            "Updated",
            "Resource Updated Successfully"
        )

        show_all_resources()

        clear_fields()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# ================= BUTTONS =================

button_frame = Frame(
    left_frame,
    bg="#1e293b"
)

button_frame.grid(row=6, columnspan=2, pady=20)


button_style = {
    "font": ("Arial", 12, "bold"),
    "width": 16,
    "cursor": "hand2",
    "bd": 0
}


# ADD BUTTON
add_btn = Button(
    button_frame,
    text="Add Resource",
    bg="#22c55e",
    fg="white",
    command=add_resource,
    **button_style
)

add_btn.grid(row=0, column=0, padx=10, pady=10)


# SEARCH BUTTON
search_btn = Button(
    button_frame,
    text="Search",
    bg="#3b82f6",
    fg="white",
    command=search_resource,
    **button_style
)

search_btn.grid(row=0, column=1, padx=10, pady=10)


# VIEW BUTTON
view_btn = Button(
    button_frame,
    text="View All",
    bg="#a855f7",
    fg="white",
    command=show_all_resources,
    **button_style
)

view_btn.grid(row=1, column=0, padx=10, pady=10)


# UPDATE BUTTON
update_btn = Button(
    button_frame,
    text="Update",
    bg="#14b8a6",
    fg="white",
    command=update_resource,
    **button_style
)

update_btn.grid(row=1, column=1, padx=10, pady=10)


# DELETE BUTTON
delete_btn = Button(
    button_frame,
    text="Delete",
    bg="#ef4444",
    fg="white",
    command=delete_resource,
    **button_style
)

delete_btn.grid(row=2, column=0, padx=10, pady=10)


# CLEAR BUTTON
clear_btn = Button(
    button_frame,
    text="Clear",
    bg="#f59e0b",
    fg="white",
    command=clear_fields,
    **button_style
)

clear_btn.grid(row=2, column=1, padx=10, pady=10)


# EXIT BUTTON
exit_btn = Button(
    button_frame,
    text="Exit",
    bg="#64748b",
    fg="white",
    command=root.destroy,
    **button_style
)

exit_btn.grid(row=3, column=0, columnspan=2, pady=10)


# ================= RIGHT FRAME =================

right_frame = Frame(
    main_frame,
    bg="#0f172a"
)

right_frame.pack(
    side=RIGHT,
    fill=BOTH,
    expand=True,
    padx=20,
    pady=20
)


# TABLE COLUMNS
columns = (
    "ID",
    "City",
    "Organization",
    "Helpline",
    "Website",
    "Address"
)


resource_table = ttk.Treeview(
    right_frame,
    columns=columns,
    show="headings",
    height=22
)


# HEADINGS
for col in columns:

    resource_table.heading(col, text=col)

    resource_table.column(col, width=160)


resource_table.pack(fill=BOTH, expand=True)


# CLICK EVENT
resource_table.bind(
    "<ButtonRelease-1>",
    select_record
)


# LOAD DATA
show_all_resources()


# MAIN LOOP
root.mainloop()