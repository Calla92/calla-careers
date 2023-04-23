from flask import Flask,render_template,jsonify

app= Flask(__name__)

JOBS=[
    {
    "id":1,
    "title": "Data Analyst",
    "location": "Dodoma, Tanzania",
    "salary": "TZS 1,000,000"
    },
     {
    "id":2,
    "title": "Frontend Engineer",
    "location": "Arusha, Tanzania",
    "salary": "TZS 2,000,000"
    },
     {
    "id":32,
    "title": "Software Engineer",
    "location": "Mwanza, Tanzania",
    
    }
]


@app.route('/')
def home():
    return render_template('home.html',jobs=JOBS)

@app.route('/jobs')
def list_jobs():
    return jsonify(JOBS)



if __name__==('__main__'):
    app.run(debug=True)