from setuptools import setup

dist = setup(name="StreetViewNumbers",
             author="Tom McClintock",
             author_email="thmsmcclintock@gmail.com",
             version="0.1.0",
             description="Identifying digits on an address.",
             url="https://github.com/tmcclintock/StreetViewNumbers",
             packages=['StreetViewNumbers'],
             install_requires=['numpy', 'scipy','tensorflow']
)
