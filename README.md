# Fiducial Tracker

<p>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/mahyarmirrashed/fiducial-tracker" alt="MIT License" /></a>
  <a href="https://pypi.org/project/cblack/"><img src="https://img.shields.io/badge/code%20style-cblack-lightblue.svg" alt="Code Sytle: cblack" /></a>
  <a href="https://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg" alt="Commitizen friendly" /></a>
  <img src="https://img.shields.io/tokei/lines/github/mahyarmirrashed/fiducial-tracker" alt="Total repo lines" />
</p>

An array of cameras sends video streams to the server module. There, the server, using `pyzbar`, a QR code scanning library, analyzes for QR code fiducials, and published their tracked locations to listening clients.

![](res/architecture.png)

Communication between cameras and server is accomplished using REQ/REP sockets. This is so that the server can regulate the input camera feed to reduce staleness of communicated frames from video streams.

## Conda Environment

Create a new Anaconda environment and installed the required packages (commands listed below).

```bash
conda create -n fiducial-tracker python=3.8 -y
conda activate fiducial-tracker
conda install -c conda-forge mamba -y
mamba install -c conda-forge pyzbar pyzmq opencv typing-extensions cachetools -y
pip3 install ormsgpack qoi
```
