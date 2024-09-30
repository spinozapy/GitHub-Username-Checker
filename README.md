# GitHub Username Checker

**GitHub Username Checker** is a Python tool that allows you to check the availability of GitHub usernames based on user-defined length. The tool generates random usernames and checks them against GitHub, logging available usernames in a timestamped format.

## Requirements

- Python 3.x
- `requests` library (Install using `pip install requests`)
- `colorama` library (Install using `pip install colorama`)

## Installation

1. Clone the repository.
2. Install the required libraries.
3. Run the tool:

    ```bash
    python main.py
    ```

## Usage

1. Start the GitHub Username Checker:

    ```bash
    python main.py
    ```

2. Enter the desired length for the usernames when prompted (minimum length is 3 characters).

3. The tool will continuously generate random usernames and check their availability on GitHub.

4. Available usernames will be logged in the `available-usernames.txt` file with a timestamp.

## Features

- **Username Length Customization:** Users can specify the length of usernames to be generated.
- **Availability Checking:** The tool checks the availability of randomly generated usernames in real-time.
- **Logging:** Available usernames are saved in a dedicated text file with timestamps for easy tracking.
- **Clear Terminal Interface:** The tool provides a clear and colorful terminal interface using `colorama`.

## Example

```bash
[GitHub-Username]: How long should the usernames be? (minimum 3)
root@you:~$ 7

[GitHub-Username]: Press Enter to stop the process.
[GitHub-Username]: Available usernames are being saved to available-usernames.txt

[GitHub-Username] Username Available: sp1n0za
[GitHub-Username] Username Available: r00t5pn
...
```

## Notes

- Ensure to handle GitHub's rate limiting to avoid being blocked.
- Use a valid internet connection while running the tool.

