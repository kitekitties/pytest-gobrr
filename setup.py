from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    packages=find_packages(),
    description="A sample project for testing pytest with Buildkite test collector",
    author="Your Name",
    author_email="zomg@example.com",
    python_requires=">=3.7",
    install_requires=[],
    extras_require={
        "dev": [
            "buildkite-test-collector",
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
