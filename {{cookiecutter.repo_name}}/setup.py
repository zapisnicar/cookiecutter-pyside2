from setuptools import setup

requirements = [
    # TODO: put your package requirements here
    'PySide2',
]

setup(
    name='{{cookiecutter.application_name}}',
    version='{{cookiecutter.version}}',
    description="{{cookiecutter.project_short_description}}",
    author="{{cookiecutter.full_name}}",
    author_email='{{cookiecutter.email}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.repo_name}}',
    packages=['{{cookiecutter.package_name}}', '{{cookiecutter.package_name}}.gui'],
#    package_data={'{{cookiecutter.package_name}}.images': ['*.png']},
    entry_points={
        'console_scripts': [
            '{{cookiecutter.application_title}}={{cookiecutter.package_name}}.app:main'
        ]
    },
    install_requires=requirements,
    zip_safe=False,
    keywords='{{cookiecutter.application_name}}',
    classifiers=[
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
