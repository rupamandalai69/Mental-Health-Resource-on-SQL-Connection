# Mental Health Resource Finder 🧠

## Full Python + SQL Menu-Based GUI Project

This project is a complete Python desktop application using:

* Python
* Tkinter GUI
* SQLite Database
* Menu-Based System
* Buttons & Colorful UI
* Search by Location
* Emergency Helpline Finder
* Add New Resources
* Delete Resources
* Exception Handling
* OOPS Concepts

---

# 📁 Project Structure

Create a folder:

```text
MentalHealthFinder/
│
├── main.py
├── database.py
├── resources.db
├── sample_data.sql
└── README.txt
```

---

# 🛠 STEP 1: Install Python

Download Python from:

```text
https://www.python.org/downloads/
```

While installing:

✅ Tick "Add Python to PATH"

---

# 🛠 STEP 2: Install VS Code

Download:

```text
https://code.visualstudio.com/
```

Install Python Extension.

---

# 🛠 STEP 3: Create Project Folder

Create:

```text
MentalHealthFinder
```

Inside it create:

```text
main.py
```

and

```text
database.py
```

---

# 🛠 STEP 4: SQL DATABASE CODE

Create file:

```text
sample_data.sql
```

Paste this:

```sql
CREATE TABLE IF NOT EXISTS resources (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city TEXT NOT NULL,
    organization TEXT NOT NULL,
    helpline TEXT NOT NULL,
    website TEXT,
    address TEXT
);

INSERT INTO resources (city, organization, helpline, website, address)
VALUES
('Kolkata', 'Mind Care Center', '1800-111-222', 'www.mindcare.org', 'Salt Lake, Kolkata'),
('Delhi', 'Hope Mental Clinic', '1800-333-444', 'www.hopeclinic.org', 'Connaught Place, Delhi'),
('Mumbai', 'Mental Wellness Foundation', '1800-555-666', 'www.wellness.org', 'Andheri, Mumbai'),
('Bangalore', 'Peace Mind Hospital', '1800-777-888', 'www.peacemind.org', 'MG Road, Bangalore'),
('Chennai', 'Care & Cure Mental Health', '1800-999-000', 'www.carecure.org', 'T Nagar, Chennai');
```

---

# 🛠 STEP 5: DATABASE PYTHON FILE

Create:

```text
database.py
```

Paste full code:

```python
import sqlite3


class Database:

    def __init__(self):
        self.conn = sqlite3.connect("resources.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            organization TEXT,
            helpline TEXT,
            website TEXT,
            address TEXT
        )
        ''')

        self.conn.commit()

    # Insert Resource
    def insert_resource(self, city, organization, helpline, website, address):

        self.cursor.execute('''
        INSERT INTO resources(city, organization, helpline, website, address)
        VALUES (?, ?, ?, ?, ?)
        ''', (city, organization, helpline, website, address))

        self.conn.commit()

    # Search by city
    def search_resource(self, city):

        self.cursor.execute('''
        SELECT * FROM resources WHERE city=?
        ''', (city,))

        return self.cursor.fetchall()

    # View all
    def view_all(self):

        self.cursor.execute('''
        SELECT * FROM resources
        ''')

        return self.cursor.fetchall()

    # Delete Resource
    def delete_resource(self, resource_id):

        self.cursor.execute('''
        DELETE FROM resources WHERE id=?
        ''', (resource_id,))

        self.conn.commit()

    def close_connection(self):
        self.conn.close()
```

---

# 🛠 STEP 6: MAIN GUI PROJECT CODE

Create:

```text
main.py
```

Paste FULL code:

