// ============================================
// ResearchHub MongoDB Database Setup
// ============================================

use("researchhub");


// ============================================
// Research Documents
// ============================================

db.research_documents.insertMany([
  {
    publication_id: 1,
    title: "AI-Based Healthcare Prediction",
    abstract: "This research explores the use of artificial intelligence and machine learning techniques for predicting healthcare outcomes.",
    keywords: [
      "Artificial Intelligence",
      "Machine Learning",
      "Healthcare Prediction"
    ],
    document_type: "Research Paper",
    publication_year: 2025
  },

  {
    publication_id: 2,
    title: "Machine Learning for Traffic Prediction",
    abstract: "This research studies machine learning techniques for predicting traffic patterns and improving transportation planning.",
    keywords: [
      "Machine Learning",
      "Traffic Prediction",
      "Transportation"
    ],
    document_type: "Research Paper",
    publication_year: 2024
  },

  {
    publication_id: 3,
    title: "Deep Learning for Image Classification",
    abstract: "This research explores deep learning techniques for classifying images using neural network models.",
    keywords: [
      "Deep Learning",
      "Image Classification",
      "Neural Networks"
    ],
    document_type: "Research Paper",
    publication_year: 2025
  },

  {
    publication_id: 4,
    title: "Natural Language Processing for Research Analysis",
    abstract: "This research explores natural language processing techniques for analyzing research documents and extracting useful information.",
    keywords: [
      "Natural Language Processing",
      "Research Analysis",
      "Text Mining"
    ],
    document_type: "Research Paper",
    publication_year: 2023
  },

  {
    publication_id: 5,
    title: "Autonomous Vehicle Decision Making Using Machine Learning",
    abstract: "This research explores machine learning techniques for decision making in autonomous vehicles, including actions such as stopping, turning, and avoiding obstacles.",
    keywords: [
      "Autonomous Vehicles",
      "Machine Learning",
      "Decision Making",
      "Obstacle Avoidance"
    ],
    document_type: "Research Paper",
    publication_year: 2025
  },

  {
    publication_id: 6,
    title: "Data Analytics for Research Performance",
    abstract: "This research explores data analytics techniques for evaluating research performance and identifying useful research insights.",
    keywords: [
      "Data Analytics",
      "Research Performance",
      "Research Insights"
    ],
    document_type: "Research Paper",
    publication_year: 2024
  }
]);


// ============================================
// Citation Data
// ============================================

db.citation_data.insertMany([
  {
    citing_publication_id: 5,
    cited_publication_id: 2,
    citation_year: 2025
  },

  {
    citing_publication_id: 3,
    cited_publication_id: 1,
    citation_year: 2025
  },

  {
    citing_publication_id: 6,
    cited_publication_id: 4,
    citation_year: 2024
  },

  {
    citing_publication_id: 2,
    cited_publication_id: 6,
    citation_year: 2024
  },

  {
    citing_publication_id: 1,
    cited_publication_id: 3,
    citation_year: 2025
  }
]);