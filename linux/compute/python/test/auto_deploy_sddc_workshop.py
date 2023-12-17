from github import Github, GithubException
import logging
import os

# Set up logging with date and time stamps
logging.basicConfig(filename='github_script.log',
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

# GitHub authentication
github_token = "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"  # Secure your token
github_username = "codyshoward"
repo_name = "SDDC_WorkShop"  # Repository name

# Authenticate with GitHub
g = Github(github_token)
for repo in g.get_user().get_repos():
    print(repo.name)

# Function to get or create a repository
def get_or_create_repo(github_username, repo_name):
    try:
        # Try to get the repository if it exists
        repo = g.get_user().get_repo(repo_name)
        logging.info(f"Repository '{repo_name}' found.")
        return repo
    except GithubException as e:
        if e.status == 404:  # Check if it's a 'Not Found' exception
            # Create the repository if it doesn't exist
            logging.info(f"Repository '{repo_name}' not found, creating new one.")
            return g.get_user().create_repo(repo_name)
        else:
            # If it's a different exception, re-raise it
            raise

# Function to check if a file exists in the repo
def file_exists_in_repo(repo, path):
    try:
        repo.get_contents(path)
        return True
    except:
        return False

# Function to create a file in the repository if it doesn't exist
def create_file_in_repo(repo, path, message, content):
    if not file_exists_in_repo(repo, path):
        repo.create_file(path, message, content)
        logging.info(f"Created file {path}")
        # Log the creation of the directory structure
        directory_path = os.path.dirname(path)
        if directory_path:
            logging.info(f"Created directory structure: {directory_path}")

# Function to create the directory structure
def create_directory_structure(repo):
    top_level_dirs = ["ucs", "power", "cooling", "purefa", "purefb", "linux", "vsphere", "windows", "ansible", "netbox", "ftd", "bigip", "nexus", "aci"]

    for top_dir in top_level_dirs:
        second_level_dirs = ["compute", "network", "storage"]
        for second_dir in second_level_dirs:
            second_path = f"{top_dir}/{second_dir}/README.md"
            if not file_exists_in_repo(repo, second_path):
                create_file_in_repo(repo, second_path, "Initial commit for second level dir", f"# README for {second_dir} in {top_dir}")

                third_level_dirs = ["ivanti", "ansible", "bash", "powershell", "python"]
                for third_dir in third_level_dirs:
                    fourth_level_dirs = ["prod", "test"]
                    for fourth_dir in fourth_level_dirs:
                        file_path = f"{top_dir}/{second_dir}/{third_dir}/{fourth_dir}/README.md"
                        create_file_in_repo(repo, file_path, "Initial commit", f"# README for {fourth_dir} in {third_dir}")

def main():
    logging.info("Script started")
    repo = get_or_create_repo(github_username, repo_name)
    create_directory_structure(repo)
    logging.info("Script finished")

if __name__ == "__main__":
    main()