```python
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from database import Database


# Database Object
obj = Database()


# MAIN WINDOW
root = Tk()
root.title("Mental Health Resource Finder")
root.geometry("1100x650")
root.config(bg="#0f172a")


# TITLE
heading = Label(
    root,
    text="🧠 Mental Health Resource Finder",
    font=("Helvetica", 26, "bold"),
    bg="#0f172a",
    fg="#38bdf8"
)
heading.pack(pady=20)


# FRAME
main_frame = Frame(root, bg="#1e293b", bd=5, relief=RIDGE)
main_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)


# ================= LEFT SIDE =================
left_frame = Frame(main_frame, bg="#1e293b")
left_frame.pack(side=LEFT, fill=Y, padx=20, pady=20)


# Labels and Entries
label_style = {
    "font": ("Arial", 13, "bold"),
    "bg": "#1e293b",
    "fg": "white"
}

entry_style = {
    "font": ("Arial", 12),
    "width": 30
}


Label(left_frame, text="City", **label_style).grid(row=0, column=0, pady=10, sticky=W)
city_entry = Entry(left_frame, **entry_style)
city_entry.grid(row=0, column=1, pady=10)


Label(left_frame, text="Organization", **label_style).grid(row=1, column=0, pady=10, sticky=W)
org_entry = Entry(left_frame, **entry_style)
org_entry.grid(row=1, column=1, pady=10)


Label(left_frame, text="Helpline", **label_style).grid(row=2, column=0, pady=10, sticky=W)
helpline_entry = Entry(left_frame, **entry_style)
helpline_entry.grid(row=2, column=1, pady=10)


Label(left_frame, text="Website", **label_style).grid(row=3, column=0, pady=10, sticky=W)
website_entry = Entry(left_frame, **entry_style)
website_entry.grid(row=3, column=1, pady=10)


Label(left_frame, text="Address", **label_style).grid(row=4, column=0, pady=10, sticky=W)
address_entry = Entry(left_frame, **entry_style)
address_entry.grid(row=4, column=1, pady=10)


# ================= FUNCTIONS =================

# Clear Fields

def clear_fields():

    city_entry.delete(0, END)
    org_entry.delete(0, END)
    helpline_entry.delete(0, END)
    website_entry.delete(0, END)
    address_entry.delete(0, END)


# Add Resource

def add_resource():

    try:

        city = city_entry.get()
        org = org_entry.get()
        helpline = helpline_entry.get()
        website = website_entry.get()
        address = address_entry.get()

        if city == "" or org == "" or helpline == "":
            messagebox.showerror("Error", "Please fill required fields")
            return

        obj.insert_resource(city, org, helpline, website, address)

        messagebox.showinfo("Success", "Resource Added Successfully")

        clear_fields()
        show_all_resources()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Show All Resources

def show_all_resources():

    resource_table.delete(*resource_table.get_children())

    data = obj.view_all()

    for row in data:
        resource_table.insert('', END, values=row)


# Search Resource

def search_resource():

    try:

        city = city_entry.get()

        if city == "":
            messagebox.showerror("Error", "Enter city name")
            return

        data = obj.search_resource(city)

        resource_table.delete(*resource_table.get_children())

        if len(data) == 0:
            messagebox.showinfo("Not Found", "No Resource Found")

        for row in data:
            resource_table.insert('', END, values=row)

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Delete Resource

def delete_resource():

    try:

        selected = resource_table.focus()

        if selected == "":
            messagebox.showerror("Error", "Select a row")
            return

        values = resource_table.item(selected, 'values')

        resource_id = values[0]

        obj.delete_resource(resource_id)

        messagebox.showinfo("Deleted", "Resource Deleted")

        show_all_resources()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ================= BUTTONS =================

button_frame = Frame(left_frame, bg="#1e293b")
button_frame.grid(row=6, columnspan=2, pady=20)


btn_style = {
    "font": ("Arial", 12, "bold"),
    "width": 15,
    "bd": 0,
    "cursor": "hand2"
}


add_btn = Button(
    button_frame,
    text="Add Resource",
    bg="#22c55e",
    fg="white",
    command=add_resource,
    **btn_style
)
add_btn.grid(row=0, column=0, padx=10, pady=10)


search_btn = Button(
    button_frame,
    text="Search",
    bg="#3b82f6",
    fg="white",
    command=search_resource,
    **btn_style
)
search_btn.grid(row=0, column=1, padx=10, pady=10)


view_btn = Button(
    button_frame,
    text="View All",
    bg="#a855f7",
    fg="white",
    command=show_all_resources,
    **btn_style
)
view_btn.grid(row=1, column=0, padx=10, pady=10)


clear_btn = Button(
    button_frame,
    text="Clear",
    bg="#f59e0b",
    fg="white",
    command=clear_fields,
    **btn_style
)
clear_btn.grid(row=1, column=1, padx=10, pady=10)


delete_btn = Button(
    button_frame,
    text="Delete",
    bg="#ef4444",
    fg="white",
    command=delete_resource,
    **btn_style
)
delete_btn.grid(row=2, column=0, padx=10, pady=10)


exit_btn = Button(
    button_frame,
    text="Exit",
    bg="#64748b",
    fg="white",
    command=root.destroy,
    **btn_style
)
exit_btn.grid(row=2, column=1, padx=10, pady=10)


# ================= RIGHT SIDE =================

right_frame = Frame(main_frame, bg="#0f172a")
right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=20, pady=20)


# TABLE
columns = ("ID", "City", "Organization", "Helpline", "Website", "Address")

resource_table = ttk.Treeview(
    right_frame,
    columns=columns,
    show='headings',
    height=20
)


for col in columns:
    resource_table.heading(col, text=col)
    resource_table.column(col, width=120)


resource_table.pack(fill=BOTH, expand=True)


# Load Existing Data
show_all_resources()


# MAIN LOOP
root.mainloop()
```

