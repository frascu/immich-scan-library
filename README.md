# Script for API Login and Scan Initiation

This script performs a login request and initiates a scan using a provided API.

## Usage

1. Install the required dependencies:

    ```bash
    pip install requests
    ```

2. Run the script from the command line, providing the necessary parameters:

    ```bash
    python script.py <base_url> <username> <password> <library_id>
    ```

    Replace `<base_url>`, `<username>`, `<password>`, and `<library_id>` with your specific values.

## Script Parameters

- `base_url`: Base URL for the API.
- `username`: Username for authentication.
- `password`: Password for authentication.
- `library_id`: Library ID for scan initiation.

## Features

- Performs API login and scan initiation.
- Supports command-line arguments for easy execution.

## Important Note

- This script uses the `requests` library for HTTP requests.
- The `verify=False` argument is used to ignore SSL verification. Use it with caution and consider securing your connection appropriately.

## License

This script is licensed under the [MIT License](LICENSE).

Feel free to modify and use it according to your needs.

