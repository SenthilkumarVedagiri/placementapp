
import subprocess


class AppLauncher:
    """Handles launching the Streamlit application"""
    @staticmethod
    def launch_streamlit():
        """Launches the Streamlit application"""
        subprocess.run(["streamlit", "run", "main.py"])

if __name__ == "__main__":
    # Example: Testing the DB connection
    #db_manager = DatabaseManager()
    #connection = db_manager.connect()
    #if connection:
     #   db_manager.close()
    
    # Launch Streamlit app
    #AppLauncher.launch_streamlit()
    print("Launching streamlit app.....")