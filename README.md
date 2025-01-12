Car Maintenance Chatbot
Project Overview
The "Car Maintenance Chatbot" is an intelligent assistant designed to guide users in diagnosing and resolving car-related issues. This AI-powered chatbot provides mechanics and car owners with detailed troubleshooting steps, explanations of symptoms, potential causes, and solutions, making car maintenance more accessible and efficient.

Group Members:
Muhammad Zeb (21PWBCS0877)
Saad Ahmad (21PWBCS0876)
Features:
User -Friendly Interface: Built with TypeScript/JavaScript using React and Next.js to ensure a smooth and intuitive user experience.
AI-Powered Responses: Backend powered by Python, leveraging LangChain and OpenAI for accurate and context-aware guidance.
Comprehensive Database: Covers a wide range of car issues, symptoms, and solutions for various car models.
Searchable Troubleshooting History: Stores chat history in MongoDB for quick access and retrieval of past interactions.
Tailored Recommendations: Provides personalized suggestions based on specific car models and user queries.
Voice Interaction: Allows users to interact using voice commands for hands-free troubleshooting.
Technology Stack
Frontend: Built with TypeScript/JavaScript using React and Next.js.
Backend: Python (chatbot logic using LangChain, OpenAI API, and ChromaDB).
Database: MongoDB (for chat history and user preference storage).
Getting Started
Clone the Repository:
bash

Verify

Open In Editor
Run
Copy code
git clone <repository-url>
Install Dependencies:
For the Frontend:

bash

Verify

Open In Editor
Run
Copy code
npm install
For the Backend (Python):

bash

Verify

Open In Editor
Run
Copy code
pip install -r requirements.txt
Set Up Environment Variables:
Create a .env file in the backend directory with the following variables:

makefile

Verify

Open In Editor
Run
Copy code
OPENAI_API_KEY=<your_openai_api_key>
Start the Backend Server:
bash

Verify

Open In Editor
Run
Copy code
python chatbot.py
Run the Frontend Application:
bash

Verify

Open In Editor
Run
Copy code
npm run dev
Future Enhancements:
Integration with OBD-II Systems: Directly fetch real-time diagnostics from car sensors.
Multilingual Support: Provide guidance in multiple languages for a diverse audience.
Cloud Sync: Save user preferences and history to the cloud for cross-device access.
Advanced AI Models: Incorporate fine-tuned domain-specific models for improved accuracy.
Offline Mode: Enable limited functionality without an active internet connection.
Maintenance Scheduling: Notify users about upcoming car services based on mileage and usage patterns.
