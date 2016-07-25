from distutils.core import setup
from io import open

def readme():
    with open('README.rst', encoding='utf-8') as f:
        return f.read()

setup(
    name = 'pycomedoresugr',
    version = '0.9',
    description = 'Biblioteca para obtener información sobre el menú de comedores de la Universidad de Granada',
    long_description=readme(),
    author = 'Alejandro Casado Quijada',
    author_email = 'acasadoquijada@gmail.com',
    url = 'https://github.com/acasadoquijada/pycomedoresugr', 
    py_modules=['pycomedoresugr'],
    install_requires=['beautifulsoup4'],
    license='GPL3',
    keywords='python comedores ugr',
    download_url='https://github.com/acasadoquijada/pycomedoresugr/releases/tag/v0.9',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ]
)


