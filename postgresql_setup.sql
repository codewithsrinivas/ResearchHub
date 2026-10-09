-- ============================================
-- ResearchHub PostgreSQL Database Setup
-- ============================================

-- Create database
CREATE DATABASE researchhub;

-- After creating the database, connect to researchhub
-- in pgAdmin before running the remaining commands.


-- Create schema
CREATE SCHEMA research;


-- ============================================
-- Departments
-- ============================================

CREATE TABLE research.departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

INSERT INTO research.departments (department_name)
VALUES
('Computer Science'),
('Artificial Intelligence'),
('Data Science'),
('Electronics');


-- ============================================
-- Authors
-- ============================================

CREATE TABLE research.authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES research.departments(department_id)
);

INSERT INTO research.authors
    (author_name, email, department_id)
VALUES
('Srinivas', 'srinivas@gmail.com', 1),
('Mounika', 'mounika@gmail.com', 2),
('Krishna', 'krishna@gmail.com', 3),
('Ravi', 'ravi@gmail.com', 1),
('Yeshu Reddy', 'yeshu.reddy@gmail.com', 2),
('Naseem', 'naseem@gmail.com', 3);


-- ============================================
-- Publications
-- ============================================

CREATE TABLE research.publications (
    publication_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publication_year INT,
    journal VARCHAR(200),
    research_area VARCHAR(100)
);

INSERT INTO research.publications
    (title, publication_year, journal, research_area)
VALUES
('AI-Based Healthcare Prediction',
 2025,
 'IEEE',
 'Artificial Intelligence'),

('Machine Learning for Traffic Prediction',
 2024,
 'Springer',
 'Machine Learning'),

('Deep Learning for Image Classification',
 2025,
 'IEEE',
 'Deep Learning'),

('Natural Language Processing for Research Analysis',
 2023,
 'Elsevier',
 'Natural Language Processing'),

('Autonomous Vehicle Decision Making Using Machine Learning',
 2025,
 'IEEE',
 'Machine Learning'),

('Data Analytics for Research Performance',
 2024,
 'Springer',
 'Data Science');


-- ============================================
-- Publication Authors
-- ============================================

CREATE TABLE research.publication_authors (
    publication_id INT,
    author_id INT,
    PRIMARY KEY (publication_id, author_id),
    FOREIGN KEY (publication_id)
        REFERENCES research.publications(publication_id),
    FOREIGN KEY (author_id)
        REFERENCES research.authors(author_id)
);

INSERT INTO research.publication_authors
    (publication_id, author_id)
VALUES
(1, 1),
(1, 2),
(2, 1),
(2, 4),
(3, 3),
(3, 5),
(4, 2),
(4, 6),
(5, 1),
(5, 3),
(5, 4),
(6, 5),
(6, 6);