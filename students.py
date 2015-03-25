from peewee import *

db = SqliteDatabase('students.db')


class Student(Model):
	username = CharField(max_length=255, unique=True)
	points = IntegerField(default=0)

	class Meta:
		database = db

students = [
	{'username':'klove','points':54333},
	{'username':'blove','points':4300},
	{'username':'clove','points':2483},
	{'username':'hlove','points':11003},

]


def addStudents():
	for student in students:
		try:
			Student.create(username = student['username'], points = student['points'])
		except IntegrityError:
			studentRecord = Student.get(username = student['username'])
			studentRecord.points = student['points']
			studentRecord.save()

def topStudent():
	student = Student.select().order_by(Student.points.desc()).get()
	return student

if __name__ == '__main__':
	db.connect()
	db.create_tables([Student], safe=True)
	addStudents()
	print("Our top student right now is: {0.username}.".format(topStudent()))