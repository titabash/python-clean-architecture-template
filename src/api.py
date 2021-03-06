import os
from controller import create_app

app = create_app()


port = int(os.environ.get('PORT', 8000))
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port, debug=True)
