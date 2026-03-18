# Infosys Springboard
# 🧠 PolicyNav - Public-Policy-Navigation-Using-AI
AI-Powered Public Policy Navigation and Intelligence Platform
Simplifying complex government policies through multilingual AI, summarization, and intelligent search.
# 🔗 Links: 
| Category       | Link                                   |
| -------------- | -------------------------------------- |
| Demo Video     | https://drive.google.com/file/d/1iWPSKYKJvN9n7cfZkcAdOkUDFPQ0DH1q/view?usp=sharing |
| Source Code    | This Repository                        |
| Docker Support | Yes                                    |
| AI Models      | Sentence Transformers · FLAN-T5 · NLLB |
# 📌 Table of Contents
- About the Project
- Problem Statement & Motivation
- Key Features
- Architecture
- Tech Stack
- Models Used
- Project Structure
- Installation & Setup
- Usage Guide
- Admin Controls
- Screenshots
- Roadmap
- Team
- License
# 🚀 Key Features (Detailed Explanation)

## 👤 User Features

### 🔐 Secure Authentication System
The platform implements a robust authentication and authorization mechanism to ensure user data security and controlled access.

- Uses JWT (JSON Web Tokens) for session management, enabling stateless and secure authentication.
- Passwords are encrypted using bcrypt hashing, preventing plaintext storage.
- Includes OTP-based password recovery, ensuring secure identity verification.
- Protects endpoints from unauthorized access through token validation.

Why it matters:  
Ensures user privacy, prevents unauthorized access, and aligns with modern security best practices.

---

### 🤖 AI Policy Assistant
An intelligent conversational interface that allows users to interact with public policies using natural language queries.

- Built using transformer-based NLP models.
- Converts user queries into embeddings via Sentence Transformers.
- Performs semantic search using FAISS to retrieve the most relevant policy content.
- Generates contextual responses using FLAN-T5.

Example Workflow:  
User Query → Embedding → FAISS Retrieval → Context Extraction → FLAN-T5 Response

Why it matters:  
Removes the need for users to manually read long documents and enables intuitive interaction.

---

### 🌍 Multi-language Support
Enables accessibility for users from diverse linguistic backgrounds.

- Uses NLLB (No Language Left Behind) model for translation.
- Supports both:
  - Query translation (user input → English for processing)
  - Response translation (output → user’s preferred language)

Why it matters:  
Breaks language barriers and makes government policies accessible to a wider audience.

---

### ✂️ Intelligent Summarization
Automatically generates concise summaries of lengthy policy documents.

- Uses FLAN-T5, a fine-tuned transformer model.
- Extracts key information while preserving meaning and context.
- Supports dynamic summarization based on retrieved policy sections.

Why it matters:  
Saves time and improves comprehension of complex documents.

---

### 🕸 Knowledge Graph Visualization
Transforms unstructured policy data into structured visual relationships.

- Uses SpaCy for Named Entity Recognition (NER).
- Extracts entities such as organizations, policies, dates, and keywords.
- Builds relationships and visualizes them using PyVis interactive graphs.

Why it matters:  
Helps users understand connections between policies, stakeholders, and concepts visually.

---

### 📖 Readability Analyzer
Evaluates and simplifies complex policy text for better understanding.

- Uses NLP techniques to:
  - Measure sentence complexity
  - Identify difficult words and structures
- Provides simplified interpretations of policy content.

Why it matters:  
Ensures accessibility for non-expert users and improves inclusivity.

---

### 🌐 Global Web Search Integration
Enhances policy understanding by fetching external, real-time information.

- Integrates web search APIs to retrieve:
  - Latest policy updates
  - Related news and articles
- Combines internal knowledge base with external data sources.

Why it matters:  
Keeps users informed with up-to-date and contextual information.

---

### 👤 Profile Management System
Allows users to manage personal information securely.

- Update email and password
- Upload avatar/profile image
- Manage account preferences

Why it matters:  
Improves user personalization and engagement.

---

### 📊 Activity History Tracking
Maintains a log of user interactions.

- Stores:
  - Queries asked
  - Summaries generated
  - Actions performed
- Enables users to revisit previous insights.

Why it matters:  
Improves usability and supports continuity in research.

---

### ⭐ Feedback & Rating System
Collects user feedback for continuous improvement.

- Users can:
  - Rate system responses
  - Provide comments
- Admin can analyze feedback trends.

Why it matters:  
Helps refine AI responses and improve system performance.

---

## 🛡 Admin Features (Detailed)

### 👥 User Management Dashboard
- View all registered users
- Block or delete suspicious accounts
- Monitor user activity patterns

---

### 📈 System Monitoring & Analytics
- Track:
  - Number of queries
  - Active users
  - System usage trends

---

### 💬 Feedback Moderation
- Analyze user feedback
- Identify issues in AI responses
- Improve model performance based on insights

---

### 📜 Activity Logs
- Maintain logs for:
  - User actions
  - System events
- Useful for debugging and auditing

---

## 🧩 Architecture (Detailed Explanation)

The system follows a monolithic architecture where all components are integrated into a unified application.

### 🔄 Data Flow

1. User interacts via Streamlit UI  
2. Request is sent to Python backend  
3. Backend processes:
   - Authentication
   - Query handling  
4. AI modules perform:
   - Embedding generation
   - Semantic search (FAISS)
   - Summarization / translation  
