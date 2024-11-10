# Text-to-SQL
 Text to SQL LLM App along with Quering SQL database using Gemini Pro
 # Gemini SQL Query Assistant

This project provides an interface to generate SQL queries using natural language processing (NLP) and retrieve corresponding data from an SQLite database. The application utilizes Google's Gemini AI model to convert user input into SQL queries, executes them on an SQLite database, and displays the results in a simple Streamlit web application.

## Features

- **Database Interaction**: The app interacts with an SQLite database (`student.db`) that contains a `STUDENT` table.
- **SQL Query Generation**: The app uses Google's Gemini AI model to convert natural language questions into SQL queries.
- **Streamlit Interface**: A user-friendly interface for interacting with the database and querying data.
- **Environment Variables**: API key for Google Gemini AI is loaded using environment variables.

## Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.10 or later 
- pip (Python package installer)

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes:
   - `streamlit`
   - `sqlite3`
   - `google-generativeai`
   - `python-dotenv`

3. Set up your environment variables:
   
   Create a `.env` file in the root directory of the project and add your **Google API key**:
   ```bash
   GOOGLE_API_KEY=your-google-api-key
   ```

4. Create the SQLite database:
   - The database `student.db` is used to store student information. It includes a table named `STUDENT` with the following columns: `NAME`, `CLASS`, `SECTION`, `MARKS`.
   - The database and sample data can be created by running the script `create_database.py`.

## Database Schema

The database consists of a `STUDENT` table with the following columns:
- `NAME` (VARCHAR(25)): The student's name.
- `CLASS` (VARCHAR(25)): The class the student is enrolled in.
- `SECTION` (VARCHAR(25)): The section of the class.
- `MARKS` (INT): The student's marks.

### Sample Data

The database is populated with sample records:

| NAME      | CLASS         | SECTION | MARKS |
|-----------|---------------|---------|-------|
| Krish     | Data Science  | A       | 90    |
| Sudhanshu | Data Science  | B       | 100   |
| Darius    | Data Science  | A       | 86    |
| Vikash    | DEVOPS        | A       | 50    |
| Dipesh    | DEVOPS        | A       | 35    |

## Running the Application

1. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open the app in your browser (usually accessible at `http://localhost:8501`).

3. Enter a natural language question related to the `STUDENT` table in the input box. For example:
   - "How many students are there?"
   - "Tell me all students in Data Science class."
   - "What are the marks of Krish?"

4. Click **Ask the question** to generate and run the SQL query. The results from the database will be displayed.

## How it Works

- The user inputs a natural language question in the Streamlit interface.
- The app sends the question to the Gemini AI model, which converts it into a corresponding SQL query.
- The SQL query is executed against the `student.db` SQLite database.
- The app retrieves and displays the results on the web interface.

## Technologies Used

- **Google Gemini AI**: For natural language to SQL query translation.
- **SQLite**: Lightweight database for storing student records.
- **Streamlit**: Web framework for building the interactive UI.
- **python-dotenv**: For securely managing environment variables.

## Example Questions

- "How many students are in the Data Science class?"
- "Who scored more than 80 marks?"
- "List all students in section A of the DEVOPS class."




**Note**: Make sure you have a valid API key for Google Gemini AI and the required Python libraries installed. You can obtain an API key by following the [Google Cloud API documentation](https://cloud.google.com/docs/authentication/api-keys).


 Key Points 

- The repository is designed to query a SQLite database (`student.db`) using natural language.
- The application leverages Google Gemini's AI model to generate SQL queries from user input.
- The app is built using **Streamlit**, a framework for building interactive web applications.
- Instructions are provided for setting up the environment, running the app, and using the API key.
- Example questions and features help users understand how to interact with the app.

Let me know if you need additional modifications!

## Contributing

Feel free to fork the repository and create a pull request. Contributions are welcome!
