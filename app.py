from flask import Flask, jsonify

app = Flask(__name__)

# Main homepage route
@app.route('/')
def hello_world():
    return '<h1>Welcome to my Flask App!</h1><p>Append <b>/share/yourname</b> to the URL to try the sharing feature.</p>'

# NEW ROUTE: Share this link with your friend!
# Example: ://render.com
@app.route('/share/<friend_name>')
def share_with_friend(friend_name):
    # Capitalizes the first letter of their name automatically
    clean_name = friend_name.capitalize() 
    
    # The message your friend will see on their screen
    html_content = f"""
    <div style="text-align: center; margin-top: 50px; font-family: Arial, sans-serif;">
        <h1 style="color: #4CAF50;">Hello, {clean_name}! 👋</h1>
        <p style="font-size: 18px;">My creator built this Flask web application and wanted to share it with you!</p>
        <p style="color: #666;">Hosted live on Render.</p>
    </div>
    """
    return html_content

if __name__ == '__main__':
    app.run()
