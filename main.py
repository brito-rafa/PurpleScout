# Import Flask application
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, send, emit
import csv

# Create app
app = Flask(__name__)
socketio = SocketIO(app)

# Index
@app.route('/')
def index():
    return render_template('home.html')

# Home
@app.route('/home.html')
def home():
    return render_template('home.html')

# Scout
@app.route('/scout.html')
def scout():
    return render_template('scout.html')

# Super scout
@app.route('/superScout.html')
def superScout():
    return render_template('superScout.html')

# Submit
@app.route('/submit.html', methods=['GET', 'POST'])
def submit():
    print(f"got request via {request.method}")
    if request.method == 'POST':

        print(request.form.to_dict())

        # append data to data/scout.csv
        with open('data/scout.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=[
                "matchNum",
                "teamNum",
                "auto-high-cones",
                "auto-high-cubes",
                "auto-mid-cones",
                "auto-mid-cubes",
                "auto-low-cones",
                "auto-low-cubes",
                "teleop-high-cones",
                "teleop-high-cubes",
                "teleop-mid-cones",
                "teleop-mid-cubes",
                "teleop-low-cones",
                "teleop-low-cubes",
                "defense",
                "sub",
                "dropped-pieces",
                "info"
            ])
            writer.writerow(request.form.to_dict())

            f.close()

        # tell the super scout that a scout has submitted
        #print(request.form.to_dict()['teamNum'])
        socketio.emit('scoutSubmit', request.form.to_dict())

        return redirect(url_for('submit'))



            
    return render_template('submit.html')

# Super scout submit
@app.route('/submit2.html', methods=['GET', 'POST'])
def submit2():
    print(f"got request via {request.method}")
    if request.method == 'POST':
        # print the data recieved from the form
        for key, value in request.form.items():
            print(f"{key}: {value}")

        print(request.form.to_dict())

        # append data to data/scout.csv
        with open('data/superScout.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=[
                "matchNum",
                "num1red",
                "num1blue",
                "num2red",
                "num2blue",
                "num3red",
                "num3blue",
                "info"
            ])
            writer.writerow(request.form.to_dict())

            f.close()

        return redirect(url_for('submit2'))



            
    return render_template('submit2.html')


#### Socket routes ####
@socketio.on('echo') # test route
def handle_echo(data):
    print(f"received echo: {data}")
    emit('echo', data)


@socketio.on('getTeams') # activated when the super scout clicks the button to fetch teams
def handle_fetchTeams(data):
    # read data from data/teams.csv into a dictionary
    matchNum = data['matchNum']
    # get line of matchNum
    with open('data/teams.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['matchNum'] == matchNum:
                # send data to super scout
                emit('sendTeams', row)
                return
            
    # if no matchNum found, send error
    emit('sendTeams', {'red1': 'error', 'red2': 'error', 'red3': 'error', 'blue1': 'error', 'blue2': 'error', 'blue3': 'error'})


# Both these routes bounce the data back to all the clients
@socketio.on('scoutSelect') # activated when a scout chooses their team (red/blue and number)
def handle_scoutSelect(data):
    print(f"received scoutSelect: {data}")
    emit('scoutSelect', data, broadcast=True)

@socketio.on('scoutAssign') # activated when the super scout assigns the team# to scouts
def handle_scoutAssign(data):
    print(f"received scoutAssign: {data}")
    emit('scoutAssign', data, broadcast=True)


# Run app  
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)