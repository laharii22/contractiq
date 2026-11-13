#ContractIQ

ContractIQ is my final-year university project. The aim is to develop an AI-powered application that helps users understand legal contracts by identifying important information, risky clauses and possible inconsistencies.

The project is currently in its early development stage. So far, I have implemented PDF text extraction and connected the application to Claude AI to generate simple contract summaries.

#Work Completed

- Created the Python project structure.
- Added a function to extract text from PDF contracts.
- Connected Claude using the Anthropic API.
- Used a `.env` file to store the API key securely.
- Added error handling for common API problems.
- Connected PDF extraction with Claude to generate contract summaries.
- Added automated tests using pytest and mocking.
- Used Git branches and pull requests to manage project changes.

#Development Work

I started by creating the project structure and developing a function to extract text from PDF files using pypdf. After testing the extraction, I connected Claude through the Anthropic API and stored the API key in a `.env` file. I then created a pipeline that takes the extracted contract text and sends it to Claude for summarisation. I also added error handling and automated tests using pytest to check that the functions work correctly. Finally, I tested the application using a sample service agreement and uploaded the changes to GitHub through a feature branch and pull request.

#Technologies Used

- **Python:** Used to develop the application.
- **pypdf:** Helps in extracting text from PDF contracts.
- **Anthropic API:** Used to send contract text to Claude for analysis.
- **python-dotenv:** Helps in loading the API key from the `.env` file.
- **pytest:** Used to test the Python functions.
- **Git and GitHub:** Used to track changes and manage project development.

#How to Run

Install the required packages:

In powershell
python -m pip install -r requirements-dev.txt


Create a `.env` file in the main project folder and add your Anthropic API key:

text:
ANTHROPIC_API_KEY=your_api_key


Run the contract analysis:

powershell:
$env:PYTHONPATH = "src"
python -c "from contractiq.pipeline import analyse_pdf; print(analyse_pdf('data/samples/sample_contract.pdf'))"

Run the automated tests:

powershell:
python -m pytest -v

# Current Limitations

- The application currently works with PDFs containing readable text.
- Scanned PDF support has not been added yet.
- Contract risk detection and inconsistency checking are still under development.
- AI-generated summaries may contain mistakes and should not be treated as legal advice.

# Next Steps

The next stage is to improve contract processing, identify individual clauses and develop features to detect potentially risky terms and inconsistencies.
