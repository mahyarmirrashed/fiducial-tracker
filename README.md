# Fiducial Tracker

<p>
  <a href="https://pypi.org/project/cblack/"><img src="https://img.shields.io/badge/code%20style-cblack-lightblue.svg" alt="Code Sytle: cblack" /></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/mahyarmirrashed/fiducial-tracker" alt="MIT License" /></a>
  <img src="https://img.shields.io/tokei/lines/github/mahyarmirrashed/fiducial-tracker" alt="Total repo lines" />
</p>

Using `darknet`, a computer vision framework, collect video streams from clients, analyze for fiducials, and publish tracked fiducial locations to listening receivers. The server acts as a broker service that distributes analysis workload to `darknet` computer vision workers, and then periodically publishes tracked results to receivers. A diagram of the architecture is shown below.

![](res/architecture.png)

## Conda Environment

To provide consistent developer working environment, create a new Anaconda environment and installed the required packages (commands listed below).

```bash
conda create -n fiducial-tracker python=3.8
conda activate fiducial-tracker
conda install -c conda-forge mamba
mamba install -c conda-forge pyzmq opencv typing-extensions pydantic
pip3 install ormsgpack qoi
```
