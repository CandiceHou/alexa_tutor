import data
#get supported courses
def get_supported_courses():
    courses = []
    for c in data.CLASS_DATA:
        courses.append(c['class name'])
    return courses


# partner with the class
def partner_with_class(class_name):
    
    found_class = False;
    for cls in data.CLASS_DATA:
        if class_name in cls['class name']:
            found_class = True;
    if (found_class):
        return class_name;
       # return "What can I help you with " + class_name;
    else:
        return "";
    
# get answers by keys
def get_answers_by_keys(class_name, key):
    found_question = False;
    for cls in data.CLASS_DATA:
        if class_name == cls["class name"]:
            for i in range(0,len(cls["question set"])):
                if key in cls["question set"][i]["key"]:
                    found_question = True;
                    return cls["question set"][i]["answer"];
    if found_question == False:
        return "Not Found";
    

# get answers by questions
def get_answers_by_questions(class_name, question):
    found_question = False;
    for cls in data.CLASS_DATA:
        if class_name == cls['class name']:
            for i in range(0, len(cls["question set"])):
                if question in cls["question set"][i]["question"]:
                    found_question = True;
                    return cls["question set"][i]["answer"];
    if found_question == False:
        return "Sorry, the question has not been added yet, we will make updates soon."