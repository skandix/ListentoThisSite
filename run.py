from gevent.wsgi import WSGIServer
import dataporno_server

http_server = WSGIServer(('', 8069),dataporno_server.app)
http_server.serve_forever()
