# Fiducial Tracker

<p>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/mahyarmirrashed/fiducial-tracker" alt="MIT License" /></a>
  <a href="https://pypi.org/project/cblack/"><img src="https://img.shields.io/badge/code%20style-cblack-lightblue.svg" alt="Code Sytle: cblack" /></a>
  <a href="https://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg" alt="Commitizen friendly" /></a>
  <img src="https://img.shields.io/tokei/lines/github/mahyarmirrashed/fiducial-tracker" alt="Total repo lines" />
</p>

Using `darknet`, a computer vision framework, collect video streams from cameras, analyze for fiducials, and publish tracked fiducial locations to listening receivers. The server acts as a broker service that distributes analysis workload to `darknet` computer vision workers, and then periodically publishes tracked results to receivers. A diagram of the architecture is shown below.

![](res/architecture.png)

Communication between cameras and server is accomplished using REQ/REP sockets. This is so that the server can regulate the input camera feed to reduce staleness of communicated frames from video streams.

The `darknet` component connected with the `server` submodule interacts using single-threading on the server main loop. Later, multi-threading may be used to preprocess incoming frames ahead of time for object detection.

## Conda Environment

Create a new Anaconda environment and installed the required packages (commands listed below).

```bash
conda create -n fiducial-tracker python=3.8 -y
conda activate fiducial-tracker
conda install -c conda-forge mamba -y
mamba install -c conda-forge pyzmq opencv typing-extensions cachetools -yimage.png
pip3 install ormsgpack qoi
```
