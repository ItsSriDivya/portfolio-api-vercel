from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app, title='PortfolioBio')  # Title of the swagger page.

GetIntroData = api.namespace('GetIntroData')  # Name of the endpoint


# Using route decorator to declare the expected inputs. In this example, clientname and requrestID of string type are expected as inputs.
@GetIntroData.route('/', methods=['GET'])
class getintrouidata(Resource):
    def get(self):
        """Function to get the extracted data"""
        try:
            result = {
                'designation': 'Front End Developer',
                'name': 'SriDivya Pulapa',
                'description': 'I love to create beautiful and performant products with delightful user experiences.'
            }  # Call the required function here to get the output to send it as a response for the end point.
        except Exception as exe:
            raise RuntimeError(exe)
        return result, 200  # Returning response with status code


GetSkillsData = api.namespace('GetSkillsData')  # Name of the endpoint


# Using route decorator to declare the expected inputs. In this example, clientname and requrestID of string type are expected as inputs.
@GetSkillsData.route('/', methods=['GET'])
class getskillsuidata(Resource):
    def get(self):
        """Function to get the extracted data"""
        try:
            result = {
                "ProficientSkillSet": [
                    {
                        'key': 'js',
                        'title': 'Javascript'
                    },
                    {
                        'key': 'react',
                        'title': 'React JS'
                    },
                    {
                        'key': 'redux',
                        'title': 'Redux'
                    },
                    {
                        'key': 'html',
                        'title': 'HTML'
                    },
                    {
                        'key': 'css',
                        'title': 'CSS'
                    },
                    {
                        'key': 'sass',
                        'title': 'Sass'
                    },
                ],
                "skillfulSkillSet": [
                    {
                        'key': 'ts',
                        'title': 'Typescript'
                    },
                    {
                        'key': 'bs',
                        'title': 'Bootstrap'
                    },
                    {
                        'key': 'python',
                        'title': 'Python'
                    },
                    {
                        'key': 'docker',
                        'title': 'Docker'
                    },
                ]
            }  # Call the required function here to get the output to send it as a response for the end point.
        except Exception as exe:
            raise RuntimeError(exe)
        return result, 200  # Returning response with status code


if __name__ == '__main__':
    app.run(debug=True, port=5000)
