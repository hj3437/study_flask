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
def showStore():
    stores = session.query(Store).all()
    return render_template('store.html', stores=stores)


@app.route('/store/new', methods=['GET', 'POST'])
def newStore():
    if request.method == 'POST':
        newStore = Store(name=request.form['name'])
        session.add(newStore)
        session.commit()
        return redirect(url_for('showStore'))
    else:
        return render_template('newStore.html')


@app.route('/store/<int:store_id>/')
@app.route('/store/<int:store_id>/menu')
def showMenu(store_id):
    print('show store_id : ', store_id)
    store = session.query(Store).filter_by(id=store_id).one()
    menus = session.query(StoreItem).filter_by(store_id=store_id).all()
    return render_template('store_menu.html', store=store, menus=menus)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5151)
