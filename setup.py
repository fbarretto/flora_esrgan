#!/usr/bin/env python

from setuptools import find_packages, setup
import os
import subprocess

default_version = '0.1.0'

def readme():
    with open('README.md', encoding='utf-8') as f:
        content = f.read()
    return content

def get_git_hash():
    def _minimal_ext_cmd(cmd):
        env = {}
        for k in ['SYSTEMROOT', 'PATH', 'HOME']:
            v = os.environ.get(k)
            if v is not None:
                env[k] = v
        env['LANGUAGE'] = 'C'
        env['LANG'] = 'C'
        env['LC_ALL'] = 'C'
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE, env=env).communicate()[0]
        return out

    try:
        out = _minimal_ext_cmd(['git', 'rev-parse', 'HEAD'])
        sha = out.strip().decode('ascii')
    except OSError:
        sha = 'unknown'

    return sha

def get_hash():
    if os.path.exists('.git'):
        sha = get_git_hash()[:7]
    else:
        sha = 'unknown'

    return sha

def get_requirements(filename='requirements.txt'):
    here = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(here, filename), 'r') as f:
        requires = [line.replace('\n', '') for line in f.readlines()]
    return requires

if __name__ == '__main__':
    version = f"{default_version}+{get_hash()}" if os.path.exists('.git') else default_version
    setup(
        name='flora_esrgan',
        version=version,
        description='Enhanced Super-Resolution Generative Adversarial Networks (ESRGAN)',
        long_description=readme(),
        long_description_content_type='text/markdown',
        author='Francisco Barretto',
        author_email='francisco@florafauna.ai',
        keywords='computer vision, pytorch, image restoration, super-resolution, esrgan',
        url='https://github.com/fbarretto/flora_esrgan',
        include_package_data=True,
        packages=find_packages(include=['utils', 'utils.architecture']),
        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.10',
        ],
        license='MIT',
        setup_requires=['cython', 'numpy'],
        install_requires=get_requirements(),
        python_requires='>=3.10',
        zip_safe=False
    )