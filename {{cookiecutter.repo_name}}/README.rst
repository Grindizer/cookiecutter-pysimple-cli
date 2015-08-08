===========
{{cookiecutter.package_name|capitalize}}
===========

{{cookiecutter.short_description}}

Installation
============

::

    pip install git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}#egg={{cookiecutter.package_name}}

Or in a develop mode after downloading a zip or cloning the git repository ::

    git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}
    cd {{cookiecutter.repo_name}}
    pip install -e .

Or in a develop mode from a git repository ::

    pip install -e git+https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}#egg={{cookiecutter.package_name}}

Once installed you can run ::

 {{cookiecutter.package_name}}_cli --help

Development
===========

To run the all tests run ::

    py.test

