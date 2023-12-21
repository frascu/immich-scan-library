# API Login and Scan Initiation Script

This script performs API login, retrieves a list of libraries with non-empty `importPaths`, and initiates a scan for each valid library.

## Usage

1. Install the required dependencies:

    ```bash
    pip install requests
    ```

2. Run the script from the command line, providing the necessary parameters:

    ```bash
    python script.py <base_url> <username> <password>
    ```

    Replace `<base_url>`, `<username>`, and `<password>` with your specific values.

## Script Parameters

- `base_url`: Base URL for the API.
- `username`: Username for authentication.
- `password`: Password for authentication.

## Features

- Performs API login with support for 200 and 201 status codes.
- Retrieves a list of libraries with non-empty `importPaths`.
- Initiates a scan for each valid library.

## Important Notes

- This script uses the `requests` library for HTTP requests.
- The `verify=False` argument is used to ignore SSL verification. Use it with caution and consider securing your connection appropriately.

## License

This script is licensed under the [MIT License](LICENSE).

Feel free to modify and use it according to your needs.

