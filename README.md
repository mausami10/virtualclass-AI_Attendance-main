# 🎓 VirtualClass | AI Powered Attendance System

VirtualClass is a Streamlit web app that takes classroom attendance using **face recognition** and **voice biometrics**. Teachers upload class photos or record a voice roll call, and the AI marks who is present. Students log in with their face and can track their attendance in every subject.

### 🚀 [Live App → virtualclass-main.streamlit.app](https://virtualclass-main.streamlit.app/)

### 🌐 [Landing Page → ai-attendance-landing-page-psi.vercel.app](https://ai-attendance-landing-page-psi.vercel.app)

---

## ✨ Features

### 👩‍🏫 For Teachers
- **Secure registration and login** with username and password (passwords are hashed with bcrypt).
- **Subject management:** create subjects with a name, section and unique subject code, and share the code with students.
- **Face attendance:** add one or more class photos, run the face analysis, and review the Present/Absent results before saving.
- **Voice attendance:** take a voice roll call, where each student's voice is matched against their stored voice embedding.
- **Attendance records:** view past sessions grouped by subject and time, with present counts.

### 🎒 For Students
- **FaceID login** using the webcam, with no password needed.
- **Self-registration** for new students, with an optional voice enrolment for voice-only attendance.
- **Subject enrolment** using the subject code from the teacher.
- **Personal dashboard** showing total classes and classes attended per subject, with the option to unenrol.

## 🧠 How the AI Works

| Part | Approach |
|---|---|
| **Face detection and embeddings** | dlib's frontal face detector, shape predictor and face recognition model (via `face_recognition_models`) produce a 128-dimension face embedding |
| **Face identification** | A scikit-learn linear SVM classifier is trained on the stored student embeddings, and a distance threshold confirms the match |
| **Voice embeddings** | Resemblyzer's `VoiceEncoder` creates a voice embedding after Librosa loads the audio at 16 kHz |
| **Voice identification** | Cosine similarity between the new and stored embeddings, with a minimum threshold of 0.65 |
| **Bulk voice roll call** | Librosa splits the recording on silence, and each segment is matched to a student |

## 🛠️ Tech Stack

- **Frontend and app framework:** [Streamlit](https://streamlit.io/)
- **Face recognition:** dlib, face_recognition_models, scikit-learn
- **Voice recognition:** Resemblyzer, Librosa
- **Database and storage:** [Supabase](https://supabase.com/) (PostgreSQL)
- **Security:** bcrypt password hashing
- **Data handling:** NumPy, pandas, Pillow

## 📁 Project Structure

```
virtualclass-AI_Attendance-main/
├── app.py                      # App entry point and screen routing
├── assets/                     # Images (logo)
└── src/
    ├── screens/                # home_screen, teacher_screen, student_screen
    ├── components/             # header, footer, subject card, dialogs
    ├── pipelines/
    │   ├── face_pipeline.py    # Face embeddings, SVM training, prediction
    │   └── voice_pipeline.py   # Voice embeddings and speaker identification
    ├── database/
    │   ├── config.py           # Supabase client
    │   └── db.py               # Database queries
    └── ui/
        └── base_layout.py      # Global styling
```

## 🗄️ Database Tables (Supabase)

`teachers`, `students`, `subjects`, `subject_students`, `attendance_logs`

## ▶️ Run Locally

1. **Clone the repository**

   ```bash
   git clone https://github.com/mausami10/virtualclass-AI_Attendance-main.git
   cd virtualclass-AI_Attendance-main
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows (PowerShell)
   venv\Scripts\Activate.ps1
   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > `dlib` can take a while to build and needs CMake and a C++ compiler on your machine.

4. **Add your Supabase credentials**

   Add your Supabase project URL and key the way `src/database/config.py` reads them (for example in `.streamlit/secrets.toml`). Do not commit this file.

5. **Run the app**

   ```bash
   streamlit run app.py
   ```

## ☁️ Deployment

The app is deployed on [Streamlit Community Cloud](https://streamlit.io/cloud) from this repository, and the landing page is a separate Flask project deployed on Vercel.

## 👩‍💻 Author

**Mausami Chaudhari**

- GitHub: [@mausami10](https://github.com/mausami10)
- Repository: [virtualclass-AI_Attendance-main](https://github.com/mausami10/virtualclass-AI_Attendance-main)

---

⭐ If you like this project, consider giving the repository a star!