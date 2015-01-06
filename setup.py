from distutils.core import setup

setup(
    name = "bocado",
    version = "0.1",
    author = "Emma Tosch",
    author_email = "etosch@cs.umass.edu",
    packages = ["bocado"],
    package_dir={"": "src"},
    package_data = {"": ["schemata/*", "protos/*"]},
    license = "Apache 2.0",
)
