from flask import Flask

app = Flask(__name__, static_url_path='/resources/static')

__app_root__ = app.root_path


@app.route('/')
def index():
    """Index method to show services are up and running"""
    return 'Services up & running! :)'


if __name__ == '__main__':
    """Triggering in the main application"""
    app.run(host='0.0.0.0', port=1330)