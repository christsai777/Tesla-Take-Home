# Tesla-Take-Home

<h2> Question 1

<p>
With my understanding on solar plants, I assumed that the solar/BES inverters
were the components that were able to control the component to either turn it
higher or lower. If the inverter were to draw power out of the component instead,
then the diagram would have the inverters between the hardware commponent and
the Utility Outlet.

I made the diagram so that the operator is sitting in an office away from the 
site and has to VLAN into the power plant controller device through a firewall
and VLAN component. And then the controller device will go through a network
switch that each component is connected to and control them through the inverters.
Lastly, the meters will feed data back to the controller in case of errors or
actions that need to be taken. The DNP3 points are placed to try to do as much
of error handling as possible, measuring both the states and quality of the
hardware components and to see if any troubleshooting or red flags will appear.

</p>
<h2> Question 2
<p>
For the second question, my apporach is that we are creating an object
PowerPlant and that this is one of the numerous functions that we will create.
I am working with the assumption that for the power plant to be efficient, we
prioritize solar power over battery power whenever possible, and the amount
of power needed is site load + utility output. Then we use up as much solar as
possible, and then use battery for the rest. A warning is thrown if there is
currently not enough input power needed for output.

To read the csv, I decided against pandas and numpy since those are heavy
libraries and I could get the job done with csv. However, if this is to be
scaled further with more complicated dataframes later on, the pandas approach
would be optimal. We read in the csv, calculate the data, create a backup of the
input "backup.csv" and then write over the data which I have named 'power.csv".
I was not sure of the prompt whether it would be better to write a separate file
"power_results.csv" so I decided to follow the prompt to write over the orgiinal
file with a backup in place. While testing, I used the input file provided.

If I had more time to expand, different validation efforts would have been taken
such as making sure the column names are validated, data is formatted properly
with lambda functions, and throw additional warnings in edge cases. Also, I
would have created different csv files to test my functions with.

For the JSON schema, I used all the required fields mentioned in the prompt and
used an ID. I assumed that the JSON schema would be an "alternative" option to
using a CSV in the future for this specific function so I created it as such.
I enforced that the rating system should be from 0-100, which I assume is the
reliability of the specific hardware component.

</p>
<h1> Question 3

<p>
For question 3, my approach when I first see the problem is that I am given
a list of ip addresses and want to filter by the 3rd of the ip address which
contains the subnet. So in Python, I first import ipaddresses and format it into
a string. Next we split the ip addresses into its individual parts with the
delimiter of "." . If there is not 4 parts to the ip address, then we throw an
error. Then, we check if the subnet part equals 60, if it does, we append it 
as valid and return list of results.
</p>