from app import create_app, db
from flask_migrate import Migrate

# Create app instance
app = create_app()

# Set up migration tool
migrate = Migrate(app, db)


# Run the app
if __name__ == '__main__':

 
    # Run the development server
    app.run(debug=True)