---

# 🛠 STEP 7: INSERT SAMPLE DATA

Open terminal inside project folder.

Run:

```bash
python
```

Then:

```python
from database import Database

obj = Database()

obj.insert_resource("Kolkata", "Mind Care Center", "1800-111-222", "www.mindcare.org", "Salt Lake")

obj.insert_resource("Delhi", "Hope Clinic", "1800-222-333", "www.hope.org", "New Delhi")

exit()
```

---

# 🛠 STEP 8: RUN PROJECT

Open terminal:

```bash
python main.py
```

---

# 🎨 FEATURES OF PROJECT

## ✅ GUI Design

* Dark Theme
* Colorful Buttons
* Professional Layout
* Table View
* Responsive UI

---

## ✅ Python Concepts Used

### 1. Functions

```python
add_resource()
search_resource()
delete_resource()
```

---

### 2. OOPS

```python
class Database
```

---

### 3. Exception Handling

```python
try:
except Exception as e:
```

---

### 4. SQL Database

```python
sqlite3.connect()
```

---

### 5. GUI

```python
Tkinter
```

---

# 🧠 HOW PROJECT WORKS

## Workflow:

```text
User enters city
        ↓
Python searches SQLite database
        ↓
Matching mental health resources displayed
        ↓
User can add/delete/search/view data
```

---

# 📸 PROJECT OUTPUT LOOK

```text
--------------------------------------------------
| 🧠 Mental Health Resource Finder                |
--------------------------------------------------
| City:        [__________]                       |
| Organization:[__________]                       |
| Helpline:   [__________]                        |
| Website:    [__________]                        |
| Address:    [__________]                        |
|                                                  |
| [Add] [Search] [View All] [Delete] [Exit]      |
--------------------------------------------------
|                 DATA TABLE                      |
--------------------------------------------------
```

---

# 🚀 EXTRA IMPROVEMENTS YOU CAN ADD

## Future Features

* Login System
* User Authentication
* AI Chatbot
* Google Maps API
* Email Support
* PDF Report Generation
* CSV Export
* Voice Assistant
* Emergency SOS Button

---

# 🎓 Viva Questions & Answers

## Q1. Why SQLite?

SQLite is lightweight, easy to use, and does not require server installation.

---

## Q2. Why Tkinter?

Tkinter is Python's built-in GUI library for desktop applications.

---

## Q3. What is Exception Handling?

Exception handling prevents program crash using try-except blocks.

---

## Q4. What is OOPS?

OOPS organizes code using classes and objects.

---

# 🏆 FINAL RESULT

You now have:

✅ SQL Integrated Project
✅ GUI Desktop App
✅ Menu-Based System
✅ Search Functionality
✅ Database Storage
✅ Colorful Professional UI
✅ Exception Handling
✅ OOPS Concepts
✅ Full Working Project

---

# ▶️ FINAL COMMAND TO RUN

```bash
python main.py
```

---

# 🌟 ADVANCED STREAMLIT VERSION (MODERN UI)

This version gives:

✅ Modern Professional Design
✅ Sidebar Menu
✅ Better Colors
✅ Search System
✅ MySQL Database Connection
✅ Responsive Layout
✅ Beautiful Tables
✅ Easy Navigation

---

# 📁 NEW PROJECT STRUCTURE

```text
MentalHealthFinder/
│
├── app.py
├── db.py
├── requirements.txt
```

---

# 🛠 INSTALL REQUIRED PACKAGES

Open terminal:

```bash
pip install streamlit mysql-connector-python pandas
```

---

# 🛠 CREATE requirements.txt

```text
streamlit
mysql-connector-python
pandas
```

