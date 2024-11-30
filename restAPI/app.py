from flask import Flask, jsonify

app=Flask(__name__)
names=[{'name':'arash'},
      {'name':'reza'},
      {'name':'fateme'},
      {'name':'ali'}
     ]
@app.route('/api/v1/name')
def dataview():
    return jsonify(names)
@app.route('/api/v1/name/<name>')
def dataviews(name):
    mylist=[]
    for i in names:
        if i['name']==name:
            mylist.append(i)
            return jsonify(mylist)
@app.route('/api/v1/name/insertdata')
def insertdata():
    names.append({'name':'arian'})
    return jsonify({'message':'succsessfully added'})

app.run()