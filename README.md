# Fiducial Tracker

<p>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/github/license/mahyarmirrashed/fiducial-tracker" alt="MIT License" /></a>
  <a href="https://pypi.org/project/cblack/"><img src="https://img.shields.io/badge/code%20style-cblack-lightblue.svg" alt="Code Sytle: cblack" /></a>
  <a href="https://commitizen.github.io/cz-cli/"><img src="https://img.shields.io/badge/commitizen-friendly-brightgreen.svg" alt="Commitizen friendly" /></a>
  <img src="https://img.shields.io/tokei/lines/github/mahyarmirrashed/fiducial-tracker" alt="Total repo lines" />
</p>

An array of cameras sends video streams to the server module. There, the server, using `zxingcpp`, a general purpose barcode code scanning library, analyzes for QR code fiducials, and published their tracked locations to listening clients.

![](res/architecture.png)

Communication between cameras and server is accomplished using REQ/REP sockets. This is so that the server can regulate the input camera feed to reduce staleness of communicated frames from video streams.

## Conda Environment

To run the code, setup the necessary `conda` environment by running `conda env create -f environment.yml`.

## Firebase Connection

To publish the tracked fiducial locations to your Firebase instance, set the `FIREBASE_DATABASE_URL` environment variable. If you are setting the environment with a `.env` file, create the `.env` in the same folder as this `README`. Then, download the `firebase` RTDB certificate JSON and pass it as the `--firebase-certificate` parameter for the `client` submodule.
