''' This file includes all the functions needed for the app '''

from jinja2 import Markup, PackageLoader, Environment

#def file_include(name):
    #return Markup(loader.get_source(env, name)[0])
#
#loader = PackageLoader(__name__, '')
#env = Environment(loader=loader)
#env.globals['file_include'] = file_include
#
#def render():
#    return env.get_template('base.html').render()
#
#if __name__ == '__main__':
#    print(render())