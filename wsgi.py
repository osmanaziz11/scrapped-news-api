from app import app
from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher
 
if __name__ == "__main__":
    try:
        path_info_descriptor = PathInfoDispatcher({'/': app})
        server = WSGIServer(('0.0.0.0', 80), path_info_descriptor)
        print("Server started")
        server.start()
    except KeyboardInterrupt:
        server.stop()
        print("Server stopped")