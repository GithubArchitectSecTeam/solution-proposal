from flask import Flask, request
from github import Github
import yaml

app = Flask(__name__)

token = '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'
g = Github(token)


@app.route("/keepalive")
def keepalive():
    return "KEEPALIVE_OK"


@app.route("/", methods=["POST"])
def webhook():
    data = request.get_json()
    if data["action"] == "created":
        # Create a README file
        repo_name = data["repository"]["full_name"]
        repo = g.get_repo(repo_name)
        repo.create_file("README", "Auto commit", repo_name)
        print("Repository " + repo_name + " has been created and initialized")

        # Get Default branch and set branch protection rules
        default_branch = repo.default_branch
        protected_branch = repo.get_branch(default_branch)
        protected_branch.edit_protection(enforce_admins=True, require_code_owner_reviews=True,
                                         required_approving_review_count=2)
        print("Branch protection enabled for " + default_branch + " branch")

        # Create an Issue and mention the protection rules that were enabled
        branch_protection_rules = yaml.dump(protected_branch.get_protection().raw_data)
        body = "@GithubArchitect \n {}".format(branch_protection_rules)
        repo.create_issue(title="Branch protection enabled", body=body)
    return "OK"


if __name__ == "__main__":
    app.run(host='localhost')
