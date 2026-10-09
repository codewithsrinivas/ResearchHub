import streamlit as st
import psycopg2
import pandas as pd
import plotly.express as px
from pathlib import Path
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Page settings
st.set_page_config(
    page_title="ResearchHub",
    page_icon="📚",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #07111f, #0b1f35, #102f4a);
}

[data-testid="stHeader"] {
    background: transparent;
}

h1, h2, h3 {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# ResearchHub Welcome Screen
# ==============================

if "entered_researchhub" not in st.session_state:
    st.session_state.entered_researchhub = False

if not st.session_state.entered_researchhub:

    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #07111f, #102a43, #0b3d5c);
    }

    .welcome-box {
        text-align: center;
        padding-top: 120px;
        color: white;
    }

    .welcome-title {
        font-size: 60px;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .welcome-subtitle {
        font-size: 24px;
        margin-bottom: 15px;
    }

    .welcome-text {
        font-size: 18px;
        color: #d7e7f5;
        margin-bottom: 35px;
    }
    </style>
    """, unsafe_allow_html=True)

    image_path = Path(__file__).parent / "ResearchHub_welcome.png"
    st.image(str(image_path), use_container_width=True)

    st.markdown("""
    <div class="welcome-box">
        <div class="welcome-title">📚 ResearchHub</div>
        <div class="welcome-subtitle">
            Research Information & Analytics Platform
        </div>
        <div class="welcome-text">
            Explore publications, authors, citations and research insights
            using data-driven analytics.
        </div>
    </div>
    """, unsafe_allow_html=True)

 

    st.markdown("<br>", unsafe_allow_html=True)

    if st.button("🚀 Enter ResearchHub", use_container_width=True):
        st.session_state.entered_researchhub = True
        st.rerun()
    st.stop()

st.markdown(
    "<h1 style='color:white; font-size:42px;'>📚 ResearchHub</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='color:#b8c7d9; font-size:20px; font-style:italic;'>"
    "Research Information & Analytics Platform"
    "</p>",
    unsafe_allow_html=True
)

# PostgreSQL connection
pg_connection = psycopg2.connect(
    host="localhost",
    database="researchhub",
    user="postgres",
    password=os.getenv("POSTGRES_PASSWORD"),
    port="5432",
    sslmode="disable"

)

pg_cursor = pg_connection.cursor()

# Get total publications
pg_cursor.execute("SELECT COUNT(*) FROM research.publications;")
total_publications = pg_cursor.fetchone()[0]

# Get total authors
pg_cursor.execute("SELECT COUNT(*) FROM research.authors;")
total_authors = pg_cursor.fetchone()[0]

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017")
mongo_database = mongo_client["researchhub"]

# Get total research documents
total_documents = mongo_database["research_documents"].count_documents({})

# Get total citations
total_citations = mongo_database["citation_data"].count_documents({})

# Dashboard metrics
# Professional metric cards

st.markdown("""
<style>
.metric-card {
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 15px;
    padding: 20px;
    text-align: center;
    margin-bottom: 20px;
}

.metric-title {
    color: #b8c7d9;
    font-size: 16px;
    font-weight: 500;
}

.metric-value {
    color: white;
    font-size: 36px;
    font-weight: 700;
    margin-top: 8px;
}
</style>
""", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📚 Total Publications</div>
        <div class="metric-value">{total_publications}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">👨‍🔬 Total Authors</div>
        <div class="metric-value">{total_authors}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📄 Research Documents</div>
        <div class="metric-value">{total_documents}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">🔗 Total Citations</div>
        <div class="metric-value">{total_citations}</div>
    </div>
    """, unsafe_allow_html=True)

# Publication Trends
pg_cursor.execute("""
    SELECT publication_year, COUNT(*) AS publication_count
    FROM research.publications
    GROUP BY publication_year
    ORDER BY publication_year;
""")

trend_data = pg_cursor.fetchall()

years = [row[0] for row in trend_data]
publication_counts = [row[1] for row in trend_data]

st.markdown(
    "<h2 style='color:white;'>📈 Publication Trends</h2>",
    unsafe_allow_html=True
)

trend_df = pd.DataFrame({
    "Year": years,
    "Publications": publication_counts
})

fig = px.line(
    trend_df,
    x="Year",
    y="Publications",
    markers=True,
    title="Publications by Year"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    title_font_size=20,
    xaxis_title="Publication Year",
    yaxis_title="Number of Publications"
)

st.plotly_chart(fig, use_container_width=True)



# Author Productivity
pg_cursor.execute("""
    SELECT
        a.author_name,
        COUNT(pa.publication_id) AS publication_count
    FROM research.authors a
    LEFT JOIN research.publication_authors pa
        ON a.author_id = pa.author_id
    GROUP BY a.author_id, a.author_name
    ORDER BY publication_count DESC;
""")

author_data = pg_cursor.fetchall()

author_names = [row[0] for row in author_data]
author_publications = [row[1] for row in author_data]

author_df = pd.DataFrame({
    "Author": author_names,
    "Publications": author_publications
})

