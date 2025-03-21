# R1 API consultations with OpenAI

This project uses Python to consult the API of R1 using the OpenAI bookstore. The objective is to send a specific prompt and obtain an answer processed by the API.

## Requirements

- Python 3.7 or higher
- Account and credentials of access to the API of R1 "https://openrouter.ai/settings/keys"

OpenAI API Key

## Installation and setup

1. Clone this repository in your local machine:
    `` Bash
    git clone https://github.com/L50E02O/BotApiR1.git
    ``
2. Install the necessary Python packages (make a venv "python -m venv namevenv" then activate it) and then in the terminal type `pip install -r requirements.txt`

## Use
1. Configure your R1 and OpenAi API credentials in an `.env`:
    ``
    R1_api_Key = tu_clave_de_api_r1
    ``
2. Execute the main script:
    `` Bash
    Python BotApi.py
    ``
3. Enter the prompt that you want to send to the API when asked.

## Project structure

-
`BotApi.py`: Main script that handles the consultations to the API.
- `requirements.txt`: Archive with the project units.
- `.Env`: Archive to store API keys safely.

## Contributions

Contributions are welcome. Please open an ISSUE or a pull requires to discuss any change you want to make.

## License

This project is licensed under the MIT license. Check the `License` file for more details.