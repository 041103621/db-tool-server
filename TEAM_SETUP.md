# Team Setup Guide

## Getting Started

1. **Clone the Repository**
   ```bash
   git clone https://github.com/041103621/db-tool-server.git
   cd db-tool-server
   ```

2. **Switch to Development Branch**
   ```bash
   git checkout demo-dev
   ```

3. **Install Dependencies**
   ```bash
   python -m venv venv
   # For Windows:
   venv\Scripts\activate
   # For Linux/Mac:
   source venv/bin/activate
   
   pip install -r requirements.txt
   ```

4. **Configure the Environment**
   - Copy the example configuration if provided
   - Set up your local database connection
   - Configure log file paths as needed

5. **Start Development**
   ```bash
   python run.py
   ```

## Development Workflow

1. **Before Starting New Work**
   ```bash
   git checkout demo-dev
   git pull origin demo-dev
   ```

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Changes and Commit**
   ```bash
   git add .
   git commit -m "feat: describe your changes"
   ```

4. **Push Your Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

5. **Create Pull Request**
   - Go to GitHub repository
   - Create a pull request from your feature branch to demo-dev
   - Wait for review and approval

## Important Notes

- Always pull the latest changes before starting new work
- Keep commits focused and well-described
- Follow the existing code style and conventions
- Test your changes before pushing
- Document any significant changes or new features

## Common Issues and Solutions

### If you see "This site can't be reached" error:
1. Check if the server is running
2. Verify you're using the correct port (default: 5001)
3. Ensure all dependencies are installed

### Database Connection Issues:
1. Verify Oracle Docker container is running
2. Check database credentials in config
3. Ensure Oracle client is properly installed

## Need Help?

If you encounter any issues:
1. Check the error logs
2. Review the documentation
3. Ask team members for help
4. Create an issue on GitHub if needed 