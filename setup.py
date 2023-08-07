#!/usr/bin/env python

from setuptools import dist

dist.Distribution().fetch_build_eggs(['setuptools_rust'])

from setuptools import setup

from setuptools_rust import Binding, RustExtension

setup(

    name="fib_rs",

    version="0.1",

    rust_extensions=[RustExtension(

        ".fib_rs.fib_rs",

        path="Cargo.toml", binding=Binding.PyO3)],

    packages=["flitton_fib_rs"],

    classifiers=[

            "License :: OSI Approved :: MIT License",

            "Development Status :: 3 - Alpha",

            "Intended Audience :: Developers",

            "Programming Language :: Python",

            "Programming Language :: Rust",

            "Operating System :: POSIX",

            "Operating System :: MacOS :: MacOS X",

        ],

    zip_safe=False,

)