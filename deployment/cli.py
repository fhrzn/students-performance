from inference import Inference
from InquirerPy import prompt
from utils.validator import ScoreValidator
from pyfiglet import Figlet


f = Figlet(font='standard')
print(f.renderText('Student Score Prediction'))

print('Welcome!')
s = '''
This is a cli-based student score prediction with machine learning. If you are curious enough about our data exploration and model building, please visit here:
    \n    
    - https://www.kaggle.com/affand20/students-performance-deep-analysis (Exploratory Data Analysis)
    \n
    - TODO (Model Building)
    \n
Task & Dataset: https://www.kaggle.com/spscientist/students-performance-in-exams
Github repo: https://github.com/affand20 
Made with ♥︎ by affand20
\n
'''
print(s)


# prompt question
questions = [    
    {
        "type": "list",
        "message": "Your gender:",
        "choices": ["Male", "Female"],
        "name": 'gender'
    },
    {
        'type': 'list',
        'message': 'Your Race/ethnicity:',
        'choices': ['group A', 'group B', 'group C', 'group D', 'group E'],
        'name': 'race/ethnicity'
    },
    {
        'type': 'list',
        'message': 'Your parent\'s education:',
        'choices': ['Master\'s Degree', 'Bachelor\'s Degree', 'Associate\'s Degree', \
            'Some College', 'High School', 'Some High School'],
        'name': 'parental level of education'
    },
    {
        'type': 'list',
        'message': 'Your type of lunch:',
        'choices': ['Standard', 'Free/reduced'],
        'name': 'lunch'
    },
    {
        'type': 'list',
        'message': 'Did you take test preparation course?',
        'choices': ['Yes', 'No'],
        'name': 'test preparation course'
    },
    {
        'type': 'input',
        'message': 'Please enter your math score (0-100)',
        'validate': ScoreValidator(),
        'name': 'math score'
    },
    {
        'type': 'input',
        'message': 'Please enter your reading score (0-100)',
        'validate': ScoreValidator(),
        'name': 'reading score'
    },
    {
        'type': 'input',
        'message': 'Please enter your writing score (0-100)',
        'validate': ScoreValidator(),
        'name': 'writing score'
    },
    {"type": "confirm", "message": "Confirm?", 'name': 'confirm'},
]

# prompt
result = prompt(questions)
while not result['confirm']:
    result = prompt(questions)

# fix some value
result['gender'] = result['gender'].lower()
result['parental level of education'] = result['parental level of education'].lower()
result['lunch'] = result['lunch'].lower()
result['test preparation course'] = 'completed' if result['test preparation course'] == 'Yes' else 'none'
result['math score'] = int(result['math score'])
result['reading score'] = int(result['reading score'])
result['writing score'] = int(result['writing score'])
del result['confirm']

# do inference
infer = Inference()
predicted = infer.make_prediction(result)
print('Your predicted final score: {}'.format(predicted['predicted_score'][0]))