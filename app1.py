import streamlit as st
import pandas as pd
import mysql.connector


# ================= DATABASE CONNECTION =================

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mental_health_resources_db"
)

cursor = conn.cursor()


# ================= FUNCTIONS =================

# ADD RESOURCE
def add_resource(city, organization, helpline, website, address):

    query = """
    INSERT INTO mental_health_resources
    (city, organization_name, helpline_number, website, address)

    VALUES (%s,%s,%s,%s,%s)
    """

    values = (
        city,
        organization,
        helpline,
        website,
        address
    )

    cursor.execute(query, values)

    conn.commit()


# VIEW ALL RESOURCES
def view_resources():

    query = "SELECT * FROM mental_health_resources"

    cursor.execute(query)

    return cursor.fetchall()


# SEARCH RESOURCE
def search_resource(city):

    query = """
    SELECT * FROM mental_health_resources
    WHERE city=%s
    """

    cursor.execute(query, (city,))

    return cursor.fetchall()


# DELETE RESOURCE
def delete_resource(resource_id):

    query = """
    DELETE FROM mental_health_resources
    WHERE resource_id=%s
    """

    cursor.execute(query, (resource_id,))

    conn.commit()


# ================= PAGE CONFIG =================

st.set_page_config(
    page_title="Mental Health Resource Finder",
    page_icon="🧠",
    layout="wide"
)


# ================= CUSTOM CSS =================

st.markdown("""
<style>

/* MAIN BACKGROUND */
.stApp {

    background: linear-gradient(
        135deg,
        #0f172a,
        #1d4ed8,
        #7c3aed
    );

    color: white;
}


/* SIDEBAR */
[data-testid="stSidebar"] {

    background: linear-gradient(
        180deg,
        #111827,
        #1e3a8a,
        #312e81
    );
}


/* SIDEBAR TEXT */
[data-testid="stSidebar"] * {

    color: white !important;

    font-size: 18px !important;

    font-weight: bold !important;
}


/* TITLE */
.main-title {

    text-align: center;

    font-size: 55px;

    font-weight: bold;

    color: white;

    margin-bottom: 30px;

    text-shadow: 0px 0px 20px cyan;
}


/* GLASS CARD */
.card {

    background: rgba(255,255,255,0.15);

    padding: 30px;

    border-radius: 20px;

    backdrop-filter: blur(10px);

    box-shadow: 0 8px 32px rgba(0,0,0,0.4);

    margin-bottom: 25px;

    color: white;
}


/* METRIC CARD */
.metric-card {

    background: linear-gradient(
        135deg,
        #06b6d4,
        #2563eb,
        #7c3aed
    );

    padding: 35px;

    border-radius: 20px;

    text-align: center;

    color: white !important;

    font-size: 32px;

    font-weight: bold;

    box-shadow: 0 0 20px rgba(255,255,255,0.3);
}


/* BUTTON */
.stButton > button {

    width: 100%;

    height: 3.5em;

    border-radius: 15px;

    border: none;

    font-size: 18px;

    font-weight: bold;

    color: white;

    background: linear-gradient(
        90deg,
        #06b6d4,
        #3b82f6,
        #8b5cf6
    );

    transition: 0.3s;
}


/* BUTTON HOVER */
.stButton > button:hover {

    transform: scale(1.03);

    box-shadow: 0 0 15px cyan;
}


/* INPUT BOX */
.stTextInput input {

    background-color: rgba(255,255,255,0.15);

    color: white !important;

    border-radius: 12px;

    border: 1px solid cyan;
}


/* TEXT AREA */
textarea {

    background-color: rgba(255,255,255,0.15) !important;

    color: white !important;

    border-radius: 12px !important;

    border: 1px solid cyan !important;
}


/* LABELS */
label {

    color: white !important;

    font-weight: bold !important;
}


/* TABLE */
[data-testid="stDataFrame"] {

    background-color: white;

    border-radius: 15px;

    padding: 10px;
}


/* SUCCESS MESSAGE */
.stSuccess {

    background-color: rgba(16, 185, 129, 0.25) !important;

    color: white !important;

    border: 2px solid #10b981 !important;

    border-radius: 15px !important;

    padding: 15px !important;
}


/* SUCCESS TEXT */
.stSuccess p {

    color: white !important;

    font-size: 20px !important;

    font-weight: bold !important;
}


/* INFO BOX */
.stInfo {

    background-color: rgba(59, 130, 246, 0.25) !important;

    color: white !important;

    border: 2px solid #3b82f6 !important;

    border-radius: 15px !important;

    padding: 15px !important;
}


/* INFO TEXT */
.stInfo p {

    color: white !important;

    font-size: 18px !important;

    font-weight: bold !important;
}


/* WARNING BOX */
.stWarning {

    background-color: rgba(245, 158, 11, 0.25) !important;

    color: white !important;

    border: 2px solid #f59e0b !important;

    border-radius: 15px !important;

    padding: 15px !important;
}


/* WARNING TEXT */
.stWarning p {

    color: white !important;

    font-size: 18px !important;

    font-weight: bold !important;
}


/* ERROR BOX */
.stError {

    background-color: rgba(239, 68, 68, 0.25) !important;

    color: white !important;

    border: 2px solid #ef4444 !important;

    border-radius: 15px !important;

    padding: 15px !important;
}


/* ERROR TEXT */
.stError p {

    color: white !important;

    font-size: 18px !important;

    font-weight: bold !important;
}

</style>
""", unsafe_allow_html=True)


