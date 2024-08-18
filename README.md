# reg_bank

## AI-powered Regulatory Analysis and Knowledge Base for AI and GenAI Regulations

reg_bank is an innovative project aimed at leveraging artificial intelligence to monitor, analyze, and provide insights on the rapidly evolving landscape of AI and GenAI regulations across various jurisdictions.

### Project Description

In the fast-paced world of artificial intelligence and generative AI, keeping up with regulatory changes can be challenging. reg_bank addresses this challenge by creating an AI-driven system that:

1. Continuously searches for and identifies new AI and GenAI regulations worldwide.
2. Analyzes the implications and key points of these regulations.
3. Builds and maintains a comprehensive knowledge base of AI regulations.
4. Provides an intuitive interface for users to query this knowledge base.

### Objectives

- Develop a robust AI agent system for efficient regulatory research and analysis.
- Create a continuously updated, comprehensive database of AI and GenAI regulations.
- Implement a user-friendly interface for accessing regulatory information.
- Ensure accuracy and relevance of the information provided.
- Foster better understanding and compliance with AI regulations across industries.

### Roadmap

#### Phase 1: Foundation (Current)
- [x] Set up project structure
- [x] Implement basic CrewAI agents for research
- [x] Create a simple Streamlit interface for interaction
- [ ] Develop core functionality for regulation search and summarization

#### Phase 2: Enhanced Analysis
- [ ] Implement advanced NLP techniques for deeper regulation analysis
- [ ] Develop a structured database to store regulatory information
- [ ] Create more specialized AI agents (e.g., legal analysis, impact assessment)
- [ ] Improve the user interface with more detailed visualizations and interactions

#### Phase 3: Knowledge Base Development
- [ ] Design and implement a comprehensive knowledge base structure
- [ ] Develop algorithms for efficient information retrieval and querying
- [ ] Implement version control for tracking regulatory changes over time
- [ ] Create API endpoints for integration with other systems

#### Phase 4: Advanced Features and Scaling
- [ ] Implement machine learning models for predictive analysis of regulatory trends
- [ ] Develop customizable alerts and notifications for regulatory changes
- [ ] Create industry-specific modules for targeted regulatory insights
- [ ] Scale the system to handle global regulations across multiple languages

### Technical Overview

reg_bank is built using modern AI and web technologies:

- **Core AI Framework**: CrewAI
  - Utilized for creating and managing AI agents for research and analysis tasks.
- **Web Scraping and Search**: crewai_tools (SerperDevTool)
  - Enables efficient web searching for the latest regulatory information.
- **User Interface**: Streamlit
  - Provides a clean, interactive web interface for users to interact with the system.
- **Language Model**: Utilizes advanced language models (specifics to be determined) for text analysis and generation.
- **Database**: (To be implemented) For storing structured regulatory data.
- **Version Control**: Git
  - Used for project management and collaborative development.

### Current Implementation

The current version includes:
- A basic CrewAI setup with a research agent capable of searching for and summarizing news on a given topic.
- A Streamlit web interface allowing users to input a research topic and view results.
- Integration with SerperDevTool for web searching capabilities.

### Getting Started

1. Clone the repository:
   ```
   git clone https://github.com/modelisai/reg_bank.git
   cd reg_bank
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Copy the file `.env.example` to `.env` in the root directory
   - Add ad least these API keys:
        ```
        SERPER_API_KEY="<your serper API key>"
        OPENAI_API_KEY="<your openai API key>"
        ```

4. Run the Streamlit app:
   ```
   streamlit run ./research/research.py
   ```

### Contributing

We welcome contributions to reg_bank! Please see our [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines on how to contribute.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

reg_bank is a project in active development. We're excited to evolve this tool into a comprehensive solution for AI regulatory intelligence. Stay tuned for updates!