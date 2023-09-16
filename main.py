from flask import Flask, render_template, request, redirect, url_for, flash, session
import csv

# Create app
app = Flask(__name__)

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

# Submit
@app.route('/submit.html', methods=['GET', 'POST'])
def submit():
    print(f"got request via {request.method}")
    if request.method == 'POST':
        # print the data recieved from the form
        #for key, value in request.form.items():
            #print(f"{key}: {value}")

        print(request.form.to_dict())

        # append data to data/scout.csv
        with open('data/scout.csv', 'a') as f:
            writer = csv.DictWriter(f, fieldnames=[
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

        return redirect(url_for('submit'))



            
    return render_template('submit.html')

# Run app  
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)