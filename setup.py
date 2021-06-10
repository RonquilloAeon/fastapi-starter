from setuptools import setup, find_packages


setup(
    name="api",
    version="0.1.0",
    install_requires=[
        "databases==0.2.6",
        "fastapi==0.65.2",
        "orm==0.1.5",
        "pydantic==1.2",
        "SQLAlchemy==1.3.11",
        "uvicorn==0.10.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.7',
)
