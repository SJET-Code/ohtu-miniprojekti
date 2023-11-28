from invoke import task

@task
def flask(ctx):
    ctx.run("python3 src/flask_app.py", pty=True)

@task
def start(ctx):
    ctx.run("python3 src/index.py", pty=True)

@task
def cov(ctx):
    ctx.run("coverage run --branch -m pytest; coverage html", pty=True)
