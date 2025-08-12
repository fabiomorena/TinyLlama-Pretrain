# Flask Blog Application

A simple blog application built with the Python Flask framework. This application allows users to create, read, edit, and delete blog posts with an intuitive web interface.

## ✨ Features

- **Blog Post Management**: Complete CRUD functionality (Create, Read, Update, Delete)
- **Post Creation**: Add new blog entries with author, title, and content
- **Post Editing**: Update existing posts (title and content)
- **Post Deletion**: Remove unwanted posts
- **Like System**: Rate posts with thumbs up
- **Automatic Timestamps**: Each post automatically receives a creation date
- **Responsive Design**: Modern user interface with custom CSS styling
- **JSON Data Storage**: Simple data persistence using JSON files

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, Jinja2 Templates
- **Data Storage**: JSON files
- **Styling**: Custom CSS with modern design

## 📊 Data Structure

Each blog post contains the following fields:
- `id`: Unique post identifier
- `author`: Author's name
- `title`: Post title
- `content`: Main post content
- `date_posted`: Creation date
- `likes`: Number of likes

## 🚀 Installation and Setup

Follow these steps to set up and run the project locally.

### 1. Clone the Repository
```bash
git clone https://github.com/fabiomorena/Flask_Application.git
cd Flask_Application
```

### 2. Create and Activate Virtual Environment
It is strongly recommended to use a virtual environment to isolate project dependencies.

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install Dependencies
All required Python packages are listed in the requirements.txt file.

```bash
pip install -r requirements.txt
```

If no requirements.txt exists, install Flask manually:
```bash
pip install Flask
pip freeze > requirements.txt
```

### 4. Start the Application
Run the main file to start the development server.

```bash
python app.py
```

The application should now be accessible in your browser at:
**http://127.0.0.1:5000**

## 📖 Usage

### Main Page
- Displays all existing blog posts
- Click "Add New Post" to create a new blog entry

### Creating a Post
- Navigate to `/add`
- Fill in the fields for author, title, and content
- Click "Submit Post"

### Editing a Post
- Click "Update" on any post
- Edit the title and/or content
- Save your changes

### Deleting a Post
- Click "Delete" on any post
- The post will be immediately and permanently removed

### Liking Posts
- Click the "Like" button on any post
- The like count will automatically increment

## 🗂️ Project Structure

```
Flask_Application/
│
├── app.py                 # Main application with all routes
├── posts.json            # JSON file for data storage
├── style.css             # CSS styling (optional/legacy)
├── templates/            # HTML templates
│   ├── index.html        # Main page with post overview
│   ├── add.html          # Form for new posts
│   └── update.html       # Form for post updates
├── data_structure.json   # Example of data structure
└── README.md             # Project documentation
```

## 🔧 API Routes

| Route | HTTP Method | Description |
|-------|-------------|-------------|
| `/` or `/home` | GET | Display all blog posts |
| `/add` | GET, POST | Form to create new posts |
| `/update/<post_id>` | GET, POST | Edit existing post |
| `/delete/<post_id>` | POST | Delete a post |
| `/like/<post_id>` | POST | Like a post |

## ⚙️ Configuration

No special environment variables are required. The application runs in debug mode for development purposes.

## 🚨 Production Notes

For production deployment, consider the following:
- Disable debug mode (`debug=False`)
- Use a real database instead of JSON files (SQLite, PostgreSQL, etc.)
- Implement authentication and authorization
- Add input validation and sanitization
- Improve error handling
- Set up proper logging
- Use a production WSGI server (Gunicorn, uWSGI)

## 🔒 Security Considerations

This is a basic application intended for learning purposes. For production use, implement:
- User authentication
- CSRF protection
- Input validation
- SQL injection prevention (when using databases)
- XSS protection

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## 📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.

---
**Created by Fabio Morena**