import re
import json
import random

class Question:
    """Represents a question.
    
    Properties:
        question (str, required): The question.
        correct_answer (Any, required): The correct answer.
        multiple_choice_one (Any, optional): The first multiple choice answer. Defaults to None.
        multiple_choice_two (Any, optional): The second multiple choice answer. Defaults to None.
        multiple_choice_three (Any, optional): The third multiple choice answer. Defaults to None.
    """
    def __init__(self, question, correct_answer,
                 multiple_choice_one=None, multiple_choice_two=None, multiple_choice_three=None):
        self._question = question
        self._correct_answer = correct_answer
        self._multiple_choice_one = multiple_choice_one
        self._multiple_choice_two = multiple_choice_two
        self._multiple_choice_three = multiple_choice_three

    @property
    def question(self):
        return self._question

    @question.setter
    def question(self, question: str):
        if self._is_valid_question(question):
            self._question = question

    @property
    def correct_answer(self):
        return self._correct_answer

    @correct_answer.setter
    def correct_answer(self, correct_answer):
        self._correct_answer = correct_answer

    @property
    def multiple_choice_one(self):
        return self._multiple_choice_one

    @multiple_choice_one.setter
    def multiple_choice_one(self, multiple_choice_one):
        self._multiple_choice_one = multiple_choice_one

    @property
    def multiple_choice_two(self):
        return self._multiple_choice_two

    @multiple_choice_two.setter
    def multiple_choice_two(self, multiple_choice_two):
        self._multiple_choice_two = multiple_choice_two

    @property
    def multiple_choice_three(self):
        return self._multiple_choice_three

    @multiple_choice_three.setter
    def multiple_choice_three(self, multiple_choice_three):
        self._multiple_choice_three = multiple_choice_three

    def has_multiple_choice(self):
        return (self.multiple_choice_one is not None | self.multiple_choice_two is not None | self.multiple_choice_three is not None)

    def _is_valid_question(self, question):
        pattern = re.compile("^([a-z]|[A-Z]|[0-9])+.*\\?")
        if pattern.match(question):
            return True
        return False


class Category:
    """Represents a category of questions.

    Properties:
        name (str): Name of the category.
        questions (list): The category's questions and answers.
        num_of_questions (int): The number of questions in the category.
    """

    def __init__(self, name: str):
        self._name = name
        self._questions = []
        self._num_of_questions = 0

    @property
    def name(self) -> str:
        """Get the category's name.

        Returns:
            name (str): Name of the category.
        """
        return self._name

    @property
    def questions(self) -> list:
        """Get the category's questions and answers.

        Returns:
            questions (list): The category's questions and answers.
        """
        return self._questions

    @property
    def num_of_questions(self) -> int:
        """Get the number of questions.

        Returns:
            num_of_questions (int): The number of questions in the category.
        """
        return self._num_of_questions

    def add_question(self, question: str, correct_answer, multiple_choice_one=None, multiple_choice_two=None,
                     multiple_choice_three=None) -> bool:
        """Add a new question.

        Args:
            question (str, required): The question.
            correct_answer (Any, required): The correct answer.
            multiple_choice_one (Any, optional): Multiple choice answer option one.
            multiple_choice_two (Any, optional): Multiple choice answer option two.
            multiple_choice_three (Any, optional): Multiple choice answer option three.
        Returns:
            bool: True if question was added, False otherwise
        """
        pattern = re.compile("^([a-z]|[A-Z]|[0-9])+.*\\?")
        if pattern.match(question):
            question_obj = Question(question, correct_answer, multiple_choice_one, multiple_choice_two,
                                    multiple_choice_three)
            self._questions.append(question_obj)
            self._num_of_questions += 1
            return True
        return False

    def edit_question(self, original_question: str, new_question: str, new_correct_answer=None,
                      new_multiple_choice_one=None, new_multiple_choice_two=None,
                      new_multiple_choice_three=None) -> bool:
        """Edit an existing question.

        Args:
            original_question (str, required): The original question.
            new_question (str, required): The updated question.
            new_correct_answer (Any, optional): The updated correct answer. Defaults to None.
            new_multiple_choice_one (Any, optional): The updated or new multiple choice answer one. Defaults to None.
            new_multiple_choice_two (Any, optional): The updated or new multiple choice answer two. Defaults to None.
            new_multiple_choice_three (Any, optional): The updated or new multiple choice answer three. Defaults to None.

        Returns:
            bool: True if question was updated, False otherwise.
        """
        for question_obj in self.questions:
            if question_obj.question == original_question:
                if new_question:
                    question_obj.question = new_question
                if new_correct_answer:
                    question_obj.correct_answer = new_correct_answer
                if new_multiple_choice_one:
                    question_obj.multiple_choice_one = new_multiple_choice_one
                if new_multiple_choice_two:
                    question_obj.multiple_choice_two = new_multiple_choice_two
                if new_multiple_choice_three:
                    question_obj.multiple_choice_three = new_multiple_choice_three
                return True
        return False

    def get_question(self):
        """Get a random question.
        
        
        Returns:
            Question: A question.
        """
        return random.choice(self.questions)

    def remove_question(self, question: str) -> bool:
        """Remove an existing question.

        Args:
            question (str, required): The question to remove.

        Returns:
            bool: True if question was removed, False otherwise.
        """
        for question_obj in self.questions:
            if question_obj.question == question:
                self._questions.remove(question_obj)
                self._num_of_questions -= 1
                return True
        return False

    def toJSON(self):
        """Return JSON serializable version of class.
        
        Returns:
            obj (JSON): JSON version of class
        """
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


class CategoryManager:
    """Manages the categories.

    Properties:
        categories (list): All the categories.
    """

    def __init__(self):
        self._categories = []

    @property
    def categories(self):
        """Get the categories.

        Returns:
            categories (list): All the categories.
        """
        return self._categories

    def get_category(self, category_name: str, to_JSON: bool = False) -> Category:
        """Get a category.

        Args:
            category_name (str, required): The name of the category.
            to_JSON (bool, optional): If True, return a JSON-serializable version of the category. If False, return category object. Defaults to False.

        Returns:
            category (Category): The category.
        """
        for category in self.categories:
            if category.name == category_name:
                if to_JSON:
                    return category.toJSON()
                return category

    def add_category(self, category_name: str) -> bool:
        """Add a new category.

        Args:
            category_name (str, required): The name of the category.


        Returns:
            bool: True
        """
        category = Category(category_name)
        self._categories.append(category)
        return True

    def remove_category(self, category_name: str) -> bool:
        """Remove an existing category.

        Args:
            category_name (str, required): The name of the category.

        Returns:
            bool: True if category was removed, False otherwise.
        """
        for category in self.categories:
            if category.name == category_name:
                self._categories.remove(category)
                return True
        return False


class Game():
    def __init__(self, category: Category):
        self._category = category
        self._curr_question_count = 0
        self._num_correct = 0
        self._num_incorrect = 0

    @property
    def category(self):
        return self._category

    @property
    def curr_question_count(self):
        return self._curr_question_count

    @property
    def num_correct(self):
        return self._num_correct

    @property
    def num_incorrect(self):
        return self._num_incorrect

    def pick_question(self):
        self._curr_question_count += 1
        return self.category.get_question()

    def validate_answer(self, question: Question, guess):
        if question.correct_answer == guess:
            self._num_correct += 1
            return True
        else:
            self._num_incorrect += 1
            return False