---

# 🛠 CREATE db.py

Save file as:

```text
db.py
```

Paste this code:

```python
import mysql.connector


class Database:

    def __init__(self):

        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="mental_health_resources_db"
        )

        self.cursor = self.conn.cursor()


    # VIEW ALL
    def view_resources(self):

        query = "SELECT * FROM mental_health_resources"

        self.cursor.execute(query)

        return self.cursor.fetchall()


    # INSERT
    def insert_resource(self, city, organization,
                        helpline, website, address):

        query = """
        INSERT INTO mental_health_resources
        (city, organization_name,
        helpline_number, website, address)
        VALUES (%s,%s,%s,%s,%s)
        """

        values = (
            city,
            organization,
            helpline,
            website,
            address
        )

        self.cursor.execute(query, values)

        self.conn.commit()


    # SEARCH
    def search_resource(self, city):

        query = """
        SELECT * FROM mental_health_resources
        WHERE city=%s
        """

        self.cursor.execute(query, (city,))

        return self.cursor.fetchall()


    # DELETE
    def delete_resource(self, resource_id):

        query = """
        DELETE FROM mental_health_resources
        WHERE resource_id=%s
        """

        self.cursor.execute(query, (resource_id,))

        self.conn.commit()
```

---

# 🛠 CREATE app.py

Save file as:

```text
app.py
```

Paste FULL CODE:

```python
import streamlit as st
import pandas as pd

from db import Database


# DATABASE
obj = Database()


# PAGE CONFIG
st.set_page_config(
    page_title="Mental Health Resource Finder",
    page_icon="🧠",
    layout="wide"
)


# CUSTOM CSS
st.markdown(
    """
    <style>

    .main {
        background-color: #0f172a;
    }

    h1 {
        color: #38bdf8;
        text-align: center;
        font-size: 45px;
    }

    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 18px;
        font-weight: bold;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# TITLE
st.markdown(
    """
    <h1>🧠 Mental Health Resource Finder</h1>
    """,
    unsafe_allow_html=True
)


# SIDEBAR MENU
menu = st.sidebar.selectbox(
    "Select Menu",
    (
        "Home",
        "Add Resource",
        "Search Resource",
        "View Resources",
        "Delete Resource"
    )
)


# HOME
if menu == "Home":

    st.image(
        "https://cdn-icons-png.flaticon.com/512/2966/2966486.png",
        width=200
    )

    st.success("Welcome to Mental Health Resource Finder")

    st.write("""
    ### Features

    - Search Mental Health Centers
    - Add New Resources
    - Delete Resources
    - View All Data
    - MySQL Database Integration
    - Modern UI Design
    """)


# ADD RESOURCE
elif menu == "Add Resource":

    st.subheader("➕ Add New Resource")

    col1, col2 = st.columns(2)

    with col1:
        city = st.text_input("City")
        organization = st.text_input("Organization")
        helpline = st.text_input("Helpline Number")

    with col2:
        website = st.text_input("Website")
        address = st.text_area("Address")


    if st.button("Add Resource"):

        if city == "" or organization == "":

            st.error("Please fill required fields")

        else:

            obj.insert_resource(
                city,
                organization,
                helpline,
                website,
                address
            )

            st.success("Resource Added Successfully")


# SEARCH RESOURCE
elif menu == "Search Resource":

    st.subheader("🔍 Search Resource")

    city = st.text_input("Enter City Name")

    if st.button("Search"):

        data = obj.search_resource(city)

        if len(data) == 0:

            st.warning("No Resource Found")

        else:

            df = pd.DataFrame(
                data,
                columns=[
                    "ID",
                    "City",
                    "Organization",
                    "Helpline",
                    "Website",
                    "Address"
                ]
            )

            st.dataframe(df, use_container_width=True)


# VIEW ALL
elif menu == "View Resources":

    st.subheader("📋 All Resources")

    data = obj.view_resources()

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "City",
            "Organization",
            "Helpline",
            "Website",
            "Address"
        ]
    )

    st.dataframe(df, use_container_width=True)


# DELETE
elif menu == "Delete Resource":

    st.subheader("🗑 Delete Resource")

    resource_id = st.number_input(
        "Enter Resource ID",
        min_value=1,
        step=1
    )

    if st.button("Delete"):

        obj.delete_resource(resource_id)

        st.success("Resource Deleted Successfully")


