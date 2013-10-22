Stat-157-HW-2
=============

Members:  
--
Bonghyun Kim  
David Wang  
Hyungkyu Chang  
Sung Hoon Choi  


Preliminary Setup Steps
-----------------------
#Before running the example on iPython notebook...

In order to run the example below, it is necessary to install the packages in the virtual machine using the following codes.

    sudo apt-get install libgeos-3.3.3 python-mpltoolkits.basemap python-mpltoolkits.basemap-data python-mpltoolkits.basemap-doc python-pandas
    sudo apt-get install python-pandas
    
Also one needs to update the Pandas using the code

    sudo pip install python-dateutil --upgrade
    sudo easy_install --upgrade pytz
    sudo apt-get build-dep python-lxml
    sudo easy_install --upgrade scipy
    sudo easy_install --upgrade statsmodels
    sudo easy_install --upgrade pandas

#To Run the Code...
Run the notebook from VirtualMachine with this command:

    ipython notebook --no-browser --ip=0.0.0.0 --script --pylab=inline

#To Run the Example...
Take the file 'HW 2.ipynb' above.
It includes the code, the steps taken, problems with the example, and the roadblocks we encountered.
