import requests
import argparse

def login(base_url, username, password):
    login_url = f'{base_url}/api/auth/login'
    login_headers = {
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
    }

    login_data = {
        'email': username,
        'password': password,
    }

    login_response = requests.post(login_url, headers=login_headers, json=login_data, verify=False)

    if login_response.status_code in (200, 201):
        print('Login successful')
        access_token = login_response.json().get('accessToken')
        return access_token
    else:
        print(f'Login failed with status code {login_response.status_code}')
        print(login_response.text)
        return None

def get_libraries(base_url, access_token):
    libraries_url = f'{base_url}/api/library'
    libraries_headers = {
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Cookie': f'immich_access_token={access_token}',
    }

    libraries_response = requests.get(libraries_url, headers=libraries_headers, verify=False)

    if libraries_response.status_code == 200:
        libraries = libraries_response.json()
        # Filter libraries with non-empty 'importPaths'
        filtered_libraries = [lib for lib in libraries if lib.get('importPaths')]
        return filtered_libraries
    else:
        print(f'Failed to retrieve libraries with status code {libraries_response.status_code}')
        print(libraries_response.text)
        return None

def initiate_scan(base_url, library_id, access_token):
    scan_url = f'{base_url}/api/library/{library_id}/scan'
    scan_headers = {
        'Accept': 'application/json, text/plain, */*',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': f'immich_access_token={access_token}',
    }

    scan_data = {}

    scan_response = requests.post(scan_url, headers=scan_headers, json=scan_data, verify=False)

    if scan_response.status_code in (200, 201):
        print(f'Scan initiation for library {library_id} successful')
        # Extract any necessary information from scan_response if needed
    else:
        print(f'Scan initiation for library {library_id} failed with status code {scan_response.status_code}')
        print(scan_response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Perform login, retrieve libraries, and initiate scan for each library with non-empty importPaths.')
    parser.add_argument('base_url', help='Base URL for the API')
    parser.add_argument('username', help='Username for authentication')
    parser.add_argument('password', help='Password for authentication')

    args = parser.parse_args()

    access_token = login(args.base_url, args.username, args.password)

    if access_token:
        libraries = get_libraries(args.base_url, access_token)

        if libraries:
            for library in libraries:
                library_id = library.get('id')
                initiate_scan(args.base_url, library_id, access_token)
