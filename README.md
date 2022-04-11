<div id="top"></div>
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
     <li><a href="#webhook">Organization webhook Configuration</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This is a use case customer scenario proposed by Github Inc:  
> Our security team is asking for help ensuring proper reviews are being done to code being added into our repositories. We have hundreds of repositories in our organization. 
> What is the best way we can achieve at scale? We are new to some of the out-of-the-box settings and the GitHub API. 
> Can you please help us create a solution that will accomplish this for our security team?

The Solution proposed is as such:
* Listen for Gihub **Organization Events** to know when a repository has been created.
* When the repository is created, please automate the protection of the default branch
* Notify yourself with an @mention in an issue within the repository that outlines the protections that were added.

<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

These are the languages, frameworks and technologies used with this project
* [Python 3](https://python.org/)
* [Flask Web Framewwork](https://flask.palletsprojects.com/en/2.1.x/)
* [Ngrok](https://ngrok.com/)
* [PyGithub (Python wrapper for Github REST API)](https://pygithub.readthedocs.io/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This will run the solution locally.

### Prerequisites
* Python 3
  ```
  https://www.python.org/downloads/
  ```
* pip3
  ```
  https://pip.pypa.io/en/stable/installation/
  ```
* Ngrok
  ```
  1. Create an account on Ngrok.com
  2. Install Ngrok
  3. Get the ngrok token from the dashboard
  ```
### Installation
First, you need to lauch the Flask Webserver:
1. Clone the repo
   ```sh
   git clone https://github.com/GithubArchitectSecTeam/proposal.git
   ```
2. Install project dependencies
   ```sh
   pip3 install -r requirements.txt
   ```
3. Export the FLASK_APP variable:
   ```sh
   export FLASK_APP=app
   ```
4. Launch the Flask webserver (port 5000 default):
   ```sh
   flask run --host localhost
   ```
5. Run Ngrok on another terminal:
   ```sh
   ngrok http 80
   ```
<p align="right">(<a href="#top">back to top</a>)</p>


## Organization webhook Configuration
1. Configure Organization webhook:
> In the Organization dashboard in Github, Go to **Settings** > **Webhooks** > **Add Webhook**.
2. Add this parameters to the webhook:
* Payload URL: **URL from Installation Step 5**
* Content type: **application/json**
* What events would you like to trigger: **Let me select individual events**
* Individual events: **Repositories**

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
Whenever a new Repository is created in our Organization, the configured webhook will be triggered.<br>
Our webserver will create a README.md file, which in turn, will create a default branch. <br>
On that default branch, we will enable some branch protection rules.
<!-- CONTACT -->
## Contact

@GithubArchitect

Project Link: [https://github.com/organizations/GithubArchitectSecTeam](https://github.com/organizations/GithubArchitectSecTeam)

<p align="right">(<a href="#top">back to top</a>)</p>