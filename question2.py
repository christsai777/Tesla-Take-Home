import os
import csv
import logging


class PowerPlant:
    def __init__(self) -> None:
        pass

    def calcluate_power_setpoints(self, filepath: os.path):
        #Create Results List to Write to Python
        results = []
        results.append(['Available PV Power', 'Available BES Power' ,'Site Load' ,
                   'Utility Export Limit','Calculated Solar Setpoint',
                   'Calculated Battery Setpoint'])
        with open(filepath, newline='') as csvfile:
            power_reader = csv.reader(csvfile, delimiter=',', quotechar='|')

            # Skip Column Titles
            next(power_reader)
            #Keep track of row number for logging purposes.
            curr = 1
            for row in power_reader:
                pw_power = int(row[0].split(' ')[0])
                bes_power = int(row[1].split(' ')[0])
                site_load = int(row[2].split(' ')[0])
                utility_output = int(row[3].split(' ')[0])
                #Find total power needed. Methodology assumes that solar power
                #will always take precedent and be used before battery power.
                total_power_needed = site_load + utility_output
                pv_power_setpoint = (pw_power if total_power_needed > 
                                        pw_power else total_power_needed)
                total_power_needed -= pv_power_setpoint
                if total_power_needed <= 0:
                    bes_power_setpoint = 0
                elif total_power_needed <= bes_power:
                    bes_power_setpoint = total_power_needed
                else:
                    bes_power_setpoint = bes_power
                    logging.warning('Not enough power for site load ' 
                                    f'and utility output in row {curr}.')
                results.append([row[0], row[1], row[2], row[3], 
                                f'{pv_power_setpoint} NM', 
                                f'{bes_power_setpoint} NM' ])
                curr += 1
        # Create backup file for input.
        os.rename(filepath, 'backup.csv')
        with open(filepath, "w") as f:
            writer = csv.writer(f)
            writer.writerows(results)    



plant = PowerPlant()
plant.calcluate_power_setpoints('power.csv')