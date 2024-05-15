import os
import logging
from setuptools import setup, Extension, Command
from Cython.Build import cythonize
from setuptools.command.build import build
import subprocess

logger = logging.getLogger(__name__)

this_dir = os.path.abspath(os.path.dirname(__file__))
libpg_dir = os.path.join(this_dir, "libpg_query")

ext_dir = "src/pg_query"

compile_envs = {
    "DEBUG": "1",
}

COMPILE_ARGS = [
    "-Og",
    "-DDEBUG",
    "-fno-omit-frame-pointer",
]
LINK_ARGS = []


class Generate(Command):
    description = "Generate the pg_query extension"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        logger.info("Generating pg_query extension")
        for k, v in compile_envs.items():
            os.environ[k] = v

        subprocess.run(["make", "-C", libpg_dir, "clean"], check=True)
        subprocess.run(["make", "-C", libpg_dir, "all"], check=True)


class CustomBuild(build):
    sub_commands = [("generate", None), *build.sub_commands]


ext = Extension(
    "pg_query",
    sources=[os.path.join(ext_dir, "__init__.py")],
    include_dirs=[libpg_dir, ext_dir],
    libraries=["pg_query"],
    library_dirs=[libpg_dir],
    extra_compile_args=COMPILE_ARGS,
    extra_link_args=LINK_ARGS,
)

setup(
    ext_modules=cythonize([ext], language_level=3),
    cmdclass={"build": CustomBuild, "generate": Generate},
)
