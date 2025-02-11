from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint

app = Flask(__name__)

# Anslutning till PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Examensarbete2025@localhost/loganalyzer'

db = SQLAlchemy(app)

# Definierar modellen för logs-tabellen och AnalysisResults-tabellen
class logs(db.Model):
    __tablename__ = 'logs'
    log_id = db.Column(db.Integer, primary_key=True)  
    ip = db.Column(db.String(255))
    country = db.Column(db.String(255))
    city = db.Column(db.String(255))
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    device = db.Column(db.String(255))
    os = db.Column(db.String(255))
    browser = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime)  
    original_source = db.Column(db.String(255))
    log_type = db.Column(db.String(255))
    log_message = db.Column(db.Text)

class analysis_results(db.Model):
    __tablename__ = 'analysis_results'
    analysis_id = db.Column(db.Integer, primary_key=True)
    log_id = db.Column(db.Integer, db.ForeignKey('logs.log_id'), nullable=False)
    threat_level = db.Column(db.Integer, nullable=False)
    risk_description = db.Column(db.Text, nullable=False)

    __table_args__ = (
        CheckConstraint('threat_level BETWEEN 1 AND 10', name='check_threat_level'),
    )

# Route för dashboard startsidan
@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5001, debug=True)
