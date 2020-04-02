from pymongo import MongoClient

client = MongoClient('mongodb+srv://user:user@cluster0-4ax1c.mongodb.net/test?retryWrites=true&w=majority')
db = client["digital_library"]
book_collection = db['book']
customer_collection = db['course']
student_collection = db['student']

books = [

    {'_id': 0, 'title': 'Calculus 1', 'author': 'Author', 'course_id': 0},

]

course = [
    {'_id': 0, 'course_name': 'Differential equations', 'target_audience': 'BS2', 'instructor_id': 0}
]

student = [
    {'_id': '0', 'first_name': 'Sasha', 'last_name': 'Petrova', 'course': 'BS2',
     'courses_id': [0, 1]}
]

book_collection.insert_many(books)
customer_collection.insert_many(course)
student_collection.insert_many(student)

client.close()