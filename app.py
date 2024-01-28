from flask import Flask, jsonify, request
import pytz
import requests
import datetime

app = Flask(__name__)
session_url = "cmr14egm4v65cu1alqt0xcq1u6bqfpre1.oast.fun"
full_url = f"https://{session_url}"


def convert_to_ist(server_time_str, server_timezone='UTC'):
    # Parse the server time string
    server_time = datetime.strptime(server_time_str, '%Y-%m-%d %H:%M:%S')
    server_time = pytz.timezone(server_timezone).localize(server_time)

    # Convert to IST timezone
    ist_time = server_time.astimezone(pytz.timezone('Asia/Kolkata'))
    return ist_time.strftime('%Y-%m-%d %H:%M:%S')

@app.route('/api/getURL', methods=['GET'])
def get_url():
    return jsonify({'url': full_url})

@app.route('/api/getInteractions', methods=['GET'])
def get_interactions():
    start_timestamp = request.args.get('start', None)
    end_timestamp = request.args.get('end', None)

    if start_timestamp:
        start_timestamp = convert_to_ist(start_timestamp)
    if end_timestamp:
        end_timestamp = convert_to_ist(end_timestamp)

    # Assuming 'interactions-endpoint' is a valid endpoint for interact.sh
    response = requests.get(f"{full_url}/interactions-endpoint", params={
        'start': start_timestamp,
        'end': end_timestamp
    })
    return response.text
    

if __name__ == '__main__':
    app.run(debug=True)
