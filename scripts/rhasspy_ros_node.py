#!/usr/bin/env python
import rospy
from rhasspy_ros_interface.msg import Intent
from flask import Flask, request
import flask.json
import threading
import os

app = Flask(__name__)

pub = rospy.Publisher('speech_intent', Intent, queue_size=10)

@app.route('/rhasspy_intent', methods=['GET', 'POST'])
def hello_world():

    if request.is_json:
        json = request.get_json()
        print("Request: " + str(json))

        intent = json['intent']['name']
        slots = json['slots'].keys()
        values = json['slots'].values()

        msg = Intent()
        msg.intent = intent
        msg.slots = slots
        msg.values = values

        pub.publish(msg)

        response_text = "OK"
    else:
        response_text = "I could not parse the command"


    response = app.response_class(
        response=flask.json.dumps({
          #"speech": {
          #  "text": response_text
          #}
        }),
        status=200,
        mimetype='application/json'
    )
    return response

def run_flask_server():
    app.run(host="0.0.0.0", port=1337)

def main():
    rospy.init_node('rhasspy_listener_node', anonymous=True)

    # start flask in separate thread and set it to daemon such that program doesn't wait for it on exit
    t = threading.Thread(target=run_flask_server)
    t.setDaemon(True)
    t.start()

    rospy.spin()

if __name__ == '__main__':
    main()

