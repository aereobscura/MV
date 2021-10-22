from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, FloatField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from morseview.models import User


class RegistrationForm(FlaskForm):
	username = StringField("Username", 
		validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("Email",
		validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField("Confirm Password",
		validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Sign Up")

	def validate_username(self, username):

		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError("Username is already taken. Please choose another")

	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError("Email is already taken. Please choose another")

class LoginForm(FlaskForm):
	email = StringField("Email",
		validators=[DataRequired(), Email()])
	password = PasswordField("Password", validators=[DataRequired()])
	remember = BooleanField("Remember Me")
	submit = SubmitField("Login")

	
class UpdateAccountForm(FlaskForm):
	username = StringField("Username", 
		validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField("Email",
		validators=[DataRequired(), Email()])
	picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "jpeg", "png"])])
	submit = SubmitField("Update")

	def validate_username(self, username):

		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError("Username is already taken. Please choose another")

	def validate_email(self, email):

		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError("Email is already taken. Please choose another")

class RequestResetForm(FlaskForm):
	email = StringField("Email",
		validators=[DataRequired(), Email()])
	submit = SubmitField("Request Password Reset")

	def validate_email(self, email):

		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError("There is no account for that email. You must register first.")

class ResetPasswordForm(FlaskForm):
	password = PasswordField("Password", validators=[DataRequired()])
	confirm_password = PasswordField("Confirm Password",
		validators=[DataRequired(), EqualTo("password")])
	submit = SubmitField("Reset Password")

"""
# original webform for mission control panel
class MorseviewInterface(FlaskForm):
	FL_motor = BooleanField("Front Left")
	FR_motor = BooleanField("Front Right")
	RL_motor = BooleanField("Rear Left")
	RR_motor = BooleanField("Rear Right")

	delay_t = FloatField("Motor Speed (delay between steps in milliseconds): ")

	rotations = FloatField("Number of full or partial rotations (decimal): ")

	maneuver = RadioField("Maneuver", choices=["Forward","Reverse"])

	submit = SubmitField("Execute")




	## VV original lightshow code VV ##
	#blue_on = BooleanField("BLUE")
	#green_on = BooleanField("GREEN")
	#message = StringField("Type a message: ", 
	#	validators=[Length(max=60)])
	#submit = SubmitField("Submit")

"""