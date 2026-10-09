# ResearchHub

## Research Information and Analytics Platform

ResearchHub is a research information and analytics platform for managing
publications, authors, research documents, and citation information.

The project uses PostgreSQL for structured research information,
MongoDB for research documents and citation data, and Python with
Streamlit for analytics and dashboard visualization.

---

## Use Case

A research information and analytics platform for managing publications,
authors, research documents, and citation information.

---

## Project Description

PostgreSQL manages structured publication and author information.

MongoDB stores research documents and citation-related data.

The Python dashboard provides:

- Research analytics
- Publication trends
- Author productivity
- Citation analysis
- Research area analysis
- Research performance insights

---

## Technologies Used

- Python
- PostgreSQL
- MongoDB
- Streamlit
- Pandas
- Psycopg2
- PyMongo
- Python-dotenv

---

## Database Structure

### PostgreSQL

PostgreSQL contains the structured research information.

Main tables:

- departments
- authors
- publications
- publication_authors

### MongoDB

MongoDB contains:

- research_documents
- citation_data

---

## Dashboard Features

### 1. Dashboard Metrics

Displays:

- Total Publications
- Total Authors
- Research Documents
- Total Citations

### 2. Publication Trends

Shows the number of publications for each year.

### 3. Author Productivity

Shows the number of publications associated with each author.

### 4. Citation Analysis

Shows citation counts for publications.

### 5. Research Performance Insights

Provides basic research performance information based on the stored data.

### 6. Publications

Displays publication information including:

- Publication ID
- Title
- Year
- Journal
- Research Area

### 7. Authors

Displays:

- Author ID
- Author Name
- Email
- Department

### 8. Research Documents

Displays research documents stored in MongoDB.

### 9. Citation Details

Displays citation relationships stored in MongoDB.

### 10. Research Area Analysis

Shows publication distribution across research areas.

---

## Project Structure

```text
ResearchHub/
│
├── app.py
├── postgres_connection.py
├── mongodb_connection.py
├── requirements.txt
├── postgresql_setup.sql
├── mongodb_setup.js
├── .env
├── .env.example
├── .gitignore
└── README.md