5. Results are returned to UI  
6. Data is stored/retrieved from SQLite database  

---

### 🧠 AI Pipeline

- Input Query  
→ Preprocessing  
→ Embedding (Sentence Transformers)  
→ Retrieval (FAISS)  
→ Processing (FLAN-T5 / NLLB)  
→ Output Response  

Why Monolithic?  
- Easier deployment (especially with Docker)  
- Simpler integration of AI modules  
- Suitable for prototype and hackathon environments  

---

## 🛠 Tech Stack (Detailed Justification)

| Layer         | Technology                 | Why Used |
|--------------|--------------------------|---------|
| Frontend     | Streamlit                 | Rapid UI development and ML integration |
| Backend      | Python                    | Strong ecosystem for AI/ML and APIs |
| Database     | SQLite                    | Lightweight and easy to integrate |
| AI Models    | Hugging Face Transformers | State-of-the-art NLP capabilities |
| Search       | FAISS                     | Fast similarity search for embeddings |
| NLP          | SpaCy                     | Efficient entity extraction |
| Visualization| PyVis                     | Interactive graph visualization |
| Security     | JWT, bcrypt, OTP          | Secure authentication and encryption |
| Deployment   | Docker                    | Easy containerization and portability |

---

## 🤖 Models Used (Detailed Explanation)

### Sentence Transformers
- Converts text into dense vector embeddings  
- Enables semantic similarity search  
- Works with FAISS for fast retrieval  

---

### FLAN-T5
- Instruction-tuned transformer model  
- Used for:
  - Summarization  
  - Question answering  
- Generates human-like responses  

---

### NLLB (No Language Left Behind)
- Meta AI multilingual translation model  
- Supports low-resource languages  
- Ensures global accessibility  

---

### SpaCy
- Industrial-strength NLP library  
- Used for:
  - Named Entity Recognition (NER)  
  - Text preprocessing
 

# 📸 Screenshots


<img width="913" height="401" alt="Screenshot 2026-03-15 133821" src="https://github.com/user-attachments/assets/12289b46-31bd-41ac-8084-8811f4f7980b" />
<img width="1865" height="842" alt="Screenshot 2026-03-18 225511" src="https://github.com/user-attachments/assets/8f9cd591-8e89-48af-a55f-6c53748bbfe7" />
<img width="1026" height="406" alt="Screenshot 2026-03-18 021246" src="https://github.com/user-attachments/assets/8e548c4c-4080-4730-a188-f70b891c3d0d" />
<img width="1893" height="847" alt="Screenshot 2026-03-18 225641" src="https://github.com/user-attachments/assets/39e8a589-21fa-41a9-bd4b-69dbedb27b5c" />
<img width="1909" height="821" alt="Screenshot 2026-03-18 225619" src="https://github.com/user-attachments/assets/be66cc46-fe34-4ea9-8f59-e30f78ecab56" />
<img width="1892" height="829" alt="Screenshot 2026-03-18 225554" src="https://github.com/user-attachments/assets/881a72c8-8baa-4ae4-8420-bec8c0d7c4fc" />
<img width="1<img width="1784" height="804" alt="Screenshot 2026-03-18 225734" src="https://github.com/user-attachments/assets/802c4243-3251-4d28-a8d2-557ad56a43ca" />
<img width="991" height="555" alt="Screenshot 2026-03-18 225708" src="https://github.com/user-attachments/assets/d9d80693-ebcf-4cf1-ac2e-df6b905d5f2c" />
<img width="1796" height="811" alt="Screenshot 2026-03-18 225653" src="https://github.com/user-attachments/assets/62abd28c-2f82-4330-bcf8-fcd6ff6fe57a" />
<img width="1700" height="717" alt="Screenshot 2026-03-18 230308" src="https://github.com/user-attachments/assets/7feda5b0-58d2-4415-bedb-95eb967913f9" />
<img width="1693" height="751" alt="Screenshot 2026-03-18 230257" src="https://github.com/user-attachments/assets/931c4283-fa1b-48a4-8ab3-dcca4366da22" />
<img width="1757" height="800" alt="Screenshot 2026-03-18 230236" src="https://github.com/user-attachments/assets/420669a0-09c1-49eb-97f5-66bb17660d76" />
<img width="1850" height="823" alt="Screenshot 2026-03-18 225956" src="https://github.com/user-attachments/assets/133c0a18-1579-432d-a2c6-143d5e03bda1" />
<img width="1824" height="814" alt="Screenshot 2026-03-18 225902" src="https://github.com/user-attachments/assets/a4b611e3-8f3b-4bbc-acee-af7fe734581c" />
880" height="830" alt="Screenshot 2026-03-18 225531" src="https://github.com/user-attachments/assets/1e6c1af5-3ad7-4e77-be72-441f08d4e79d" />

# 📊 Roadmap
- Improve model performance
- Add more datasets
- Enhance UI/UX
- Deploy on cloud platform
- Add voice-based interaction
# 👥 Team
| Name                          | Role                              |
| ----------------------------- | --------------------------------- |
| Shambhavi Jha                 | AI and NLP Development            |
| Srideepalakshmi Muruganantham | Backend and Security              |
| Mainuddeen                    | Summarization and Web Integration |
| Bhuvaneshwar Reddy Mandadapu  | Profile and System Integration    |
| Arjun L Nair                  | Testing and Deployment            |
# 📜 License
MIT License
- Free to use, modify, and distribute with proper credits.
