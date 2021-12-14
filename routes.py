from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from .server import CategoryManager

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

category_manager = CategoryManager()

@app.route('/category', methods=['GET', 'POST', 'DELETE'])
@cross_origin()
def category():
    return 'Hello'
    # payload = request.get_json()
    # category = str(payload['category'])
    # if request.method == 'GET':
    #     return category_manager.get_category(category, True), 200
    # elif request.method == 'POST':
    #     if category_manager.add_category(category):
    #         return 'Category added.', 204
    #     return 'Category not added.', 400
    # elif request.method == 'DELETE':
    #     if category_manager.remove_category(category):
    #         return 'Category deleted.', 200
    #     return 'Category not deleted.', 400


@app.route('/question', methods=['GET', 'POST', 'DELETE'], )
def question():
    payload = request.get_json()
    question = str(payload['question'])
    correct_answer = str(payload['correct_answer'])
    multiple_choice_one = None
    multiple_choice_two = None
    multiple_choice_three = None
    if 'multiple_choice_one' in payload:
        multiple_choice_one = str(payload['multiple_choice_one'])
    if 'multiple_choice_two' in payload:
        multiple_choice_two = str(payload['multiple_choice_two'])
    if 'multiple_choice_three' in payload:
        multiple_choice_three = str(payload['multiple_choice_three'])
    category = str(request.args.get('category'))
    if request.method == 'GET':
        return 'GET'
    elif request.method == 'POST':
        category_obj = category_manager.get_category(category, False)
        if category_obj.add_question(question, correct_answer, multiple_choice_one, multiple_choice_two, multiple_choice_three):
            return 'Question added.', 200
        return 'Question not added.', 400
    elif request.method == 'DELETE':
        return 'DELETE'