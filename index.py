import os
import re
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def get_post(path):
    m = re.search('(/post/)?([^\.]+)', path)
    return m.group(2)

class PostHandler(webapp.RequestHandler):
  def get(self):
    post = get_post(self.request.path)
    title = '%s :: %s' % ('rm -rf slash', post)
    path = os.path.join(os.path.dirname(__file__), "post/%s.html" % post)
    self.response.out.write(template.render(path, {'post': post, 'title': title, 'img_folder': '/img/%s' % post }))

class MainPage(webapp.RequestHandler):
    def get(self):
      files = os.listdir(os.path.join(os.path.dirname(__file__), 'post'))
      post_names = [get_post(f) for f in files]
      template_values = { 'files' : post_names, 'title': 'rm -rf slash' }
      path = os.path.join(os.path.dirname(__file__), 'index.html')
      self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([
    ('/post/.*', PostHandler),
    ('/.*', MainPage)
], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
