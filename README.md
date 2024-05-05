# UW HFS Dorm Availability Notifier

## Overview
This system is designed to automatically check the dormitory availability on the University of Washington's Housing & Food Services (HFS) website. It notifies the user via email when a dorm room becomes available. This tool is particularly useful for students who are looking to secure housing but face high demand and limited availability.

## Features
- **Automated Checking**: Automatically logs into the UW HFS website and checks for available dorm rooms at specified intervals.
- **Notifications**: Sends alerts through email and SMS when a dorm room matching the specified criteria becomes available.
- **User-friendly Configuration**: Easy to set up with user-defined parameters like login credentials, checking intervals, and target dorms.

## Prerequisites
Before you start using this notifier, you need to ensure that you have the following:
- Python 3.x installed on your machine.
- Pip (Python package installer) for installing dependencies.

## Installation
To set up the dorm availability notifier on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/pingw220/uw-hfs-notifier.git
   ```
2. Navigate to the cloned directory:
   ```bash
   cd uw-hfs-notifier
   ```
3. Install the required Python packages

## Configuration
Before running the script, you need to configure a few settings in the `config.json` file:
- `username`: Your UW NetID.
- `password`: Your HFS account password.
- `check_interval`: Time interval (in minutes) between each availability check.
- `email`: Email address to receive notifications.

## Usage
To start the dorm availability notifier, run the following command in the terminal:
```bash
python notifier.py
```
