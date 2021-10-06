import os
import setuptools

import sms_hub_api

if "requirements.txt" in os.listdir("."):
    with open("requirements.txt", encoding="utf-8") as r:
        requires = [i.strip() for i in r]  # Зависимости
else:
    requires = []

setuptools.setup(
    name="sms_hub_api",
    packages=setuptools.find_packages(),
    version=sms_hub_api.__version__,
    author="daveusa31",
    include_package_data=True,
    python_requires=">=3.6",
    install_requires=requires,
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Natural Language :: Russian",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    project_urls={"Source": "https://github.com/daveusa31/sms_hub_api"},
)
