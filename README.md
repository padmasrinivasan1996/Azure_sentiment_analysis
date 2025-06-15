# Azure_sentiment_analysis
This project is a simple web application built using **Python Flask** and **HTML**, integrated with **Azure language services** to analyze user-input sentiment. It allows users to enter text and receive sentiment analysis results, determining whether the text conveys **positive, negative, or neutral** emotions.

 **Features** 
✔️ Sentiment analysis using Azure API  
✔️ Flask-based web app for easy user interaction  
✔️ HTML frontend with a simple input form  
✔️ Environment variables for secure API key handling  

## **Tech Stack**  
- **Programming Language:** Python  
- **Framework:** Flask  
- **Cloud Service:** Azure language Services  
- **Frontend:** HTML, CSS  

## **Setup & Installation**  
Follow these steps to set up and run the project:  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/padmasrinivasan1996/Azure_sentiment_analysis

2. **Create a Virtual Environment:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # (Mac/Linux)
   venv\Scripts\activate     # (Windows)
   ```

3. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables:**  
   Create a `.env` file and add your Azure API credentials:  
   ```
   AZURE_KEY=your-azure-api-key
   ENDPOINT=your-azure-endpoint
   ```

5. **Run the Application:**  
   ```bash
   flask run
   ```
   The app will start at **http://127.0.0.1:5000/**  

## **Project Structure**  
```
/project-directory
│── app.py             # Flask application
│── templates/
│   ├── index.html     # Frontend page
│── .env               # Environment variables (not included in GitHub)
│── requirements.txt   # Python dependencies
│── README.md          # Project documentation
```

OUTPUT
This is the screenshots of the output 
![Sentiment output](https://github.com/user-attachments/assets/629106a7-4160-4ef8-a090-633a640cf5bf)

![output2](https://github.com/user-attachments/assets/62902e9b-f3bb-46a4-b6d3-57dee067a4d3)

## **Future Enhancements**  
🚀 Add database support for storing user inputs  
🚀 Implement a more advanced sentiment analysis model  
🚀 Deploy the app on a cloud platform
