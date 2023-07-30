# dominant-color

This API provides a service for detecting the dominant color of a webpage from a given URL. It utilizes Docker for easy deployment and testing. Before using the API, make sure you have Docker installed on your system.

# Setup
1. Install Docker on your machine.
2. Clone the repository and navigate to its directory.
3. Build the application by running the `build_app.sh` script.
4. Start the API server with the `run_app.sh` script.

# How to use
You can use any API client like Postman or simply your web browser to test the API. Send a GET request to the following endpoint:

`GET http://127.0.0.1:8000/api/colors/dominant_color?url=<url>`

# Additional Information
For more information on how the API works or to explore the available endpoints, you can visit /api/docs once the API server is running. This will provide you with an interactive documentation that details each endpoint and its usage.

