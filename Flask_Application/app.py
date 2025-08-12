import json
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

# Create the Flask application instance
app = Flask(__name__)


# --- HELPER FUNCTION ---
def fetch_post_by_id(post_id):
    """Finds a post by its ID from the JSON file."""
    with open('posts.json', 'r') as f:
        posts = json.load(f)
    for post in posts:
        if post['id'] == post_id:
            return post
    return None


# --- ROUTES ---

@app.route("/")
@app.route("/home")
def index():
    """Displays the main page with all blog posts."""
    with open('posts.json', 'r') as f:
        blog_posts = json.load(f)
    return render_template('index.html', posts=blog_posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """Handles adding a new blog post."""
    if request.method == 'POST':
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')

        with open('posts.json', 'r+') as f:
            posts = json.load(f)

            # Find the highest existing ID and add 1
            new_id = max([post['id'] for post in posts]) + 1 if posts else 1

            new_post = {
                'id': new_id,
                'author': author,
                'title': title,
                'content': content,
                'date_posted': datetime.now().strftime('%B %d, %Y'),
                'likes': 0  # New posts start with 0 likes
            }

            posts.append(new_post)
            f.seek(0)
            json.dump(posts, f, indent=2)

        return redirect(url_for('index'))

    return render_template('add.html')


@app.route('/update/<int:post_id>', methods=['GET', 'POST'])
def update(post_id):
    """Handles updating an existing blog post."""
    post = fetch_post_by_id(post_id)
    if post is None:
        return "Post not found", 404

    if request.method == 'POST':
        new_title = request.form.get('title')
        new_content = request.form.get('content')

        with open('posts.json', 'r') as f:
            posts = json.load(f)

        for p in posts:
            if p['id'] == post_id:
                p['title'] = new_title
                p['content'] = new_content
                break

        with open('posts.json', 'w') as f:
            json.dump(posts, f, indent=2)

        return redirect(url_for('index'))

    return render_template('update.html', post=post)


@app.route('/delete/<int:post_id>', methods=['POST'])
def delete(post_id):
    """Handles deleting a blog post."""
    with open('posts.json', 'r') as f:
        posts = json.load(f)

    posts = [post for post in posts if post['id'] != post_id]

    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

    return redirect(url_for('index'))


@app.route('/like/<int:post_id>', methods=['POST'])
def like(post_id):
    """Handles incrementing the like count for a post."""
    with open('posts.json', 'r') as f:
        posts = json.load(f)

    for post in posts:
        if post['id'] == post_id:
            post['likes'] += 1
            break

    with open('posts.json', 'w') as f:
        json.dump(posts, f, indent=2)

    return redirect(url_for('index'))


# This block runs the app
if __name__ == '__main__':
    app.run(debug=True)

