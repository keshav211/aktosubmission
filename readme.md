
# Flask Wrapper for interact.sh

This Flask application serves as a wrapper for `interact.sh`, providing a simple API to interact with the system. It includes two main endpoints: `api/getURL` and `api/getInteractions`.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher installed.
- Docker installed (for Dockerization).
- Basic understanding of Python and Flask.
- Go (Golang) environment set up, as `interact.sh` is a Go-based application.
- An instance of `interact.sh` running (adjust the URLs in the code accordingly).

## Running interact.sh

To run interact.sh, you can use the following command:

```bash
./interactsh-server
```

This will start the interact.sh server. Make note of the output, especially the server URL, as you'll need this for your Flask application.

## Installation and Setup

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/keshav211/aktosubmission.git

   ```

2. **Install Dependencies**

   Install the necessary Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuration**

   Update the `INTERACTSH_BASE_URL` in `app.py` to point to your instance of `interact.sh`.

## Running the Flask Application

Copy the address generated from the interact.sh terminal into the URL part in the Flask app.

Run the application directly on your machine:

```bash
python app.py
```

The application will start on `http://localhost:5000`.

## Dockerization

To run the application as a Docker container:

1. **Build the Docker Image**

   ```bash
   docker build -t my-flask-app .
   ```

2. **Run the Docker Container**

   ```bash
   docker run -p 5000:5000 my-flask-app
   ```

Now, the application is accessible at `http://localhost:5000`.

## API Endpoints

1. **GET `/api/getURL`**
   
   Returns the URL of the testing server being used for the current session in interact.sh.

2. **GET `/api/getInteractions`**
   
   Takes the URL of the testing server and returns information about its interactions. Optional timestamp limits can be provided.
