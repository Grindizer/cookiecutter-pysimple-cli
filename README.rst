=========================
cookiecutter-pysimple-cli
=========================

Cookiecutter template for a simple python command line
interface application.
It is mainly helpful to turn those one file python code into a
useful python package that expose a basic command line interface (make others want to use your super app !!)

Out of the box you would get:

* Pbr_ Integration.
* Pytest_ runner supports.
* Click_ for command line interface.

Usage & Workflow
-----------------

1. Generate a Python package::

    cookiecutter thisrepo

2. Answer a couple of template questions (most important being the name you would like to give to you application/project).

3. At this stage you get a working python application.
that can be installed through::

    cd <your new generated project>
    git init .
    pip install -e .

or::

    cd <your new generated project>
    git init .
    python setup.py install

4. The main function of your application is callable at::

    <package_name>_cli


Because of the integration with pbr, you can create a new versions on your code
by creating a git tag:

ex::

    git tag -a 0.1.0
    git push --tags

Your new created version of your command line can then be installed by::

    pip install git+<github repo>@0.1.0#egg=<package name>

Example
--------
Want to see what the generated project looks like? https://github.com/Grindizer/pyboilerplate

.. _Pytest: http://pytest.org/
.. _Click:
.. _Pbr: