
from pydoc import describe
from flask import Flask, render_template, request, flash, redirect, url_for
from logging import debug
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:24465336Kotiki@localhost:5432/birds'
app.config['SECRET_KEY'] = '\xae\x8c\x1e\xb9;\x193L\x90g\xd0\xffU\x95\xaej\xabE\x84B\xccK\x19\xe7'
db = SQLAlchemy(app)


class Bird(db.Model):
    __tablename__ = 'birds'
    bird_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=255))


class Feature(db.Model):
    __tablename__ = 'features'

    feature_id = db.Column(db.Integer, primary_key=True)
    bird_id = db.Column(db.Integer, db.ForeignKey('birds.bird_id'))
    feature = db.Column(db.String(length=400))

    bird = db.relationship('Bird', backref='bird')


@app.route("/")
def display_birds():
    return render_template('home.html', birds=Bird.query.all())


@app.route('/bird/<bird_id>')
def display_features(bird_id):
    return render_template('bird-feature.html', birds=Bird.query.filter_by(bird_id=bird_id).first(), features=Feature.query.filter_by(bird_id=bird_id).all())


@app.route("/add/bird", methods=['POST'])
def add_bird():
    if not request.form['bird-name']:
        flash('Enter a name of a bird', 'tomato')
    else:
        bird = Bird(name=request.form['bird-name'])
        db.session.add(bird)
        db.session.commit()
        flash('Bird Added Succesfully', 'lawngreen')

    return redirect(url_for('display_birds'))


@app.route('/add/feature/<bird_id>', methods=['POST'])
def add_feature(bird_id):
    if not request.form['feature-description']:
        flash('Enter new observations or facts', 'tomato')
    else:
        feature = Feature(
            feature=request.form['feature-description'], bird_id=bird_id)
        db.session.add(feature)
        db.session.commit()
        flash('Notes Added Succesfully', 'lawgreen')
    return redirect(url_for('display_features', bird_id=bird_id))


@app.route('/delete/feature/<feature_id>', methods=['POST'])
def delete_feature(feature_id):
    pendeing_delete_feature = Feature.query.filter_by(
        feature_id=feature_id).first()
    target_feature_id = pendeing_delete_feature.bird.bird_id
    db.session.delete(pendeing_delete_feature)
    db.session.commit()
    return redirect(url_for('display_features', bird_id=target_feature_id))


@app.route('/delete/bird/<bird_id>', methods=['POST'])
def delete_bird(bird_id):
    pending_delete_bird = Bird.query.filter_by(bird_id=bird_id).first()
    db.session.delete(pending_delete_bird)
    db.session.commit()
    return redirect(url_for('display_birds'))


if __name__ == "__main__":
    app.run(debug=True)
