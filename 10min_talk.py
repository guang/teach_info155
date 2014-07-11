"""     @author:        Guang Yang
        @mktime:        7/10/2014
        @description:   ideas/schedule for teaching 10 min mini-lectures
"""
class Ideas(object):
    def __init__(self, name=None, description=None, date=None, resource=None):
        self.name = name
        self.description = description
        self.date = date
        self.resource = resource
    
    def __repr__(self):
        return self.name

    def display_all_ideas():


# -- ToDo: implement the pretty print --
    def __print__(self):
        return "implement me"

idea1 = Ideas('IPython',
              'IPython basics, Tab Completion, Introspection, Timing Code, Basic Profiling',
              '7-14-2014',
              'Python for Data Analysis',
              )

idea2 = Ideas('Text Editors',
              'Vim, Emacs, Sublime Text, Textmate',
              '7-16-2014',
              None,
              )

idea3 = Idea('

