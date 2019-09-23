from setuptools import setup
requirements = [
"aiohttp",
"ujson"
]

setup(
    name='aiofaceapp',
    version='0.0.1',
    description=" Python aioFaceApp.",
    author="dark0ghost",
    url='https://github.com/dark0ghost/aiofaceapp/',
    packages=[
        'aiofaceapp',
    ],
    package_dir={'aiofaceapp':
                     'aiofaceapp'},
    include_package_data=True,
    install_requires=requirements,
    license="Apache License 2.0",
    zip_safe=False,
    keywords='aiofaceapp, faceapp',
    classifiers=[
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
