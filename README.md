# Fiducial Tracker

<p>
  <a href="https://pypi.org/project/cblack/"><img src="https://img.shields.io/badge/code%20style-cblack-lightblue.svg" alt="Code Sytle: cblack" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/mahyarmirrashed/fiducial-tracker" alt="MIT License" /></a>
  <img src="https://img.shields.io/tokei/lines/github/mahyarmirrashed/fiducial-tracker" alt="Total repo lines" />
</p>

Using computer vision, track fiducials from multiple input client video streams (subset of frames captured) and publish the tracked locations to listening receivers. Shown below, multiple clients and multiple receivers can be connected to any single client.

![](res/architecture.png)

Future versions can even include brokerage systems for the darknet workers to distribute incoming computer vision works.

## Conda Environment

To provide consistent developer working environment, create a new Anaconda environment and installed the required packages (commands listed below).

```bash
conda create -n tracker python=3.8
conda activate tracker
conda install -c conda-forge mamba
mamba install -c conda-forge pyzmq opencv typing-extensions
```
