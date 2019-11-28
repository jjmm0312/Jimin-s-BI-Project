#import dprocess
import recommendation
from flask import Flask, request, jsonify,send_file,render_template
import json

app = Flask(__name__)
NEWS_DATA= []


@app.route('/main')
def ClockPage():
    return render_template('index.html')

@app.route('/jimin') 
def returnJimin():
    filename = 'Jimin.jpg'
    return send_file(filename,mimetype='image/jpg')

# recommend with 30 latest news history
@app.route('/i_recommend', methods=['POST'])
def implicit_recommend():
    history = []
    if request.method == 'POST':
        dataJson = request.get_json()
        #   print(dataJson)
        for line in dataJson:
            tmp = json.dumps(line)
            #print(tmp)
            history.append(json.loads(tmp))


    result = recommendation.i_recommend(history, NEWS_DATA)
    resultJson = json.dumps(result)

    return resultJson

# recommend with 3 priority
@app.route('/e_recommend', methods=['POST'])
def explicit_recommend():
    priority = []
    if request.method == 'POST':
        dataJson = request.get_json()
        #print(dataJson)
        #print(type(dataJson))
        for line in dataJson:
            #print(type(line))
            tmp = json.dumps(line)
            #print(type(tmp))
            priority.append(json.loads(tmp))


    result = recommendation.e_recommend(priority, NEWS_DATA)
    resultJson = json.dumps(result)
    return resultJson

if __name__ == "__main__":

    # receive News Data
    print('i am okay')
    fname = 'new_list.json'

    with open(fname, "r") as st_json:
        NEWS_DATA = json.load(st_json)

    for i in range (len(NEWS_DATA)):
        NEWS_DATA[i]['index'] = i

    #print(NEWS_DATA[0])
    '''
    with open(fname) as st_json:
        for line in st_json:
            NEWS_DATA.append(json.loads(line))
    '''

    print('total news count : ' + str(len(NEWS_DATA)))
    print('data load finish\n\n')

    app.run(host="0.0.0.0",port="8080")
