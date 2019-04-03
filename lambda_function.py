import tutor_, data
import logging

from flask import Flask, render_template
from flask_ask import Ask, statement, question, session, request


app = Flask(__name__)
ask = Ask(app, '/')
logging.getLogger("flask_ask").setLevel(logging.DEBUG)

def lambda_handler(event, _context):
    return ask.run_aws_lambda(event)

@ask.launch
def welcome():
    return question(render_template('welcome')) \
        .reprompt(render_template("reprompt"))
    
@ask.intent("AMAZON.HelpIntent")
def help():
    return question(render_template('help')) \
        .reprompt(render_template("reprompt"))
    
@ask.intent("AMAZON.FallbackIntent")
def fallback():
    return question(render_template('error-not-understand')) \
        .reprompt(render_template('error-not-understand'))

@ask.intent('AMAZON.CancelIntent')
@ask.intent("AMAZON.StopIntent")
def stop():
    return statement(render_template('goodbye'))


@ask.intent('SupportedCoursesIntent')
def supported_courses():
    courses = get_supported_courses()
    answer_msg = render_template('answer-supported-courses', results = courses)
    help_msg = render_template('ask-class')
    return question(answer_msg).reprompt(help_msg)

@ask.intent('PartnerWithCourseIntent')
def partner_with_class(class_name):
    matchedClass_ = partner_with_class(class_name)
    if (matchedClass != ""):
        session.attributes['class_name'] = matchedClass
        answer_msg = render_template('ask-question', courses = matchedClass)
        return question(answer_msg)
    
@ask.intent("GetAnswerIntent")
def get_answer(question):
    class_name = session.attributes['class_name'] 
    key = question
    answer = get_answers_by_keys(class_name, key)
    if (answer == "Not Found"):
        answer = get_answers_by_questions(class_name, question);
    return question(answer)

if __name__ == '__main__':
    app.run(debug=True)