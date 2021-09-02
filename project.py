from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Store, Base, StoreItem

app = Flask(__name__)

engine = create_engine('sqlite:///store.db', connect_args={'check_same_thread': False})
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/store/JSON')
def storesJSON():
    stores = session.query(Store).all()
    return jsonify(Store=[i.serialize for i in stores])

@app.route('/store/<int:store_id>/menu/JSON')
def storeMenuJSON(store_id):
    store = session.query(Store).filter_by(id=store_id).one()
    items = session.query(StoreItem).filter_by(
        store_id=store_id).all()
    return jsonify(StoreItem=[i.serialize for i in items])


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


@app.route('/store/<int:store_id>/edit', methods=['GET', 'POST'])
def editStore(store_id):
    editedStore = session.query(Store).filter_by(id=store_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedStore.name = request.form['name']
            session.add(editedStore)
            session.commit()
        return redirect(url_for('showStore'))
    else:
        return render_template('editStore.html', store=editedStore)


@app.route('/store/<int:store_id>/delete', methods=['GET', 'POST'])
def deleteStore(store_id):
    storeToDelete = session.query(Store).filter_by(id=store_id).one()
    if request.method == 'POST':
        print('store_id', store_id)
        session.delete(storeToDelete)
        session.commit()
        return redirect(url_for('showStore'))
    else:
        return render_template('deleteStore.html', store=storeToDelete)


@app.route('/store/<int:store_id>/')
@app.route('/store/<int:store_id>/menu')
def showMenu(store_id):
    print('show store_id : ', store_id)
    store = session.query(Store).filter_by(id=store_id).one()
    menus = session.query(StoreItem).filter_by(store_id=store_id).all()
    return render_template('store_menu.html', store=store, menus=menus)


@app.route('/store/<int:store_id>/menu/new/', methods=['GET', 'POST'])
def newItem(store_id):
    if request.method == 'POST':
        if request.form['name'] and request.form['description'] \
                and request.form['price'] and request.form['package_item']:
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            package_item = request.form['package_item']

            newItem = StoreItem(name=name, description=description, price=price, package_item=package_item,
                                store_id=store_id)
            session.add(newItem)
            session.commit()

        return redirect(url_for('showMenu', store_id=store_id))
    else:
        return render_template('newmenuitem.html', store_id=store_id)


@app.route('/store/<int:store_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def editItem(store_id, menu_id):
    editedItem = session.query(StoreItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['package_item']:
            editedItem.package_item = request.form['package_item']
        session.add(editedItem)
        session.commit()
        return redirect(url_for('showMenu', store_id=store_id))
    else:
        return render_template('editmenuitem.html', store_id=store_id, menu_id=menu_id, item=editedItem)


@app.route('/store/<int:store_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteItem(store_id, menu_id):
    itemToDelete = session.query(StoreItem).filter_by(id=menu_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showMenu', store_id=store_id))
    else:
        return render_template('deletemenuitem.html', item=itemToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5151)
