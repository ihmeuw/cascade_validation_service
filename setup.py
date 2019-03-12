from setuptools import setup, PEP420PackageFinder

setup(
    name="cascade_validation_service",
    packages=["cascade.validation_service"],
    package_dir={"": "src"},
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    install_requires=["flask"],#, "cascade @ git+https://github.com/ihmeuw/cascade.git"],
    extras_require={
        "testing": ["pytest", "pytest-mock"],
    },
    classifiers=[
        "Intended Audience :: Science/Research",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Topic :: Scientific/Engineering :: Statistics",
    ],
)
