from invoke import task

@task
def foo(ctx):
    print("bar")

