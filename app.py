from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Static site generation
def build_static_site():
    with app.test_request_context():
        # Rendering pages to files
        os.makedirs('dist', exist_ok=True)
        pages = ['index', 'about']
        for page in pages:
            rendered_page = render_template(f'{page}.html')
            with open(f'dist/{page}.html', 'w') as f:
                f.write(rendered_page)
        print("Static site generated successfully.")

if __name__ == "__main__":
    build_static_site()
