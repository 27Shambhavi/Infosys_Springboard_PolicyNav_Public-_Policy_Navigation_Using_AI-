# Infosys Springboard  

# 🧠 PolicyNav – Public Policy Navigation Using AI  
AI-powered platform for simplifying and navigating complex public policy documents using Natural Language Processing and Machine Learning.

---

## 🎥 Demo Video  
Watch the working demo of PolicyNav:  
[▶️ Demo Video](https://drive.google.com/file/d/1iWPSKYKJvN9n7cfZkcAdOkUDFPQ0DH1q/view?usp=sharing)

---

## 🔗 Links  
| Category       | Link |
| -------------- | ---- |
| Source Code    | This Repository |
| Docker Support | Yes |
| AI Models      | Sentence Transformers · FLAN-T5 · NLLB |

---

## 📌 Table of Contents  
- About the Project  
- Problem Statement & Motivation  
- Key Features  
- Architecture  
- Tech Stack  
- Models Used  
- Installation & Setup  
- Usage Guide  
- Admin Controls  
- Screenshots  
- Roadmap  
- Team  
- License  

---

## 📖 About the Project  
PolicyNav is an AI-powered platform developed during the Infosys Springboard Internship to improve accessibility and understanding of public policy documents.  

It uses advanced NLP techniques such as semantic search, summarization, multilingual translation, and entity extraction to transform complex policy documents into structured and easy-to-understand insights.  

The platform is designed for students, citizens, researchers, and policy analysts to efficiently explore, analyze, and interpret policies.

---

## 🎯 Problem Statement & Motivation  
Public policies are often difficult to understand due to:  
- Complex legal language  
- Lengthy and unstructured documents  
- Lack of centralized access  
- Language barriers  

PolicyNav addresses these challenges by simplifying content, enabling intelligent search, and providing multilingual, structured insights.

---

## 🚀 Key Features (Detailed)  

### 🔐 Secure Authentication  
Provides a complete user authentication system including signup, login, and OTP-based password recovery. Ensures secure access using JWT tokens and encrypted passwords (bcrypt), maintaining data privacy and session management.

---

### 🤖 AI Policy Assistant  
Allows users to interact with the system using natural language queries. The assistant understands user intent and retrieves relevant policy information using semantic search and NLP models, delivering accurate and contextual responses.

---

### 🌍 Multi-language Support  
Supports translation of both user queries and system responses using advanced multilingual models (NLLB). This ensures accessibility for users from different linguistic backgrounds.

---

### ✂️ Summarization  
Automatically generates concise summaries of long and complex policy documents using transformer-based models (FLAN-T5), helping users quickly grasp key information.

---

### 🧠 Knowledge Graph Visualization  
Extracts entities and relationships from policy text using NLP techniques and represents them visually using graphs (PyVis). This helps users understand connections between concepts, organizations, and regulations.

---

### 📊 Readability Analyzer  
Evaluates the complexity of policy text and provides simplified interpretations. Helps users better understand difficult content by reducing linguistic complexity.

---

### 🌐 Global Web Search  
Fetches additional policy-related information from external sources to provide broader context and enhance the accuracy of responses.

---

### 👤 Profile Management  
Allows users to manage their account details, update credentials, and personalize their experience within the platform.

---

### 📜 Activity History  
Tracks user queries and interactions, enabling users to revisit previous searches and maintain continuity in their exploration.

---

### ⭐ Feedback System  
Enables users to provide ratings and feedback, helping improve system performance and user experience.

---

## 🛠 Admin Features (Detailed)  

### 👥 User Management  
Admins can view, block, or delete users to maintain system integrity and security.

### 📊 Feedback Monitoring  
Allows administrators to analyze user feedback and identify areas for improvement.

### 📋 Activity Logs  
Tracks system-wide activity for monitoring usage patterns and debugging.

### 📈 Analytics Dashboard  
Provides insights into user engagement, usage statistics, and system performance.

---

## 🧩 Architecture  
Monolithic architecture integrating all components:  

**User → Streamlit UI → Python Backend → AI Models → Database**

---

## 🛠 Tech Stack  
| Layer         | Technology |
| ------------- | ---------- |
| Frontend      | Streamlit |
| Backend       | Python |
| Database      | SQLite |
| AI Models     | Hugging Face Transformers |
| Search        | FAISS |
| NLP           | SpaCy |
| Visualization | PyVis |
| Security      | JWT, bcrypt, OTP |
| Deployment    | Docker |

---

## 🤖 Models Used  
| Model                 | Purpose |
| --------------------- | ------- |
| Sentence Transformers | Semantic search and embeddings |
| FLAN-T5               | Text summarization |
| NLLB                  | Multilingual translation |
| SpaCy                 | Named entity recognition |

---

## ⚙️ Installation & Setup  

```bash
git clone <repository-link>
cd PolicyNav
pip install -r requirements.txt
streamlit run app.py

![ScreenShots]

<img width="913" height="401" alt="Screenshot 2026-03-15 133821" src="https://github.com/user-attachments/assets/2e03ac89-a653-496f-8788-62c024c53051" />
<img width="1700" height="717" alt="Screenshot 2026-03-18 230308" src="https://github.com/user-attachments/assets/158da1f7-a70b-4b4f-b7f2-0367b350504f" />
<img width="1693" height="751" alt="Screenshot 2026-03-18 230257" src="https://github.com/user-attachments/assets/f2558292-e101-4893-8a64-7db72fb98e01" />
<img width="1757" height="800" alt="Screenshot 2026-03-18 230236" src="https://github.com/user-attachments/assets/8fbbaaed-f4a8-4b5a-ae64-905db9bf5b3c" />
<img width="1850" height="823" alt="Screenshot 2026-03-18 225956" src="https://github.com/user-attachments/assets/f2c40100-3b3e-47b3-9cf0-f8f7d0c0354e" />
<img width="1824" height="814" alt="Screenshot 2026-03-18 225902" src="https://github.com/user-attachments/assets/7f8da425-3106-4d20-baa3-a74b36004b7b" />
<img width="1784" height="804" alt="Screenshot 2026-03-18 225734" src="https://github.com/user-attachments/assets/06ee4013-5d12-4d1d-8953-cccdb9fcd443" />
<img width="991" height="555" alt="Screenshot 2026-03-18 225708" src="https://github.com/user-attachments/assets/2499892a-3edd-418e-aeb1-c51b379bb284" />
<img width="1796" height="811" alt="Screenshot 2026-03-18 225653" src="https://github.com/user-attachments/assets/45faa885-b78c-4ca5-b858-b3e859d9812c" />
<img width="1893" height="847" alt="Screenshot 2026-03-18 225641" src="https://github.com/user-attachments/assets/e5a52a12-0c0c-49ad-8bed-a8bbd6b78f84" />
<img width="1909" height="821" alt="Screenshot 2026-03-18 225619" src="https://github.com/user-attachments/assets/6c685fdf-d43d-4b4b-97ab-5fc3b8764c0d" />
<img width="1892" height="829" alt="Screenshot 2026-03-18 225554" src="https://github.com/user-attachments/assets/3a21733b-2a92-4c5f-bd61-d2ac63c0473d" />
<img width="1880" height="830" alt="Screenshot 2026-03-18 225531" src="https://github.com/user-attachments/assets/d9e1b0b9-a2a0-4d18-b8b0-15c7e5f3ea0f" />
<img width="1865" height="842" alt="Screenshot 2026-03-18 225511" src="https://github.com/user-attachments/assets/f088c04d-0e76-49bd-aea6-a4bf2f39e02a" />
<img width="1026" height="406" alt="Screenshot 2026-03-18 021246" src="https://github.com/user-attachments/assets/5dff955e-8708-413e-9741-8f354fecbabb" />
<img width="873" height="339" alt="Screenshot 2026-03-18 004338" src="https://github.com/user-attachments/assets/de99336a-9bbd-403d-82f4-7ef56076f2b0" />
<img width="1026" height="406" alt="Screenshot 2026-03-18 021246" src="https://github.com/user-attachments/assets/beb25f80-fff1-4cbc-aa04-ae043d8946d0" />