# ================= TITLE =================

st.markdown("""
<div class='main-title'>
🧠 Mental Health Resource Finder
</div>
""", unsafe_allow_html=True)


# ================= SIDEBAR =================

st.sidebar.title("🌟 Navigation Menu")

menu = st.sidebar.radio(
    "Choose Option",
    [
        "🏠 Home",
        "➕ Add Resource",
        "🔍 Search Resource",
        "📋 View Resources",
        "🗑 Delete Resource"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success(
    "Mental Health Support System"
)

st.sidebar.info(
    "Find mental health resources quickly and easily."
)


# ================= HOME =================

if menu == "🏠 Home":

    data = view_resources()

    total_resources = len(data)

    total_cities = len(set([x[1] for x in data]))

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(f"""
        <div class='metric-card'>
            📌<br>
            Total Resources<br><br>
            {total_resources}
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown(f"""
        <div class='metric-card'>
            🌍<br>
            Cities Covered<br><br>
            {total_cities}
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class='card'>

    <h2 style='color:white;'>✨ Features</h2>

    <h4 style='color:white;'>

    ✅ Add New Mental Health Resources<br><br>

    ✅ Search Resources by City<br><br>

    ✅ View All Available Resources<br><br>

    ✅ Delete Existing Resources<br><br>

    ✅ MySQL Database Integration<br><br>

    ✅ Professional Streamlit Dashboard<br><br>

    ✅ Colorful Modern UI<br><br>

    </h4>

    </div>
    """, unsafe_allow_html=True)

    st.success(
        "Welcome to the Professional Mental Health Resource Finder"
    )


# ================= ADD RESOURCE =================

elif menu == "➕ Add Resource":

    st.markdown("""
    <div class='card'>
    <h2 style='color:white;'>➕ Add New Resource</h2>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        city = st.text_input("🌍 City")

        organization = st.text_input("🏥 Organization Name")

        helpline = st.text_input("☎ Helpline Number")

    with col2:

        website = st.text_input("🌐 Website")

        address = st.text_area("📍 Address")

    if st.button("Add Resource"):

        if city == "" or organization == "" or helpline == "":

            st.error("Please fill all required fields")

        else:

            add_resource(
                city,
                organization,
                helpline,
                website,
                address
            )

            st.success("✅ Resource Added Successfully")


# ================= SEARCH RESOURCE =================

elif menu == "🔍 Search Resource":

    st.markdown("""
    <div class='card'>
    <h2 style='color:white;'>🔍 Search Resource</h2>
    </div>
    """, unsafe_allow_html=True)

    city = st.text_input("Enter City Name")

    if st.button("Search"):

        data = search_resource(city)

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

            st.dataframe(
                df,
                use_container_width=True
            )

            st.success(
                f"{len(data)} Resource(s) Found"
            )


# ================= VIEW RESOURCES =================

elif menu == "📋 View Resources":

    st.markdown("""
    <div class='card'>
    <h2 style='color:white;'>📋 All Resources</h2>
    </div>
    """, unsafe_allow_html=True)

    data = view_resources()

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

    st.dataframe(
        df,
        use_container_width=True,
        height=500
    )

    st.info(
        f"Total Resources Available: {len(data)}"
    )


# ================= DELETE RESOURCE =================

elif menu == "🗑 Delete Resource":

    st.markdown("""
    <div class='card'>
    <h2 style='color:white;'>🗑 Delete Resource</h2>
    </div>
    """, unsafe_allow_html=True)

    resource_id = st.number_input(
        "Enter Resource ID",
        min_value=1,
        step=1
    )

    if st.button("Delete Resource"):

        delete_resource(resource_id)

        st.success("Resource Deleted Successfully")