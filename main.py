from bottle import route, run
import subprocess
import time

### Define where your git directory is. This needs to be absolute with now trailing slash.
gitdir = '/home/your/git/directory'
### Define the Screen session name you want the server to run under.
screen_session = 'django'
# Define which server you're using. Currently only supports django. Use 'None' if you are using something else.
server = 'django'

if server == 'django':
    @route('/github', method='POST')
    def index(name='Github'):
        subprocess.Popen(['screen', '-X', '-S', screen_session, 'kill'])
        time.sleep(.1)
        subprocess.Popen(['git', 'pull'], cwd=gitdir)
        time.sleep(.1)
        subprocess.Popen(['screen', '-S', screen_session, 'python', './manage.py', 'runserver', '0.0.0.0:80'], cwd=gitdir)
        time.sleep(.1)
        subprocess.Popen(['screen', '-d', screen_session])
        return 'Thanks'
else:
    @route('/github', method='POST')
    def index(name='Github'):
        subprocess.Popen(['git', 'pull'], cwd=gitdir)
        time.sleep(.1)
        return 'Thanks'

run(host='0.0.0.0', port=5050)
