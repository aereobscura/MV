let FL_motor = document.getElementById("FL_slider");
let FR_motor = document.getElementById("FR_slider");
let RL_motor = document.getElementById("RL_slider");
let RR_motor = document.getElementById("RR_slider");

let FL_speedometer = document.getElementById("FLspeedometer");
let FR_speedometer = document.getElementById("FRspeedometer");
let RL_speedometer = document.getElementById("RLspeedometer");
let RR_speedometer = document.getElementById("RRspeedometer");

let engage = document.getElementById("engage")

let motor_data = {
	FL: 0,
	FR: 0,
	RL: 0,
	RR: 0
};

FL_motor.addEventListener("mouseup", () => {
	
	FL_speedometer.innerHTML = FL_motor.value
	if (FL_motor.value < 0) {
		FL_speedometer.style.color = "red";
	} else if (FL_motor.value > 0){
		FL_speedometer.style.color = "green";
	} else {
		FL_speedometer.style.color = "gray";
	}
	motor_data.FL = Number(FL_motor.value);
	console.log(motor_data);
});

FR_motor.addEventListener("mouseup", () => {

	FR_speedometer.innerHTML = FR_motor.value
	if (FR_motor.value < 0) {
		FR_speedometer.style.color = "red";
	} else if (FR_motor.value > 0){
		FR_speedometer.style.color = "green";
	} else {
		FR_speedometer.style.color = "gray";
	}
	motor_data.FR = Number(FR_motor.value);
	console.log(motor_data);
});

RL_motor.addEventListener("mouseup", () => {
	
	RL_speedometer.innerHTML = RL_motor.value
	if (RL_motor.value < 0) {
		RL_speedometer.style.color = "red";
	} else if (RL_motor.value > 0){
		RL_speedometer.style.color = "green";
	} else {
		RL_speedometer.style.color = "gray";
	}
	motor_data.RL = Number(RL_motor.value);
	console.log(motor_data);
});

RR_motor.addEventListener("mouseup", () => {
	
	RR_speedometer.innerHTML = RR_motor.value
	if (RR_motor.value < 0) {
		RR_speedometer.style.color = "red";
	} else if (RR_motor.value > 0){
		RR_speedometer.style.color = "green";
	} else {
		RR_speedometer.style.color = "gray";
	}
	motor_data.RR = Number(RR_motor.value);
	console.log(motor_data);
});

engage.addEventListener("click", () => {


	var xml = new XMLHttpRequest();
	
	if ("192.168.1" == document.getElementById("pi_stream").src.slice(7, 16)) {
		xml.open("POST", "http://192.168.1.191:5000/mission_control/engage", true);
	} else {
		xml.open("POST", "http://99.121.229.178:5000/mission_control/engage", true);
	}

	xml.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	xml.onload = function(){
		var dataReply = this.responseText;
		console.log(dataReply);
		//parse json with JSON.parse()
		//var parsedData = JSON.parse(dataReply);
		
	};

	xml.send(JSON.stringify(motor_data));
	console.log(JSON.stringify(motor_data));
});

