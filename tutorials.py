"""     @author:        Guang Yang
        @mktime:        7/10/2014
        @description:   ideas/schedule for teaching 10 min tutorials
"""

# -- Initialization --
class Ideas(object):
    """ Ideas/schedule for tutorials

    Attributes:
        name: Name of the idea
        description: Description of the idea
        date: Date to present the idea
        resource: any resources supporting/elaborating the idea

    Methods:
        Ideas.get_all_idea(): Shows all ideas
        Ideas.get_schedule(): Shows schedule with ideas
        Ideas.get_idea('name of idea'): Access the object associated with that idea  
    """

    all_idea = []
    def __init__(self, name=None, description=None, date=None, resource=None):
        self.name = name
        self.description = description
        self.date = date
        self.resource = resource
        Ideas.all_idea.append(self)
    
    def __repr__(self):
        return self.name

    @staticmethod
    def get_all_idea():
        return idea_dict.keys()

    @staticmethod
    def get_schedule():
        date_list = schedule_dict.keys()
        date_list.sort()
        schedule_list = [(i_date, schedule_dict[i_date]) for i_date in date_list]
        return schedule_list

    @staticmethod
    def get_idea(idea_name):
        return idea_dict[idea_name]

    def __str__(idea):
        return "Name: {idea.name} \nDescription: {idea.description} \nDate: {idea.date} \nResource: {idea.resource}".format(idea=idea)


# -- Populating Database --
idea1 = Ideas('IPython',
              'IPython basics, Tab Completion, Introspection', 
              '20140716',
              'Python for Data Analysis',
              )

idea2 = Ideas('Text Editors',
              'Vim, Emacs, Sublime Text, Textmate',
              '20140714',
              None,
              )

idea3 = Ideas('Data Analysis with NumPy', 
              'NumPy, SciPy, pandas'
              )

idea4 = Ideas('Documentation',
              'Docstrings',
              )

idea5 = Ideas('Test Driven Development',
              'built-in Doctest',
              )

idea6 = Ideas('2D Visualizations',
              'matplotlib',
              )

# -- Keep Track --
idea_dict = {i_idea.name: i_idea for i_idea in Ideas.all_idea} 
schedule_dict = {i_idea.date: i_idea for i_idea in Ideas.all_idea}
