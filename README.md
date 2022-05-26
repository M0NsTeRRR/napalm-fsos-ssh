Napalm driver for FSOS using SSH

![Python test](https://github.com/M0NsTeRRR/napalm-fsos/workflows/Python%20test/badge.svg)

# Warning
This driver has been tested only on S3900 24T4S

# Install
```
pip install napalm-fsos-ssh
```

# Switch configuration

In order to use the driver you need to enable ssh:
```
ip ssh server enable
```

You also need to configure a username and password to authenticate with ssh
```
username <your_username> privilege 0
username <your_username> password 7 <your_password>
```

# Licence

The code is under CeCILL license.

You can find all details here: https://cecill.info/licences/Licence_CeCILL_V2.1-en.html

# Credits

Copyright © Ludovic Ortega, 2022

Contributor(s):

-Ortega Ludovic - ludovic.ortega@adminafk.fr