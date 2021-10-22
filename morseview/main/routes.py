import os
from flask import (render_template, request, url_for, redirect,
	Blueprint, jsonify)
from morseview.models import Post
#from morseview.users.forms import MorseviewInterface
from morseview.scripts.MVScripts import (ManeuverInitialize,
	ManeuverForward, ManeuverReverse, executeManeuver)

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
	page = request.args.get("page", 1, type=int)
	posts = Post.query.order_by(Post.date_posted.desc())\
		.paginate(page=page, per_page=5)
	return render_template("home.html", posts=posts)


@main.route('/about')
def about():
	return render_template("about.html", title="About")


@main.route('/mission_control', methods=["GET", "POST"])
def mission_control():
	
	client_ip = request.remote_addr
	
	if "192.168.1." in client_ip:
		video_src = "http://192.168.1.191:8081"
	else:
		video_src = "http://99.121.229.178:8081"

	
	"""
	form = MorseviewInterface()

	if form.validate_on_submit():
		
		which_motors = []
		motor_speed = str(form.delay_t.data)
		delay_t = form.delay_t.data / float(1000)
		rotations = round(form.rotations.data * float(512))
		
		if form.FL_motor.data == True:
			which_motors.append(MI[0][0])
		if form.FR_motor.data == True:
			which_motors.append(MI[0][1])
		if form.RL_motor.data == True:
			which_motors.append(MI[0][2])
		if form.RR_motor.data == True:
			which_motors.append(MI[0][3])
		
		if form.maneuver.data == "Forward":
			ManeuverForward(which_motors, motor_speed, delay_t, MI[1], rotations)
		if form.maneuver.data == "Reverse":
			ManeuverReverse(which_motors, motor_speed, delay_t, MI[1], rotations)

	"""

	
	return (render_template("mission_control.html", title="Mission Control",
		legend="CONTROL MORSEVIEW", v_src=video_src))

@main.route("/mission_control/engage", methods= ["GET", "POST"])
def engage():

	dataGet = request.get_json(force=True)
	motor_data = dict(dataGet)

	##MI = ManeuverInitialize()

	executeManeuver(motor_data)


	#print(str(motor_data["FL"]) + " " + str(motor_data["FR"]))
	#for JSON data
	#dataReply = {'this':'that', 'then':'there'}
	#jsonify(dataReply)
	return "engage command recieved" 
