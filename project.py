from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Store, Base, StoreItem

app = Flask(__name__)

engine = create_engine('sqlite:///store.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/store/')
def mainMenu():
    stores = session.query(Store).all()
    return render_template('store.html', stores=stores)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5151)
