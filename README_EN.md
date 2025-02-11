# Flask Chat Application

This project provides a chat interface using Flask and OpenAI's API. Users can send messages and receive AI-generated responses.

## Features
- Flask-based API
- OpenAI API integration
- Dynamic chat interface
- Copyable code blocks

## Installation

### Requirements
- Python 3.x
- Flask
- OpenAI library
- Dotenv

### Steps
1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Create a `.env` file and add your NVIDIA API key:
   ```ini
   NVIDIA_API_KEY=your_api_key_here
   ```
5. Run the application:
   ```sh
   python app.py
   ```
6. Open in your browser: `http://127.0.0.1:5000`

## Usage
- Type your message in the chat box and send it.
- Responses are displayed in a structured format, and code blocks are copyable.

## Contributing
Pull requests are welcome. Please open an issue to discuss changes before making modifications.

## License
This project is licensed under the MIT License.

## Acknowledgements
- [Flask](https://flask.palletsprojects.com/)