st.markdown(
    "<h2 style='color:white;'>👨‍🔬 Author Productivity</h2>",
    unsafe_allow_html=True
)

fig = px.bar(
    author_df,
    x="Publications",
    y="Author",
    orientation="h",
    title="Publications by Author"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    title_font_size=20,
    xaxis_title="Number of Publications",
    yaxis_title="Author"
)

st.plotly_chart(fig, use_container_width=True)

# Citation Analysis
citation_collection = mongo_database["citation_data"]

citation_pipeline = [
    {
        "$group": {
            "_id": "$cited_publication_id",
            "citation_count": {"$sum": 1}
        }
    },
    {
        "$sort": {
            "citation_count": -1
        }
    }
]

citation_data = list(citation_collection.aggregate(citation_pipeline))

citation_ids = [row["_id"] for row in citation_data]
citation_counts = [row["citation_count"] for row in citation_data]

citation_df = pd.DataFrame({
    "Publication ID": citation_ids,
    "Citations": citation_counts
})

st.markdown(
    "<h2 style='color:white;'>🔗 Citation Analysis</h2>",
    unsafe_allow_html=True
)

fig = px.bar(
    citation_df,
    x="Publication ID",
    y="Citations",
    title="Citations by Publication"
)

fig.update_layout(
    template="plotly_dark",
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(color="white"),
    title_font_size=20,
    xaxis_title="Publication ID",
    yaxis_title="Number of Citations"
)

st.plotly_chart(fig, use_container_width=True)

# Research Performance Insights

st.markdown(
    "<h2 style='color:white;'>💡 Research Performance Insights</h2>",
    unsafe_allow_html=True
)

total_authors = len(author_data)
total_citations = len(citation_data)

st.write(
    f"ResearchHub currently contains {total_publications} publications "
    f"written by {total_authors} authors."
)

st.write(
    f"The research database contains {total_citations} citation records."
)

st.write(
    "These metrics can be used to understand publication activity, "
    "author productivity, and citation patterns."
)

# Publications Table

st.markdown(
    "<h2 style='color:white;'>📈 Publication Trends</h2>",
    unsafe_allow_html=True
)

pg_cursor.execute("""
    SELECT
        publication_id,
        title,
        publication_year,
        journal,
        research_area
    FROM research.publications
    ORDER BY publication_id;
""")

publications_table = pg_cursor.fetchall()

publications_df = pd.DataFrame(
    publications_table,
    columns=[
        "ID",
        "Title",
        "Year",
        "Journal",
        "Research Area"
    ]
)

st.dataframe(
    publications_df,
    use_container_width=True
)

# Authors Table

st.markdown(
    "<h2 style='color:white;'>👨‍🔬 Author Productivity</h2>",
    unsafe_allow_html=True
)

pg_cursor.execute("""
    SELECT
        a.author_id,
        a.author_name,
        a.email,
        d.department_name
    FROM research.authors a
    LEFT JOIN research.departments d
        ON a.department_id = d.department_id
    ORDER BY a.author_id;
""")

authors_table = pg_cursor.fetchall()

authors_df = pd.DataFrame(
    authors_table,
    columns=[
        "ID",
        "Author Name",
        "Email",
        "Department"
    ]
)

st.dataframe(
    authors_df,
    use_container_width=True
)

# Research Documents Table

st.markdown(
    "<h2 style='color:white;'>📄 Research Documents</h2>",
    unsafe_allow_html=True
)

documents_collection = mongo_database["research_documents"]

documents_data = list(
    documents_collection.find(
        {},
    {
    "_id": 0,
    "publication_id": 1,
    "title": 1,
    "keywords": 1,
    "document_type": 1,
    "publication_year": 1
    }
    ).sort("publication_id", 1)
)

documents_df = pd.DataFrame(documents_data)

st.dataframe(
    documents_df,
    use_container_width=True
)

# Citation Details Table

st.markdown(
    "<h2 style='color:white;'>🔗 Citation Details</h2>",
    unsafe_allow_html=True
)

citation_details = list(
    citation_collection.find(
        {},
        {
            "_id": 0,
            "citing_publication_id": 1,
            "cited_publication_id": 1,
            "citation_year": 1
        }
    ).sort("citation_year", 1)
)

citation_details_df = pd.DataFrame(citation_details)

st.dataframe(
    citation_details_df,
    use_container_width=True
)

# Research Area Analysis

st.markdown(
    "<h2 style='color:white;'>📊 Research Area Analysis</h2>",
    unsafe_allow_html=True
)

pg_cursor.execute("""
    SELECT
        research_area,
        COUNT(*) AS publication_count
    FROM research.publications
    GROUP BY research_area
    ORDER BY publication_count DESC;
""")

research_area_data = pg_cursor.fetchall()

research_area_df = pd.DataFrame(
    research_area_data,
    columns=[
        "Research Area",
        "Publications"
    ]
)

st.bar_chart(
    research_area_df,
    x="Research Area",
    y="Publications"
)

# Close connections
pg_cursor.close()
pg_connection.close()
mongo_client.close()

