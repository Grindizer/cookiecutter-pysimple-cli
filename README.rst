=========================
cookiecutter-pysimple-cli
=========================

Cookiecutter template for a a simple python command line
interface application.
It is mainly helpful to turn those one file python code into a
useful python package that expose a basic command line interface (making others want to use your application !)

Out of the box you would get:

* Pbr_ Integration.
* Pytest_ runner supports.
* Click_ for command line interface.

Usage & Workflow
----------------

* Generate a Python package::

    cookiecutter thisrepo

* Answer a couple of template questions:
 most important being the name you would like to give to to you application/project.

* At this stage you get a working python application.
that can be installed through ::

    pip install -e .

or

    python setup.py install

The main function of your application is callable at::

    <package_name>_cli

Because of the integration with pbr, you can create new version on your code
by creating a git tag:

ex:
    git tag -a 0.1.0
    git push --tags


.. _Pytest: http://pytest.org/
.. _Click:
.. _Pbr: