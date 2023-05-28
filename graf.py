from tkinter import Tk
import matplotlib
from flask import Flask
import numpy as np
import io
from flask import send_file
import matplotlib.pyplot as plt
from subjects import get_subject

matplotlib.use('agg')
app = Flask(__name__)
root = Tk()
plt.rcParams["figure.figsize"] = [7.50, 4]
subjects_name=get_subject()

@app.route('/number_of_students_in_each_training')
def number_of_students_in_each_training():
    # d = StudentsDesiresCrud()
    opt_names, opt_amount = subjects_name, [3, 40, 6, 19, 34, 23]
    subjects = np.arange(1, 7)
    data = opt_amount
    plt.clf()
    plt.plot(subjects, data)
    plt.xlabel('subjects')
    plt.ylabel('number of students')
    plt.title('Plot Title')
    subjects_names = opt_names
    plt.xticks(subjects, subjects_names)
    # Save the plot to a BytesIO object
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    # Return the plot as a response
    return send_file(buffer, mimetype='image/png')


@app.route("/compare_students_grades/<student1_id>/<student2_id>")
def compare_students_grades(student1_id, student2_id):
    arr1 = [87, 90, 78, 56, 99, 89]
    arr2 = [80, 96, 72, 40, 78, 67]
    student1_grades, student2_grades = arr1, arr2,
    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    X = np.arange(6)
    p1 = plt.bar(X, student1_grades, bar_width, color='b',
                 label='John')
    # The bar of second plot starts where the first bar ends
    p2 = plt.bar(X + bar_width, student2_grades, bar_width,
                 color='g',
                 label='Sam')
    plt.xlabel('Subject')
    plt.ylabel('Scores')
    plt.title('Scores in each subject')
    plt.xticks(X + (bar_width / 2), (subjects_name[0], subjects_name[1], subjects_name[2], subjects_name[3],
                                     subjects_name[4], subjects_name[5]))

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    return send_file(buffer, mimetype='image/png')


app.run(debug=True)
